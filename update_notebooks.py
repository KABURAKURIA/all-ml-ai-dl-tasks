import nbformat
import os
import glob
import re

NOTEBOOKS_DIR = "ai_inference_notebooks"
LICENSE_TEXT = """## License

This notebook is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/huggingface/transformers/blob/main/LICENSE) file for more details.

This notebook focuses on open-source, lightweight, and updated models, and is optimized to run on the Google Colab Free Tier."""

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

def fix_nlp_09(nb):
    """Specific fix for NLP_09_Text_Generation.ipynb"""
    # Find Step 3 and Step 6 code cells
    step3_idx = -1
    step6_idx = -1

    current_step = 0
    for idx, cell in enumerate(nb.cells):
        if cell.cell_type == 'markdown':
            content = cell.source.strip()
            if content.startswith('## 3. Load Data'):
                current_step = 3
            elif content.startswith('## 6. Inference'):
                current_step = 6

        if cell.cell_type == 'code':
            if current_step == 3 and 'tokenizer.apply_chat_template' in cell.source:
                step3_idx = idx
            if current_step == 6 and step6_idx == -1: # First code cell of step 6
                step6_idx = idx

    if step3_idx != -1 and step6_idx != -1:
        print("  Applying fix for NLP_09: Moving chat template logic...")
        # Extract lines
        lines = nb.cells[step3_idx].source.split('\n')
        new_step3_lines = []
        moved_lines = []
        for line in lines:
            if 'tokenizer.apply_chat_template' in line or 'input_text =' in line:
                moved_lines.append(line)
            else:
                new_step3_lines.append(line)

        nb.cells[step3_idx].source = '\n'.join(new_step3_lines).strip()

        # Insert into Step 6
        current_step6_source = nb.cells[step6_idx].source
        nb.cells[step6_idx].source = '\n'.join(moved_lines) + "\n" + current_step6_source
        return True
    return False

def update_notebook(filepath):
    print(f"Updating {filepath}...")
    try:
        nb = nbformat.read(filepath, as_version=4)
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return

    changes_made = False

    # 1. License Cell (Index 1)
    # Check if cell 1 is license
    if len(nb.cells) > 1:
        cell1 = nb.cells[1]
        if cell1.cell_type != 'markdown' or cell1.source.strip() != LICENSE_TEXT.strip():
            print("  Inserting/Updating License cell...")
            license_cell = nbformat.v4.new_markdown_cell(LICENSE_TEXT)
            # If cell 1 looks like a license but wrong, replace it. If it's something else, insert.
            if cell1.cell_type == 'markdown' and 'License' in cell1.source:
                nb.cells[1] = license_cell
            else:
                nb.cells.insert(1, license_cell)
            changes_made = True

    # 2. Header Standardization
    # Iterate and try to match headers
    step_indices = {}
    for idx, cell in enumerate(nb.cells):
        if cell.cell_type == 'markdown':
            lines = cell.source.split('\n')
            header_line = next((l for l in lines if l.startswith('##')), None)
            if header_line:
                clean = clean_header(header_line)
                # Try to identify step
                step_num = None
                if 'Installation' in clean: step_num = 1
                elif 'Imports' in clean: step_num = 2
                elif 'Load Data' in clean: step_num = 3
                elif 'Data Cleaning' in clean: step_num = 4
                elif 'Load Model' in clean: step_num = 5
                elif 'Inference' in clean: step_num = 6
                elif 'Save Results' in clean: step_num = 7
                elif 'Advanced Usage' in clean: step_num = 8

                # Also check for numbers like "3. Load Model" which might be wrong step
                match = re.search(r'(\d+)\.', clean)
                if match and not step_num:
                    # Fallback to number if name doesn't match, but be careful
                    pass

                if step_num:
                    expected = EXPECTED_HEADERS[step_num]
                    # Update header if it doesn't match exactly (e.g. wrong number)
                    if not header_line.startswith(f"## {expected}"):
                        print(f"  Updating header: {header_line} -> ## {expected}")
                        # Replace the header line in the source
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

    # 3. Kitchen Sink (Step 7)
    if 7 in step_indices:
        step7_idx = step_indices[7]
        # Look for the code cell after Step 7 header
        if step7_idx + 1 < len(nb.cells):
            next_cell = nb.cells[step7_idx + 1]
            if next_cell.cell_type == 'code':
                # Check if it already has kitchen sink
                if 'if \'results\' in locals():' not in next_cell.source:
                    print("  Appending Kitchen Sink logic...")
                    # Append, don't overwrite if there's manual save
                    next_cell.source += "\n\n" + KITCHEN_SINK_CODE
                    changes_made = True
            else:
                 # Insert new code cell
                 print("  Inserting Kitchen Sink code cell...")
                 new_cell = nbformat.v4.new_code_cell(KITCHEN_SINK_CODE)
                 nb.cells.insert(step7_idx + 1, new_cell)
                 changes_made = True

    # 4. Fix NLP_09
    if "NLP_09_Text_Generation.ipynb" in filepath:
        if fix_nlp_09(nb):
            changes_made = True

    # 5. Teaching Tip (Step 8)
    if 8 in step_indices:
        step8_idx = step_indices[8]
        step8_cell = nb.cells[step8_idx]
        if "Teaching Tip:" not in step8_cell.source:
             print("  Adding Teaching Tip to Step 8...")
             step8_cell.source += "\n\n**Teaching Tip:** Try varying the input parameters or prompts to see how the model's output changes. This helps build intuition about the model's capabilities and limitations."
             changes_made = True

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
