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
        gr.Markdown(f"# Wisp\n**Field:** Sound Therapy\n\nGenerate ambient music and binaural beats for meditation and brainwave entrainment.")

    with gr.Row():
        inp = gr.Textbox(label='Music Prompt', lines=2)
        out = gr.Audio(label='Generated Audio')

    btn = gr.Button("Run Wisp")
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
