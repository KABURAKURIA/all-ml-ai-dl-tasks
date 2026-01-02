# AI Inference Notebooks

This folder contains a set of Jupyter Notebooks designed to introduce you to AI and Machine Learning tasks using open-source models.

**No programming experience is required!** The notebooks are heavily documented and explain every step.

## How to use

1.  Open these notebooks in a Jupyter environment (like JupyterLab, VS Code with Jupyter extension, or Google Colab).
2.  Start with `01_Setup_and_Introduction.ipynb`. It will guide you through installing the necessary tools.
3.  Proceed through the notebooks in order:
    - `02_NLP_and_LLMs.ipynb`: Working with text.
    - `03_Computer_Vision.ipynb`: Working with images.
    - `04_Audio_Tasks.ipynb`: Working with audio.

## Requirements

These notebooks rely on Python and several libraries, mainly:
- `transformers` (by Hugging Face)
- `torch` (PyTorch)

The first notebook will help you install them.

## Troubleshooting

If you encounter errors related to missing modules, ensure you have run the installation cell in the first notebook.
If you are running this locally (not on Colab), you might need to install `ffmpeg` for audio processing tasks, though `soundfile` usually covers the basics.
