import os
import time
import subprocess
import glob
import re
import sys
import requests
from multiprocessing import Process, Manager
from playwright.sync_api import sync_playwright

TOOLS_DIR = "psychology_inference_tools"
MANUALS_DIR = "manuals"
SCREENSHOT_DIR = os.path.join(MANUALS_DIR, "screenshots")
MANUAL_FILE = os.path.join(MANUALS_DIR, "USER_MANUAL.md")

# Ensure directories exist
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

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

def verify_worker(worker_id, tools_chunk, results_list):
    print(f"Worker {worker_id} started with {len(tools_chunk)} tools.")

    # Define ports for this worker
    # Streamlit defaults to 8501. Gradio defaults to 7860.
    streamlit_port = 8501 + (worker_id * 10)
    gradio_port = 7900 + (worker_id * 10)

    for tool_path in tools_chunk:
        tool_name = os.path.basename(tool_path).replace(".py", "")
        is_streamlit = "Streamlit" in tool_name

        print(f"[Worker {worker_id}] Verifying {tool_name}...")

        port = streamlit_port if is_streamlit else gradio_port
        url = f"http://localhost:{port}"

        env = os.environ.copy()
        if is_streamlit:
            cmd = ["streamlit", "run", tool_path, "--server.port", str(port), "--server.headless", "true"]
        else:
            cmd = ["python", tool_path]
            env["GRADIO_SERVER_PORT"] = str(port)

        process = subprocess.Popen(cmd, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Give it time to start
        time.sleep(5)

        screenshot_filename = None
        verified = False

        try:
            # Try simple request first to see if it's up
            for _ in range(10):
                try:
                    requests.get(url, timeout=2)
                    verified = True
                    break
                except:
                    time.sleep(1)

            if verified:
                try:
                    with sync_playwright() as p:
                        browser = p.chromium.launch(headless=True)
                        page = browser.new_page()
                        page.goto(url, timeout=5000)
                        page.wait_for_timeout(2000)
                        screenshot_filename = f"{tool_name}.png"
                        screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_filename)
                        page.screenshot(path=screenshot_path)
                        print(f"[Worker {worker_id}] Screenshot captured for {tool_name}")
                        browser.close()
                except Exception as e:
                    print(f"[Worker {worker_id}] Screenshot failed for {tool_name}: {e}")
                    # If screenshot fails, we still consider it verified if requests worked
                    # We just won't have an image
            else:
                print(f"[Worker {worker_id}] Failed to connect to {tool_name}")

        except Exception as e:
             print(f"[Worker {worker_id}] Error verifying {tool_name}: {e}")

        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except:
                process.kill()
            # Wait for port to clear
            time.sleep(1)

        if verified:
            field = get_tool_metadata(tool_path)
            entry = f"## {tool_name}\n**Field:** {field}\n\n**File:** `{tool_path}`\n\n"
            if screenshot_filename:
                entry += f"![{tool_name}](screenshots/{screenshot_filename})\n\n"
            else:
                entry += f"*Screenshot not available*\n\n"
            entry += "---\n"
            results_list.append(entry)

if __name__ == "__main__":
    tools = sorted(glob.glob(os.path.join(TOOLS_DIR, "*.py")))
    print(f"Found {len(tools)} tools.")

    num_workers = 1 # Sequential to ensure stability

    # Split tools
    chunks = [tools[i::num_workers] for i in range(num_workers)]

    manager = Manager()
    results_list = manager.list()

    processes = []
    for i in range(num_workers):
        p = Process(target=verify_worker, args=(i, chunks[i], results_list))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    # Write Manual
    # Sort results by tool name to maintain order
    sorted_results = sorted(list(results_list), key=lambda x: x.split('\n')[0])

    full_content = HEADER + "\n".join(sorted_results)
    with open(MANUAL_FILE, "w") as f:
        f.write(full_content)

    print(f"Manual generated at {MANUAL_FILE} with {len(sorted_results)} entries.")
