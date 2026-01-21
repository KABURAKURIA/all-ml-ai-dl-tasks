import gradio as gr
from transformers import pipeline

# Model
pipe = pipeline("question-answering", model="deepset/roberta-base-squad2")


def process_input(context, question):
    if not context or not question:
        return "Please enter both context and question."
    try:
        result = pipe(question=question, context=context)
        return f"Answer: {result['answer']}\nScore: {result['score']:.4f}"
    except Exception as e:
        return f"Error: {e}"


# Interface
with gr.Blocks() as app:
    with gr.Row():
        gr.Markdown(f"# Ember\n**Field:** Neuropsychology\n\nAnswer specific questions about brain functions and neurological phenomena based on context.")

    with gr.Row():
        inp = [gr.Textbox(label='Context', lines=5), gr.Textbox(label='Question')]
        out = gr.Textbox(lines=5, label="Output", interactive=False)

    btn = gr.Button("Run Ember")
    btn.click(fn=process_input, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch(theme=gr.themes.Glass(), css="""
        .gradio-container { background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 20px; }
        button { background: rgba(255, 255, 255, 0.3) !important; backdrop-filter: blur(5px); border: 1px solid rgba(255, 255, 255, 0.5) !important; color: white !important; }
        label, span, p, h1 { color: white !important; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); }
        .prose { color: white !important; }
        input, textarea { background: rgba(255, 255, 255, 0.1) !important; color: white !important; border: 1px solid rgba(255, 255, 255, 0.3) !important; }
        """)
