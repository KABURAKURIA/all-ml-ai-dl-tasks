import gradio as gr
from transformers import pipeline

# Model
pipe = pipeline("text-to-audio", model="facebook/musicgen-small")


def process_input(text):
    if not text:
        return None
    try:
        # MusicGen
        result = pipe(text, forward_params={"max_new_tokens": 256})
        if isinstance(result, list):
            result = result[0]

        # Gradio expects (sample_rate, audio_array)
        # result['audio'] is likely (channels, samples) or (samples,)
        # If it's (1, samples), we might want to flatten it or transpose
        audio = result["audio"]
        if audio.ndim > 1 and audio.shape[0] < audio.shape[1]:
             audio = audio.T # Transpose to (samples, channels)

        return (result["sampling_rate"], audio)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Interface
with gr.Blocks() as app:
    with gr.Row():
        gr.Markdown(f"# Gaze\n**Field:** Sound Therapy\n\nGenerate ambient music and binaural beats for meditation and brainwave entrainment.")

    with gr.Row():
        inp = gr.Textbox(label='Music Prompt', lines=2)
        out = gr.Audio(label='Generated Audio')

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
