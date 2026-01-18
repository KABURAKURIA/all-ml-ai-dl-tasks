import gradio as gr
from transformers import pipeline

# Model
pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def process_input(text):
    if not text:
        return "Please enter text."
    try:
        if "zero-shot-classification" == "text-generation":
            result = pipe(text, max_length=150, num_return_sequences=1)
            return result[0]['generated_text']
        elif "zero-shot-classification" == "zero-shot-classification":
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
        gr.Markdown(f"# Transcend\n**Field:** Psychometrics\n\nCategorize personality traits from descriptions.")

    with gr.Row():
        inp = gr.Textbox(lines=5, label="Input Text", placeholder="Enter your text here...")
        out = gr.Textbox(lines=5, label="Output", interactive=False)

    btn = gr.Button("Run Transcend")
    btn.click(fn=process_input, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch(theme=gr.themes.Soft(primary_hue='red', secondary_hue='pink', neutral_hue='slate', font=['Courier New', 'monospace']), css="""
        body { background-color: #FFDEE9; background-image: linear-gradient(0deg, #FFDEE9 0%, #B5FFFC 100%); }
        .gradio-container { border: 3px solid black; box-shadow: 8px 8px 0px 0px #000000; background-color: white; }
        button { border: 2px solid black !important; box-shadow: 4px 4px 0px 0px #000000 !important; border-radius: 0 !important; font-weight: bold !important; }
        input, textarea { border: 2px solid black !important; border-radius: 0 !important; }
        """)
