# User Manual: Anima (Health Psychology)

## Overview
**Anima** is an AI-powered tool designed for the field of **Health Psychology**. It leverages the `gpt2` model to generate text based on user input, specifically tailored for:
- Generating relaxation scripts.
- Creating health behavior nudges.
- General text generation and classification.

## Installation
1. Ensure you have Python installed.
2. Install the required dependencies:
   ```bash
   pip install gradio transformers torch
   ```

## Usage
1. Run the script:
   ```bash
   python psychology_inference_tools/Anima_Gradio.py
   ```
2. Open the provided local URL (usually `http://127.0.0.1:7860`) in your web browser.
3. **Input Text:** Enter a prompt or text in the input box.
4. **Run Anima:** Click the button to process your input.
5. **Output:** The generated or classified text will appear in the output box.

## Interface
The interface is designed with a **Glassmorphic** theme, providing a modern and clean user experience.

![Anima Screenshot](anima_screenshot.png)

## Troubleshooting
- **Error loading model:** Ensure you have an internet connection to download the `gpt2` model on the first run.
- **Port already in use:** If the default port is busy, Gradio will automatically assign a new one. Check the console output for the correct URL.
