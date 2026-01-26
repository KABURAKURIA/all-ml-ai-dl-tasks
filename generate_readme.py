import glob
import os
import nbformat
import re

NOTEBOOKS_DIR = "ai_inference_notebooks"
README_PATH = os.path.join(NOTEBOOKS_DIR, "README.md")

HEADER = """# AI Inference Notebooks

This folder contains **{count}** "In-Depth" Jupyter Notebooks. Each notebook is dedicated to a specific AI/ML task, using real-world datasets and models from the Hugging Face ecosystem.

**Features:**
- **No programming experience required**: Each step is explained.
- **In-Depth**: Covers installation, library imports, data loading (using `datasets` or real URLs), model loading, inference, and analysis.
- **Visual**: Includes image displays, audio playback, and structured outputs.

## Categories
"""

FOOTER = """
## Usage
Run the installation cell at the top of each notebook.
Most notebooks require a GPU for optimal performance (especially Video and Image generation tasks).
"""

CATEGORY_MAP = {
    "Multimodal": "Multimodal",
    "NLP": "Natural Language Processing (NLP)",
    "CV": "Computer Vision (CV)",
    "Audio": "Audio",
    "Tabular": "Tabular, Graphs & RL",
    "Graph": "Tabular, Graphs & RL",
    "RL": "Tabular, Graphs & RL"
}

CATEGORY_ORDER = [
    "Multimodal",
    "Natural Language Processing (NLP)",
    "Computer Vision (CV)",
    "Audio",
    "Tabular, Graphs & RL"
]

def get_notebook_info(filepath):
    try:
        nb = nbformat.read(filepath, as_version=4)
        if not nb.cells:
            return None, None

        first_cell = nb.cells[0]
        if first_cell.cell_type != 'markdown':
            return None, None

        source = first_cell.source
        lines = source.split('\n')

        title = "Untitled"
        description = "No description."

        # Extract Title
        for line in lines:
            if line.startswith('# '):
                title = line.strip('# ').strip()
                break

        # Extract Description logic
        found_task_bold = False
        found_task_header = False
        captured_desc = None

        for i, line in enumerate(lines):
            line = line.strip()

            # Check for **Task:** style
            if "**Task:**" in line:
                captured_desc = line.replace("**Task:**", "").strip()
                found_task_bold = True
                break

            # Check for ## Task Description style
            if "## Task Description" in line:
                found_task_header = True
                continue

            if found_task_header:
                if line and not line.startswith('#'):
                    captured_desc = line
                    break

        if captured_desc:
            description = captured_desc
        else:
            # Fallback: First non-empty line after title that isn't a header
            found_title = False
            for line in lines:
                if line.startswith('# '):
                    found_title = True
                    continue
                if found_title:
                    if line.startswith('#'): # Subheader
                         # Exception: if we didn't match "Task Description" explicitly above,
                         # maybe we still want to skip generic headers.
                         continue
                    if line.strip():
                        description = line.strip()
                        break

        return title, description

    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None, None

def main():
    notebooks = sorted(glob.glob(os.path.join(NOTEBOOKS_DIR, "*.ipynb")))
    data = {}

    for nb_path in notebooks:
        filename = os.path.basename(nb_path)
        prefix = filename.split('_')[0]

        cat_key = CATEGORY_MAP.get(prefix, "Others")

        title, description = get_notebook_info(nb_path)

        if not title:
            continue

        if cat_key not in data:
            data[cat_key] = []

        data[cat_key].append(f"{filename}: {description}")

    # Generate Markdown
    content = HEADER.format(count=len(notebooks))

    for cat in CATEGORY_ORDER:
        if cat in data:
            content += f"\n### {cat}\n"
            for i, item in enumerate(data[cat], 1):
                parts = item.split(': ', 1)
                fname = parts[0]
                desc = parts[1] if len(parts) > 1 else ""
                content += f"{i}.  `{fname}`: {desc}\n"

    content += FOOTER

    with open(README_PATH, 'w') as f:
        f.write(content)

    print(f"Generated README.md with {len(notebooks)} notebooks.")

if __name__ == "__main__":
    main()
