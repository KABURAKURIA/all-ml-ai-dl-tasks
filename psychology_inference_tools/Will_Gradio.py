import gradio as gr
from transformers import pipeline

# Model
pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")


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
        gr.Markdown(f"# Will\n**Field:** Consumer Psychology\n\nAnalyze consumer reviews to determine sentiment towards products or services.")

    with gr.Row():
        inp = gr.Textbox(label='Input Text', lines=5)
        out = gr.Textbox(lines=5, label='Output', interactive=False)

    btn = gr.Button("Run Will")
    btn.click(fn=process_input, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch(theme=gr.themes.Soft(primary_hue='red', secondary_hue='pink', neutral_hue='slate', font=['Courier New', 'monospace']), css="""
        body { background-color: #FFDEE9; background-image: linear-gradient(0deg, #FFDEE9 0%, #B5FFFC 100%); }
        .gradio-container { border: 3px solid black !important; box-shadow: 8px 8px 0px 0px #000000 !important; background-color: white !important; }
        button { border: 2px solid black !important; box-shadow: 4px 4px 0px 0px #000000 !important; border-radius: 0 !important; font-weight: bold !important; background-color: #FF9A8B !important; color: black !important; }
        button:hover { transform: translate(2px, 2px); box-shadow: 2px 2px 0px 0px #000000 !important; }
        input, textarea, .gr-input { border: 2px solid black !important; border-radius: 0 !important; font-family: 'Courier New', monospace !important; }
        label { font-weight: bold !important; color: black !important; }
        h1, h2, p { font-family: 'Courier New', monospace !important; color: black !important; }
        .prose { font-family: 'Courier New', monospace !important; }
        """)
