import nbformat
import os
import glob
import re
import ast

NOTEBOOKS_DIR = "ai_inference_notebooks"

LICENSE_TEXT = """## License

This notebook is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/huggingface/transformers/blob/main/LICENSE) file for more details.

This notebook focuses on open-source, lightweight, and updated models, and is optimized to run on the Google Colab Free Tier."""

LEARNING_OBJECTIVES_TEXT = """## Learning Objectives

*   **Practical:** Gain hands-on experience with this model.
*   **Theory:** Understand the underlying concepts and architecture."""

GPU_CHECK_CODE = """# Check for GPU
!nvidia-smi"""

TROUBLESHOOTING_TEXT = """## 9. Troubleshooting

*   **Out of Memory (OOM):** If you encounter OOM errors, try reducing the batch size or input length. On the Free Tier, you are limited to T4 GPUs with 16GB VRAM.
*   **GPU Not Found:** Ensure your runtime type is set to GPU. Go to *Runtime > Change runtime type* and select *T4 GPU*.
*   **Missing Packages:** If you see `ModuleNotFoundError`, make sure you have run the **Installation** step (Step 1)."""

KITCHEN_SINK_CODE = """# Kitchen Sink: Save Results
import os
import numpy as np
try:
    from PIL import Image
except ImportError:
    pass
try:
    import scipy.io.wavfile as wavfile
except ImportError:
    pass

print("Saving results...")

# 1. Text / Data / Variables
with open('results.txt', 'w') as f:
    if 'results' in locals():
        f.write(str(results))
    elif 'predictions' in locals():
        f.write(str(predictions))
    elif 'prediction' in locals():
        f.write(str(prediction))
    elif 'output' in locals():
        f.write(str(output))
    elif 'features' in locals():
        f.write(str(features))
    elif 'summary' in locals():
        f.write(str(summary))
    elif 'translation' in locals():
        f.write(str(translation))
    elif 'answers' in locals():
        f.write(str(answers))
    elif 'conversation' in locals():
        f.write(str(conversation))
    elif 'generated_text' in locals():
        f.write(str(generated_text))
    elif 'transcription' in locals():
        f.write(str(transcription))
    elif 'text' in locals():
        f.write(str(text))
    elif 'triplets' in locals():
        f.write(str(triplets))
    else:
        f.write("Task completed.")
print("Saved results.txt")

# 2. Images
if 'image' in locals():
    if hasattr(image, 'save'):
        image.save('generated_image.png')
        print("Saved generated_image.png")
elif 'images' in locals() and isinstance(images, list) and len(images) > 0:
    if hasattr(images[0], 'save'):
        images[0].save('generated_image.png')
        print("Saved generated_image.png (first image)")
    # Try to save as GIF if it's a list of images (for video/3D)
    try:
        from diffusers.utils import export_to_gif
        export_to_gif(images, "generated_video.gif")
        print("Saved generated_video.gif")
    except:
        # Fallback for standard list of PIL images
        try:
            images[0].save("generated_video.gif", save_all=True, append_images=images[1:], duration=100, loop=0)
            print("Saved generated_video.gif")
        except:
            pass

# Graph Visualization (specific to Graph RAG)
if os.path.exists("graph_visualization.png"):
    import shutil
    shutil.copy("graph_visualization.png", "generated_image.png")
    print("Saved generated_image.png from graph_visualization.png")

# 3. Audio
if 'audio' in locals():
    if isinstance(audio, tuple):
        rate, data = audio
        try:
            wavfile.write('generated_audio.wav', rate, data)
            print("Saved generated_audio.wav")
        except:
            pass
    elif hasattr(audio, 'ndim'): # numpy array
        rate = save_rate if 'save_rate' in locals() else 16000
        try:
            wavfile.write('generated_audio.wav', rate, audio)
            print("Saved generated_audio.wav")
        except:
            pass
elif 'audio_data' in locals():
    rate = save_rate if 'save_rate' in locals() else 16000
    try:
        wavfile.write('generated_audio.wav', rate, audio_data)
        print("Saved generated_audio.wav")
    except:
        pass
"""

