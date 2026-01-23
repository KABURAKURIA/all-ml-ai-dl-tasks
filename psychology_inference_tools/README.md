# Psychology Inference Tools

This directory contains over 125 unique inference tools designed for various fields of general and applied psychology. Each tool is a standalone application built with either [Streamlit](https://streamlit.io/) or [Gradio](https://gradio.app/), featuring distinct "Glassmorphic" or "Neobrutalistic" user interface styles.

## Overview

The tools cover a wide range of psychological domains, including but not limited to:
- Clinical Psychology
- Cognitive Psychology
- Social Psychology (Sentiment & Emotion Analysis)
- Behavioral Psychology
- Industrial-Organizational Psychology
- Developmental Psychology
- Forensic Psychology
- Neuropsychology
- Sports Psychology
- Cyberpsychology

Each tool utilizes specific Hugging Face `transformers` models tailored to the task, such as text generation, classification, summarization, and question-answering.

## UI Styles

The tools are designed with two unique visual themes:
*   **Glassmorphic:** A modern, frosted-glass aesthetic with gradients and translucency.
*   **Neobrutalistic:** A bold, high-contrast design with stark borders and vibrant colors.

## Installation

Ensure you have the required dependencies installed:

```bash
pip install -r ../requirements.txt
```

## How to Run

### Streamlit Tools
To run a Streamlit tool (files ending in `_Streamlit.py`), use the following command:

```bash
streamlit run <ToolName>_Streamlit.py
```

Example:
```bash
streamlit run Bolt_Streamlit.py
```

### Gradio Tools
To run a Gradio tool (files ending in `_Gradio.py`), simply execute the Python script:

```bash
python <ToolName>_Gradio.py
```

Example:
```bash
python Haze_Gradio.py
```

## Disclaimer
These tools are for educational and demonstration purposes only. They use AI models to simulate psychological insights and should not be used as a substitute for professional psychological advice, diagnosis, or treatment.
