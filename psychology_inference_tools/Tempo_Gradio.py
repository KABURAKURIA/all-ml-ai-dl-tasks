import gradio as gr
from transformers import pipeline

# Model
pipe = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def process_input(text):
    if not text:
        return "Please enter text."
    try:
        if "sentiment-analysis" == "text-generation":
            result = pipe(text, max_length=150, num_return_sequences=1)
            return result[0]['generated_text']
        elif "sentiment-analysis" == "zero-shot-classification":
            labels = ["positive", "negative", "neutral", "urgent", "informational"]
            result = pipe(text, candidate_labels=labels)
            return str(result)
        else:
            return str(pipe(text))
    except Exception as e:
        return f"Error: {e}"

# Interface
with gr.Blocks(theme=gr.themes.Glass(), css="""
        .gradio-container { background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 20px; }
        """) as app:
    with gr.Row():
        gr.Markdown(f"# Tempo\n**Field:** Consumer Psychology\n\nAnalyze consumer sentiment and reaction to products.")

    with gr.Row():
        inp = gr.Textbox(lines=5, label="Input Text", placeholder="Enter your text here...")
        out = gr.Textbox(lines=5, label="Output", interactive=False)

    btn = gr.Button("Run Tempo")
    btn.click(fn=process_input, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch()