EXPECTED_HEADERS = {
    1: "1. Installation",
    2: "2. Imports",
    3: "3. Load Data",
    4: "4. Data Cleaning",
    5: "5. Load Model",
    6: "6. Inference",
    7: "7. Save Results",
    8: "8. Advanced Usage"
}

def clean_header(source):
    """Normalize header text to check against expected."""
    return source.strip().lstrip('#').strip()

def clean_empty_cells(nb):
    """Remove empty code or markdown cells."""
    new_cells = []
    removed = False
    for cell in nb.cells:
        if cell.source.strip() == "":
            removed = True
        else:
            new_cells.append(cell)

    if removed:
        nb.cells = new_cells
        return True
    return False

def check_title(nb, filepath):
    """Ensure the first cell is a markdown Title."""
    if not nb.cells:
        return False

    first_cell = nb.cells[0]
    if first_cell.cell_type != 'markdown' or not first_cell.source.strip().startswith('# '):
        print(f"  WARNING: {filepath} missing proper Title in first cell.")
        # We don't auto-fix this easily as we don't know the title, but we warn.
        # Could potentially infer from filename but better to let user handle or just warn.
        # For now, we will prepend a generic title if completely missing to enforce structure
        filename = os.path.basename(filepath).replace(".ipynb", "").replace("_", " ")
        print(f"  Prepending generic title: # {filename}")
        nb.cells.insert(0, nbformat.v4.new_markdown_cell(f"# {filename}\n\n## Task Description\nAutomated description."))
        return True
    return False

def check_syntax(nb, filepath):
    """Check for Python syntax errors in code cells."""
    for idx, cell in enumerate(nb.cells):
        if cell.cell_type == 'code':
            source = cell.source
            # Filter out magic commands
            clean_source = []
            for line in source.split('\n'):
                if line.strip().startswith('!') or line.strip().startswith('%'):
                    pass
                else:
                    clean_source.append(line)
            clean_source = '\n'.join(clean_source)

            if clean_source.strip():
                try:
                    ast.parse(clean_source)
                except SyntaxError as e:
                    print(f"  ERROR: Syntax error in {filepath} (Cell {idx}): {e}")

def check_optimization(nb, filepath):
    """Check for optimization flags when loading models."""
    for cell in nb.cells:
        if cell.cell_type == 'code':
            if 'from_pretrained' in cell.source:
                # Check for quantization or float16
                optimized = False
                keywords = ['load_in_4bit', 'load_in_8bit', 'torch.float16', 'torch.bfloat16']
                for kw in keywords:
                    if kw in cell.source:
                        optimized = True
                        break

                if not optimized:
                    print(f"  WARNING: 'from_pretrained' used without optimization in {filepath}. Consider 'load_in_4bit' or 'torch.float16'.")

def check_for_heavy_models(nb, filepath):
    heavy_keywords = ["70b", "405b", "gpt-4", "claude-3", "gemini-1.5", "Mixtral", "Grok", "DeepSeek-V3"]
    for cell in nb.cells:
        if cell.cell_type == 'code':
            for kw in heavy_keywords:
                if kw in cell.source:
                    print(f"  WARNING: Potential heavy model '{kw}' detected in {filepath}. Ensure compatibility with Colab Free Tier.")

