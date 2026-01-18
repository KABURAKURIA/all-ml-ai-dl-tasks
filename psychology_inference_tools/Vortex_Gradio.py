import gradio as gr
from transformers import pipeline

# Model
pipe = pipeline("translation_en_to_fr", model="t5-small")

def process_input(text):
    if not text:
        return "Please enter text."
    try:
        if "translation_en_to_fr" == "text-generation":
            result = pipe(text, max_length=150, num_return_sequences=1)
            return result[0]['generated_text']
        elif "translation_en_to_fr" == "zero-shot-classification":
            labels = ["positive", "negative", "neutral", "urgent", "informational"]
            result = pipe(text, candidate_labels=labels)
            return str(result)
        else:
            return str(pipe(text))
    except Exception as e:
        return f"Error: {e}"

# Interface
with gr.Blocks() as app:
    with gr.Row():
        gr.Markdown(f"# Vortex\n**Field:** Cross-Cultural Psychology\n\nTranslate psychological concepts across languages (Simulated).")

    with gr.Row():
        inp = gr.Textbox(lines=5, label="Input Text", placeholder="Enter your text here...")
        out = gr.Textbox(lines=5, label="Output", interactive=False)

    btn = gr.Button("Run Vortex")
    btn.click(fn=process_input, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch(theme=gr.themes.Glass(), css="""
        .gradio-container { background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 20px; }
        """)
