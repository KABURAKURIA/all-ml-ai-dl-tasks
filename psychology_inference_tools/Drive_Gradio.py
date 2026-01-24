import gradio as gr
from transformers import pipeline

# Model
pipe = pipeline("text-generation", model="gpt2")


def process_input(text):
    if not text:
        return "Please enter text."
    try:
        if "text-generation" == "summarization":
             result = pipe(text, max_length=150, min_length=30, do_sample=False)
        else:
             result = pipe(text, max_length=200, num_return_sequences=1)

        if isinstance(result, list):
            if 'generated_text' in result[0]:
                return result[0]['generated_text']
            elif 'summary_text' in result[0]:
                return result[0]['summary_text']
            elif 'translation_text' in result[0]:
                return result[0]['translation_text']
            else:
                return str(result[0])
        else:
            return str(result)
    except Exception as e:
        return f"Error: {e}"


# Interface
with gr.Blocks() as app:
    with gr.Row():
        gr.Markdown(f"# Drive\n**Field:** Sleep Psychology\n\nGenerate sleep hygiene tips and bedtime routines based on user descriptions of sleep issues.")

    with gr.Row():
        inp = gr.Textbox(label='Input Text', lines=5)
        out = gr.Textbox(lines=5, label='Output', interactive=False)

    btn = gr.Button("Run Drive")
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