def fix_regressions(nb, filepath):
    """Apply specific fixes for known regressions."""
    changes = False

    # NLP_09 Fix
    if "NLP_09_Text_Generation.ipynb" in filepath:
        # Move chat template logic if needed (simplified from original script)
        # We will iterate to find steps
        step3_idx = -1
        step6_idx = -1
        current_step = 0
        for idx, cell in enumerate(nb.cells):
            if cell.cell_type == 'markdown':
                if '## 3. Load Data' in cell.source: current_step = 3
                elif '## 6. Inference' in cell.source: current_step = 6
            if cell.cell_type == 'code':
                if current_step == 3 and 'tokenizer.apply_chat_template' in cell.source: step3_idx = idx
                if current_step == 6 and step6_idx == -1: step6_idx = idx

        if step3_idx != -1 and step6_idx != -1:
            print("  Applying fix for NLP_09...")
            lines = nb.cells[step3_idx].source.split('\n')
            new_step3 = []
            moved = []
            for line in lines:
                if 'tokenizer.apply_chat_template' in line or 'input_text =' in line: moved.append(line)
                else: new_step3.append(line)
            nb.cells[step3_idx].source = '\n'.join(new_step3).strip()
            nb.cells[step6_idx].source = '\n'.join(moved) + "\n" + nb.cells[step6_idx].source
            changes = True

    # CV_23 Fix
    if "CV_23_Explainable_AI.ipynb" in filepath:
        # Ensure image is assigned for Kitchen Sink
        found_inference = False
        for idx, cell in enumerate(nb.cells):
            if cell.cell_type == 'markdown' and '## 6. Inference' in cell.source:
                found_inference = True
            elif found_inference and cell.cell_type == 'code':
                if "image = result_image" not in cell.source:
                    print("  Fixing CV_23: Assigning result_image to image...")
                    cell.source += "\n\n# Assign to 'image' for Kitchen Sink saver\nimage = result_image"
                    changes = True
                break

    # NLP_26 Fix
    if "NLP_26_Explainable_AI.ipynb" in filepath:
        # Ensure SHAP plot is saved
        found_inference = False
        for idx, cell in enumerate(nb.cells):
            if cell.cell_type == 'markdown' and '## 6. Inference' in cell.source:
                found_inference = True
            elif found_inference and cell.cell_type == 'code':
                if "shap.plots.bar" not in cell.source:
                    print("  Fixing NLP_26: Adding SHAP plot saving...")
                    addition = """
# 3. Generate and Save Plot
shap.plots.bar(shap_values[0], show=False)
plt.savefig("shap_bar.png", bbox_inches='tight')
print("Saved shap_bar.png")

# Load for Kitchen Sink
try:
    from PIL import Image
    image = Image.open("shap_bar.png")
except:
    pass

results = str(shap_values)
"""
                    cell.source += addition
                    changes = True
                break

    return changes

