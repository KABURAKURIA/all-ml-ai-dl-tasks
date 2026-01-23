import gradio as gr
from transformers import pipeline

# Model
pipe = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")


def process_input(text):
    if not text:
        return "Please enter text."
    try:
        result = pipe(text, top_k=5)
        if isinstance(result, list) and isinstance(result[0], list):
             result = result[0]
        # Sort
        result = sorted(result, key=lambda x: x['score'], reverse=True)
        output = "Predictions:\n"
        for res in result:
             output += f"- {res['label']}: {res['score']:.4f}\n"
        return output
    except Exception as e:
        return f"Error: {e}"


# Interface
with gr.Blocks() as app:
    with gr.Row():
        gr.Markdown(f"# Gaze\n**Field:** Social Psychology (Emotion)\n\nDetect specific emotions (anger, disgust, fear, joy, neutral, sadness, surprise) in social interactions.")

    with gr.Row():
        inp = gr.Textbox(label='Input Text', lines=5)
        out = gr.Textbox(lines=5, label="Output", interactive=False)

    btn = gr.Button("Run Gaze")
    btn.click(fn=process_input, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch(theme=gr.themes.Glass(), css="""
        .gradio-container { background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 20px; }
        button { background: rgba(255, 255, 255, 0.3) !important; backdrop-filter: blur(5px); border: 1px solid rgba(255, 255, 255, 0.5) !important; color: white !important; }
        label, span, p, h1 { color: white !important; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); }
        .prose { color: white !important; }
        input, textarea { background: rgba(255, 255, 255, 0.1) !important; color: white !important; border: 1px solid rgba(255, 255, 255, 0.3) !important; }
        """)
