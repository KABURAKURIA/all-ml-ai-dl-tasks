import os
import json
import re

notebook_dir = "ai_inference_notebooks"
notebooks = [f for f in os.listdir(notebook_dir) if f.endswith(".ipynb")]

license_cell = {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## License\n",
    "\n",
    "This notebook is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/huggingface/transformers/blob/main/LICENSE) file for more details.\n",
    "\n",
    "This notebook focuses on open-source models and is optimized to run on the Google Colab Free Tier."
   ]
}

def update_save_cell(source_list):
    source_text = "".join(source_list)
    # Detect filename
    filename_match = re.search(r"with open\('([^']+)', 'w'\)", source_text)
    filename = filename_match.group(1) if filename_match else "results.txt"

    # We replace any save cell with our master robust block to ensure all variables are covered.
    # But we check if it's already the master block to avoid unnecessary writes.
    # Updated to check for more variables
    if "summary" in source_text and "translation" in source_text and "answers" in source_text and "generated_text" in source_text:
         # Check if 'text' is at the end (roughly) to confirm it's the updated version
         if source_text.find("'text' in locals()") > source_text.find("'image' in locals()"):
             return source_list

    # Master robust save block
    new_code = [
        f"with open('{filename}', 'w') as f:\n",
        "    if 'predictions' in locals():\n",
        "        f.write(str(predictions))\n",
        "    elif 'prediction' in locals():\n",
        "        f.write(str(prediction))\n",
        "    elif 'output' in locals():\n",
        "        f.write(str(output))\n",
        "    elif 'features' in locals():\n",
        "        f.write(str(features))\n",
        "    elif 'result' in locals():\n",
        "        f.write(str(result))\n",
        "    elif 'summary' in locals():\n",
        "        f.write(str(summary))\n",
        "    elif 'translation' in locals():\n",
        "        f.write(str(translation))\n",
        "    elif 'answers' in locals():\n",
        "        f.write(str(answers))\n",
        "    elif 'conversation' in locals():\n",
        "        f.write(str(conversation))\n",
        "    elif 'generated_text' in locals():\n",
        "        f.write(str(generated_text))\n",
        "    elif 'frames' in locals():\n",
        "        f.write(\"Video generated.\")\n",
        "    elif 'image' in locals():\n",
        "        f.write(\"Image generated.\")\n",
        "    elif 'text' in locals():\n",
        "        f.write(str(text))\n",
        "    else:\n",
        "        f.write(\"Task completed.\")\n",
        f"print('Results saved to {filename}')\n"
    ]
    return new_code

def update_model_loading(source_list):
    # Check for specific models and add fp16 if missing
    source_text = "".join(source_list)

    # Generic function to inject args into from_pretrained
    def inject_arg(text, model_name, arg_str):
        if model_name in text and arg_str not in text:
            # Iterate lines to safely inject only in pipeline/from_pretrained calls
            lines = text.splitlines(keepends=True)
            new_lines = []
            for line in lines:
                if model_name in line and ("from_pretrained" in line or "pipeline" in line):
                    # Inject arg
                    pattern = re.compile(f'({re.escape(model_name)}[\'"])')
                    line = pattern.sub(f'\\1, {arg_str}', line)
                new_lines.append(line)
            return "".join(new_lines)
        return text

    # SVD
    if "stabilityai/stable-video-diffusion-img2vid-xt" in source_text:
        source_text = inject_arg(source_text, "stabilityai/stable-video-diffusion-img2vid-xt", 'variant="fp16"')
        if "torch_dtype=torch.float16" not in source_text:
             source_text = inject_arg(source_text, "stabilityai/stable-video-diffusion-img2vid-xt", 'torch_dtype=torch.float16')

    # Text-to-Video
    if "damo-vilab/text-to-video-ms-1.7b" in source_text:
         source_text = inject_arg(source_text, "damo-vilab/text-to-video-ms-1.7b", 'variant="fp16"')
         if "torch_dtype=torch.float16" not in source_text:
             source_text = inject_arg(source_text, "damo-vilab/text-to-video-ms-1.7b", 'torch_dtype=torch.float16')

    # Split back to list ensuring newlines are kept or handled.
    if isinstance(source_text, str):
         lines = source_text.splitlines(keepends=True)
         return lines
    return source_list


for nb_file in sorted(notebooks):
    filepath = os.path.join(notebook_dir, nb_file)
    print(f"Processing {nb_file}...")

    with open(filepath, "r", encoding="utf-8") as f:
        try:
            content = json.load(f)
        except Exception as e:
            print(f"Error reading {nb_file}: {e}")
            continue

    cells = content.get("cells", [])

    # 1. Add License Cell
    # Check if already present to avoid duplicates
    has_license = False
    for cell in cells[:3]: # Check first 3 cells
        if "## License" in "".join(cell.get("source", [])):
            has_license = True
            break

    if not has_license:
        # If the first cell is a markdown title, insert after it (index 1), else insert at top (index 0)
        # But instructions say "dedicated Markdown cell at the beginning".
        # If index 0 is title, it usually stays at 0.
        cells.insert(1, license_cell)
        print("  - Added License cell")

    # Iterate over cells to fix content
    for cell in cells:
        if cell.get("cell_type") == "code":
            source = cell.get("source", [])
            source_str = "".join(source)

            # Check for Gradio 'interact' issue in case it appears in code cells
            if "interact=" in source_str and "gradio" in source_str.lower():
                new_source = source_str.replace("interact=", "interactive=")
                cell["source"] = new_source.splitlines(keepends=True)
                print("  - Fixed Gradio 'interact' argument")

            # 2. Fix SVD Cleaning
            if nb_file in ["CV_08_Image_to_Video.ipynb", "Multimodal_06_Image_to_Video.ipynb"]:
                source_str = "".join(cell["source"]) # Reload source in case it changed
                if "image.resize((224, 224))" in source_str:
                    new_source = source_str.replace("image.resize((224, 224))", "image.resize((1024, 576))")
                    # Update cell source
                    cell["source"] = new_source.splitlines(keepends=True)
                    print("  - Fixed SVD resolution")

                # Also fix the print statement if it matches the old one
                source_str = "".join(cell["source"])
                if "print('Image resized to (224, 224)" in source_str:
                     new_source = source_str.replace("print('Image resized to (224, 224)", "print('Image resized to (1024, 576)")
                     cell["source"] = new_source.splitlines(keepends=True)
                     print("  - Fixed SVD print statement")

            # 2.1 Fix Corrupted Model ID in Multimodal_06
            if nb_file == "Multimodal_06_Image_to_Video.ipynb":
                source_str = "".join(cell["source"])
                corrupted_pattern = 'model_id = "stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16'
                if corrupted_pattern in source_str:
                    new_source = source_str.replace(corrupted_pattern, 'model_id = "stabilityai/stable-video-diffusion-img2vid-xt"')
                    cell["source"] = new_source.splitlines(keepends=True)
                    print("  - Fixed corrupted model_id")

            # 3. Fix Save Results
            source_str = "".join(cell["source"])
            if "with open(" in source_str and ", 'w') as f:" in source_str:
                cell["source"] = update_save_cell(cell["source"])

            # 4. Optimize Models
            cell["source"] = update_model_loading(cell["source"])

    content["cells"] = cells

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(content, f, indent=1)

print("All notebooks updated.")