def update_notebook(filepath):
    print(f"Updating {filepath}...")
    try:
        nb = nbformat.read(filepath, as_version=4)
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return

    changes_made = False

    # 0. Clean Empty Cells
    if clean_empty_cells(nb):
        changes_made = True

    # 0.5 Check Title
    if check_title(nb, filepath):
        changes_made = True

    # 1. License Cell (Index 1)
    if len(nb.cells) > 1:
        cell1 = nb.cells[1]
        if cell1.cell_type != 'markdown' or cell1.source.strip() != LICENSE_TEXT.strip():
            print("  Inserting/Updating License cell...")
            license_cell = nbformat.v4.new_markdown_cell(LICENSE_TEXT)
            if cell1.cell_type == 'markdown' and 'License' in cell1.source:
                nb.cells[1] = license_cell
            else:
                nb.cells.insert(1, license_cell)
            changes_made = True

    # 2. Learning Objectives (Index 2)
    if len(nb.cells) > 2:
        cell2 = nb.cells[2]
        if cell2.cell_type != 'markdown' or "Learning Objectives" not in cell2.source:
             print("  Inserting Learning Objectives at Index 2...")
             lo_cell = nbformat.v4.new_markdown_cell(LEARNING_OBJECTIVES_TEXT)
             nb.cells.insert(2, lo_cell)
             changes_made = True

    # 3. GPU Check (Index 3)
    if len(nb.cells) > 3:
        cell3 = nb.cells[3]
        if cell3.cell_type != 'code' or "!nvidia-smi" not in cell3.source:
             print("  Inserting GPU Check at Index 3...")
             gpu_cell = nbformat.v4.new_code_cell(GPU_CHECK_CODE)
             nb.cells.insert(3, gpu_cell)
             changes_made = True

    # 4. Header Standardization
    step_indices = {}
    for idx, cell in enumerate(nb.cells):
        if cell.cell_type == 'markdown':
            lines = cell.source.split('\n')
            header_line = next((l for l in lines if l.startswith('##')), None)
            if header_line:
                clean = clean_header(header_line)
                step_num = None
                if 'Installation' in clean: step_num = 1
                elif 'Imports' in clean: step_num = 2
                elif 'Load Data' in clean: step_num = 3
                elif 'Data Cleaning' in clean: step_num = 4
                elif 'Load Model' in clean: step_num = 5
                elif 'Inference' in clean: step_num = 6
                elif 'Save Results' in clean: step_num = 7
                elif 'Advanced Usage' in clean: step_num = 8

                if step_num:
                    expected = EXPECTED_HEADERS[step_num]
                    if not header_line.startswith(f"## {expected}"):
                        print(f"  Updating header: {header_line} -> ## {expected}")
                        new_lines = []
                        replaced = False
                        for l in lines:
                            if l.startswith('##') and not replaced:
                                new_lines.append(f"## {expected}")
                                replaced = True
                            else:
                                new_lines.append(l)
                        cell.source = '\n'.join(new_lines)
                        changes_made = True
                    step_indices[step_num] = idx

    # 5. Kitchen Sink (Step 7)
    if 7 in step_indices:
        step7_idx = step_indices[7]
        if step7_idx + 1 < len(nb.cells):
            next_cell = nb.cells[step7_idx + 1]
            if next_cell.cell_type == 'code':
                if next_cell.source.strip() != KITCHEN_SINK_CODE.strip():
                     print("  Updating Kitchen Sink to latest version...")
                     next_cell.source = KITCHEN_SINK_CODE
                     changes_made = True
            else:
                 print("  Inserting Kitchen Sink code cell...")
                 new_cell = nbformat.v4.new_code_cell(KITCHEN_SINK_CODE)
                 nb.cells.insert(step7_idx + 1, new_cell)
                 changes_made = True

    # 6. Regressions & Fixes
    if fix_regressions(nb, filepath):
        changes_made = True

    # 7. Teaching Tip (Step 8)
    if 8 in step_indices:
        step8_idx = step_indices[8]
        step8_cell = nb.cells[step8_idx]
        if "Teaching Tip:" not in step8_cell.source:
             print("  Adding Teaching Tip to Step 8...")
             step8_cell.source += "\n\n**Teaching Tip:** Try varying the input parameters or prompts to see how the model's output changes. This helps build intuition about the model's capabilities and limitations."
             changes_made = True

    # 8. Troubleshooting (Step 9)
    has_step9 = False
    for cell in nb.cells:
        if cell.cell_type == 'markdown' and '## 9. Troubleshooting' in cell.source:
            has_step9 = True
            break
    if not has_step9:
        print("  Appending Troubleshooting (Step 9)...")
        nb.cells.append(nbformat.v4.new_markdown_cell(TROUBLESHOOTING_TEXT))
        changes_made = True

    # 9. Checks (No changes, just warnings)
    check_for_heavy_models(nb, filepath)
    check_optimization(nb, filepath)
    check_syntax(nb, filepath)

    if changes_made:
        nbformat.write(nb, filepath)
        print(f"  Saved changes to {filepath}")
    else:
        print("  No changes needed.")

def main():
    notebooks = sorted(glob.glob(os.path.join(NOTEBOOKS_DIR, "*.ipynb")))
    print(f"Found {len(notebooks)} notebooks.")
    for nb_path in notebooks:
        update_notebook(nb_path)

if __name__ == "__main__":
    main()
