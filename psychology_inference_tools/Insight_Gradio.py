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
        gr.Markdown(f"# Insight\n**Field:** Environmental Psychology\n\nDescribe the potential psychological impact of different environmental settings on well-being.")

    with gr.Row():
        inp = gr.Textbox(label='Input Text', lines=5)
        out = gr.Textbox(lines=5, label="Output", interactive=False)

    btn = gr.Button("Run Insight")
    btn.click(fn=process_input, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch(theme=gr.themes.Glass(), css="""
        .gradio-container { background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 20px; }
        button { background: rgba(255, 255, 255, 0.3) !important; backdrop-filter: blur(5px); border: 1px solid rgba(255, 255, 255, 0.5) !important; color: white !important; }
        label, span, p, h1 { color: white !important; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); }
        .prose { color: white !important; }
        input, textarea { background: rgba(255, 255, 255, 0.1) !important; color: white !important; border: 1px solid rgba(255, 255, 255, 0.3) !important; }
        """)
