import nbformat
import os

NOTEBOOKS_DIR = "ai_inference_notebooks"

def fix_cv_23():
    filepath = os.path.join(NOTEBOOKS_DIR, "CV_23_Explainable_AI.ipynb")
    print(f"Fixing {filepath}...")
    nb = nbformat.read(filepath, as_version=4)

    # Locate Step 6
    step6_idx = -1
    for idx, cell in enumerate(nb.cells):
        if cell.cell_type == 'markdown' and '## 6. Inference' in cell.source:
            # The next code cell is Step 6
            if idx + 1 < len(nb.cells) and nb.cells[idx+1].cell_type == 'code':
                step6_idx = idx + 1
                break

    if step6_idx != -1:
        source = nb.cells[step6_idx].source
        if "image = result_image" not in source:
            print("  Appending 'image = result_image' to Step 6...")
            nb.cells[step6_idx].source = source + "\n\n# Assign to 'image' for Kitchen Sink saver\nimage = result_image"
            nbformat.write(nb, filepath)
            print("  Saved.")
        else:
            print("  Already fixed.")
    else:
        print("  Step 6 not found.")

def fix_nlp_26():
    filepath = os.path.join(NOTEBOOKS_DIR, "NLP_26_Explainable_AI.ipynb")
    print(f"Fixing {filepath}...")
    nb = nbformat.read(filepath, as_version=4)

    # Locate Step 6
    step6_idx = -1
    for idx, cell in enumerate(nb.cells):
        if cell.cell_type == 'markdown' and '## 6. Inference' in cell.source:
             if idx + 1 < len(nb.cells) and nb.cells[idx+1].cell_type == 'code':
                step6_idx = idx + 1
                break

    if step6_idx != -1:
        source = nb.cells[step6_idx].source
        if "shap.plots.bar" not in source:
            print("  Appending SHAP plot generation to Step 6...")
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
            nb.cells[step6_idx].source = source + addition
            nbformat.write(nb, filepath)
            print("  Saved.")
        else:
            print("  Already fixed.")
    else:
        print("  Step 6 not found.")

if __name__ == "__main__":
    fix_cv_23()
    fix_nlp_26()
