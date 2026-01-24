import gradio as gr
from transformers import pipeline

# Model
pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")


def process_input(text):
    if not text:
        return "Please enter text."
    try:
        labels = ["risk", "safety", "neutral", "positive", "negative"]
        result = pipe(text, candidate_labels=labels)
        output = "Predictions:\n"
        for label, score in zip(result['labels'], result['scores']):
            output += f"- {label}: {score:.4f}\n"
        return output
    except Exception as e:
        return f"Error: {e}"


# Interface
with gr.Blocks() as app:
    with gr.Row():
        gr.Markdown(f"# Pure\n**Field:** Media Psychology\n\nAnalyze media content for themes like violence, prosocial behavior, or consumerism.")

    with gr.Row():
        inp = gr.Textbox(label='Input Text', lines=5)
        out = gr.Textbox(lines=5, label='Output', interactive=False)

    btn = gr.Button("Run Pure")
    btn.click(fn=process_input, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch(theme=gr.themes.Glass(), css="""
        .gradio-container { background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 20px; }
        button { background: rgba(255, 255, 255, 0.3) !important; backdrop-filter: blur(5px); border: 1px solid rgba(255, 255, 255, 0.5) !important; color: white !important; }
        label, span, p, h1 { color: white !important; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); }
        .prose { color: white !important; }
        input, textarea { background: rgba(255, 255, 255, 0.1) !important; color: white !important; border: 1px solid rgba(255, 255, 255, 0.3) !important; }
        """)
