import os
import glob
import re

TOOLS_DIR = "psychology_inference_tools"
MANUALS_DIR = "manuals"
SCREENSHOT_DIR = os.path.join(MANUALS_DIR, "screenshots")
MANUAL_FILE = os.path.join(MANUALS_DIR, "USER_MANUAL.md")

HEADER = """# Psychology Inference Tools User Manual

## Introduction
This manual provides a comprehensive guide to the AI-powered psychology inference tools generated in this repository. Each tool is designed for a specific domain within psychology, leveraging state-of-the-art NLP models to assist researchers, students, and practitioners.

## General Usage
- **Streamlit Tools:** Run with `streamlit run <tool_name>.py`. Access at `http://localhost:8501`.
- **Gradio Tools:** Run with `python <tool_name>.py`. Access at `http://localhost:7860`.

---

# Tools Catalog

"""

def get_tool_metadata(tool_path):
    try:
        with open(tool_path, "r") as f:
            content = f.read()

        # Try to find field
        field = "General Psychology"
        # Gradio: **Field:** Value
        g_match = re.search(r"\*\*Field:\*\*\s*(.+?)\\n", content)
        if g_match:
            field = g_match.group(1).strip()

        # Streamlit: <b>Field:</b> Value
        s_match = re.search(r"<b>Field:</b>\s*(.+?)</p>", content)
        if s_match:
            field = s_match.group(1).strip()

        return field
    except:
        return "Unknown"

def generate_manual():
    print("Generating manual from existing screenshots...")

    screenshots = sorted(glob.glob(os.path.join(SCREENSHOT_DIR, "*.png")))
    catalog_entries = []

    for screenshot in screenshots:
        filename = os.path.basename(screenshot)
        tool_name = filename.replace(".png", "")

        # Find corresponding tool file
        # We need to guess the extension or try both?
        # The tool name in screenshot usually matches the python file name prefix?
        # My verification script names screenshot as `{tool_name}.png` where tool_name is filename without .py.
        # So `Aether_Gradio.png` corresponds to `Aether_Gradio.py`.

        tool_path = os.path.join(TOOLS_DIR, f"{tool_name}.py")
        if not os.path.exists(tool_path):
            print(f"Warning: Tool file not found for {tool_name}")
            continue

        field = get_tool_metadata(tool_path)

        entry = f"## {tool_name}\n"
        entry += f"**Field:** {field}\n\n"
        entry += f"**File:** `{tool_path}`\n\n"
        entry += f"![{tool_name}](screenshots/{filename})\n\n"
        entry += "---\n"
        catalog_entries.append(entry)

    full_content = HEADER + "\n".join(catalog_entries)
    with open(MANUAL_FILE, "w") as f:
        f.write(full_content)

    print(f"Manual generated at {MANUAL_FILE} with {len(catalog_entries)} entries.")

if __name__ == "__main__":
    generate_manual()
