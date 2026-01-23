# AI Agents Directive: Notebook Structure & Quality

The scope of this `AGENTS.md` file is the `ai_inference_notebooks/` directory. All Jupyter Notebooks in this folder must adhere to the following strict guidelines to ensure consistency, quality, and teachability.

## 1. The 8-Step Structure

Every notebook must follow this exact 8-step structure. Sections must be numbered clearly in Markdown headers.

1.  **Installation**: Install all necessary libraries. Always include `!pip install` commands. Use `-q` for quiet installation where appropriate.
2.  **Imports**: Import all Python libraries.
3.  **Load Data**: Load the dataset or define input data.
4.  **Data Cleaning**: Preprocess the data (e.g., resizing images, cleaning text).
5.  **Load Model**: Load the model and tokenizer/processor.
6.  **Inference**: Run the model on the data.
7.  **Save Results**: Save the output using the "Kitchen Sink" pattern.
8.  **Advanced Usage**: Provide suggestions for further exploration (e.g., different models, hyperparameters).

## 2. Mandatory License Cell

The **second cell** (Index 1) of every notebook must be a Markdown cell containing the following License information:

```markdown
## License

This notebook is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/huggingface/transformers/blob/main/LICENSE) file for more details.

This notebook focuses on open-source models and is optimized to run on the Google Colab Free Tier.
```

## 3. "Kitchen Sink" Saving Logic

Step 7 (Save Results) must implement a robust saving mechanism that checks for various variable names (`results`, `predictions`, `generated_text`, `image`, `audio`, etc.) and saves them appropriately. This ensures that whatever the task, the result is captured.

*   **Text/Data**: Save to `results.txt`.
*   **Images**: Save PIL images to `generated_image.png`.
*   **Audio**: Save numpy arrays to `generated_audio.wav`.

## 4. Environment & Models

*   **Google Colab Free Tier**: All code must run on the free tier (T4 GPU). Avoid models that are too large (e.g., >7B parameters in full precision, though quantized is fine if it fits VRAM).
*   **Open Source**: Prioritize truly open-source models (Apache 2.0, MIT) available on Hugging Face.
*   **Lightweight**: Use `float16` or 4-bit/8-bit quantization (`bitsandbytes`) where necessary to save memory.
