import os
import random

TOOLS_DIR = "psychology_inference_tools"
os.makedirs(TOOLS_DIR, exist_ok=True)

names = [
    "Aether", "Anima", "Apex", "Aura", "Axis", "Beacon", "Bloom", "Bridge", "Catalyst", "Clarity",
    "Core", "Crest", "Drift", "Echo", "Ember", "Essence", "Ethos", "Flux", "Focus", "Forge",
    "Fuse", "Gaze", "Glow", "Grit", "Grove", "Halo", "Haven", "Helm", "Horizon", "Insight",
    "Iris", "Journey", "Kairos", "Kinetic", "Lens", "Link", "Lotus", "Lumen", "Matrix", "Merge",
    "Mimesis", "Mind", "Mode", "Momentum", "Mosaic", "Motion", "Myriad", "Nexus", "Nova", "Oasis",
    "Orbit", "Origin", "Pace", "Path", "Peak", "Phase", "Pivot", "Prism", "Pulse", "Quest",
    "Radius", "Realm", "Resonance", "Rhythm", "Ripple", "Root", "Sage", "Scale", "Scope", "Sense",
    "Shift", "Signal", "Spark", "Spectrum", "Sphere", "Spire", "Spirit", "Surge", "Sync", "Synergy",
    "Synthesis", "Tact", "Tempo", "Terra", "Tide", "Trace", "Track", "Transcend", "Unity", "Valence",
    "Vector", "Velocity", "Verve", "Vision", "Vital", "Vivid", "Vortex", "Wave", "Weave", "Will", "Zenith", "Zone",
    "Optic", "Sonic", "Haptic", "Logic", "Civic", "Ethic", "Lyric", "Mythic", "Tonic", "Ionic",
    "Omen", "Oracle", "Scribe", "Vigil", "Warden", "Xenon", "Yonder", "Zephyr", "Alpha", "Beta",
    "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu"
]

domains = [
    ("Clinical Psychology", "text-generation", "gpt2", "Simulate therapeutic responses or generate coping strategies."),
    ("Cognitive Psychology", "summarization", "facebook/bart-large-cnn", "Summarize complex texts to aid memory and comprehension."),
    ("Social Psychology", "sentiment-analysis", "distilbert-base-uncased-finetuned-sst-2-english", "Analyze social tone and emotional valence in text."),
    ("Industrial-Organizational Psychology", "text-generation", "gpt2", "Generate professional feedback or workplace scenarios."),
    ("Developmental Psychology", "text-generation", "gpt2", "Provide parenting advice or developmental milestone descriptions."),
    ("Forensic Psychology", "zero-shot-classification", "facebook/bart-large-mnli", "Classify statements for potential deception or risk markers."),
    ("Health Psychology", "text-generation", "gpt2", "Generate relaxation scripts or health behavior nudges."),
    ("Educational Psychology", "text2text-generation", "t5-small", "Simplify concepts for better learning."),
    ("Neuropsychology", "text-generation", "gpt2", "Explain brain functions and neurological phenomena."),
    ("Evolutionary Psychology", "text-generation", "gpt2", "Hypothesize evolutionary reasons for behaviors."),
    ("Consumer Psychology", "sentiment-analysis", "distilbert-base-uncased-finetuned-sst-2-english", "Analyze consumer sentiment and reaction to products."),
    ("Environmental Psychology", "text-generation", "gpt2", "Describe impact of environment on well-being."),
    ("Sports Psychology", "text-generation", "gpt2", "Generate motivational speeches and focus techniques."),
    ("Positive Psychology", "text-generation", "gpt2", "Generate gratitude prompts and positive affirmations."),
    ("Psychometrics", "zero-shot-classification", "facebook/bart-large-mnli", "Categorize personality traits from descriptions."),
    ("Biopsychology", "text-generation", "gpt2", "Discuss biological underpinnings of behavior."),
    ("Cross-Cultural Psychology", "translation_en_to_fr", "t5-small", "Translate psychological concepts across languages (Simulated)."),
    ("Comparative Psychology", "text-generation", "gpt2", "Compare animal and human behaviors."),
    ("Rehabilitation Psychology", "text-generation", "gpt2", "Create recovery plans and motivational support."),
    ("Family Psychology", "text-generation", "gpt2", "Address family dynamics and conflict resolution.")
]

streamlit_glass_css = """
<style>
.stApp {
    background-image: linear-gradient(to right top, #d16ba5, #c777b9, #ba83ca, #aa8fd8, #9a9ae1, #8aa7ec, #79b3f4, #69bff8, #52cffe, #41dfff, #46eefa, #5ffbf1);
}
.stTextInput > div > div > input, .stTextArea > div > div > textarea {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.5);
    color: white;
    border-radius: 15px;
}
.stButton > button {
    background: rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.5);
    color: white;
    border-radius: 15px;
    padding: 10px 20px;
    font-weight: bold;
}
h1, h2, h3, p, label {
    color: white;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.glass-container {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 16px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 20px;
    margin-bottom: 20px;
}
</style>
"""

streamlit_neobrutal_css = """
<style>
.stApp {
    background-color: #FFDEE9;
    background-image: linear-gradient(0deg, #FFDEE9 0%, #B5FFFC 100%);
}
.stTextInput > div > div > input, .stTextArea > div > div > textarea {
    background-color: #fff;
    border: 3px solid black;
    box-shadow: 5px 5px 0px 0px #000000;
    border-radius: 0px;
    color: black;
    font-family: 'Courier New', Courier, monospace;
}
.stButton > button {
    background-color: #FF9A8B;
    border: 3px solid black;
    box-shadow: 5px 5px 0px 0px #000000;
    color: black;
    font-weight: 900;
    border-radius: 0px;
    text-transform: uppercase;
}
.stButton > button:hover {
    box-shadow: 2px 2px 0px 0px #000000;
    transform: translate(3px, 3px);
}
h1, h2, h3 {
    font-family: 'Courier New', Courier, monospace;
    font-weight: 900;
    text-transform: uppercase;
    border: 3px solid black;
    padding: 10px;
    background-color: #FBAB7E;
    box-shadow: 5px 5px 0px 0px #000000;
    color: black;
    display: inline-block;
}
.neo-container {
    background-color: #8BC6EC;
    border: 3px solid black;
    box-shadow: 8px 8px 0px 0px #000000;
    padding: 20px;
    margin-bottom: 20px;
}
</style>
"""

def generate_streamlit_code(name, field, task, model, description, style_css, style_name):
    code = f"""import streamlit as st
from transformers import pipeline

# Configuration
st.set_page_config(page_title="{name}", layout="centered")

# Style: {style_name}
st.markdown(\"\"\"{style_css}\"\"\", unsafe_allow_html=True)

# Application Header
st.markdown('<div class="{ 'glass-container' if 'Glass' in style_name else 'neo-container' }"><h1>{name}</h1><p><b>Field:</b> {field}</p><p>{description}</p></div>', unsafe_allow_html=True)

# Model Pipeline
@st.cache_resource
def load_model():
    return pipeline("{task}", model="{model}")

pipe = load_model()

# User Input
with st.container():
    st.markdown('<div class="{ 'glass-container' if 'Glass' in style_name else 'neo-container' }">', unsafe_allow_html=True)
    user_input = st.text_area("Enter text for analysis/generation:", height=150)

    if st.button("Run {name}"):
        if user_input:
            with st.spinner("Processing..."):
                try:
                    # Adjust parameters based on task for better results
                    if "{task}" == "text-generation":
                        result = pipe(user_input, max_length=150, num_return_sequences=1)
                        output = result[0]['generated_text']
                    elif "{task}" == "zero-shot-classification":
                        labels = ["positive", "negative", "neutral", "urgent", "informational"]
                        result = pipe(user_input, candidate_labels=labels)
                        output = str(result)
                    else:
                        result = pipe(user_input)
                        output = str(result)

                    st.success("Completed!")
                    st.markdown("### Result:")
                    st.write(output)
                except Exception as e:
                    st.error(f"Error: {{e}}")
        else:
            st.warning("Please enter some text.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(f"*{name} - A tool for {field}*")
"""
    return code

def generate_gradio_code(name, field, task, model, description, style_type):
    # Determine theme
    if style_type == "Glassmorphic":
        theme = "gr.themes.Glass()"
    else:
        # Custom brutalist-like theme construction or just Soft with CSS injection
        theme = "gr.themes.Soft(primary_hue='red', secondary_hue='pink', neutral_hue='slate', font=['Courier New', 'monospace'])"

    css = ""
    if style_type == "Neobrutalistic":
        css = """
        body { background-color: #FFDEE9; background-image: linear-gradient(0deg, #FFDEE9 0%, #B5FFFC 100%); }
        .gradio-container { border: 3px solid black; box-shadow: 8px 8px 0px 0px #000000; background-color: white; }
        button { border: 2px solid black !important; box-shadow: 4px 4px 0px 0px #000000 !important; border-radius: 0 !important; font-weight: bold !important; }
        input, textarea { border: 2px solid black !important; border-radius: 0 !important; }
        """
    elif style_type == "Glassmorphic":
        css = """
        .gradio-container { background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 20px; }
        """

    code = f"""import gradio as gr
from transformers import pipeline

# Model
pipe = pipeline("{task}", model="{model}")

def process_input(text):
    if not text:
        return "Please enter text."
    try:
        if "{task}" == "text-generation":
            result = pipe(text, max_length=150, num_return_sequences=1)
            return result[0]['generated_text']
        elif "{task}" == "zero-shot-classification":
            labels = ["positive", "negative", "neutral", "urgent", "informational"]
            result = pipe(text, candidate_labels=labels)
            return str(result)
        else:
            return str(pipe(text))
    except Exception as e:
        return f"Error: {{e}}"

# Interface
with gr.Blocks(theme={theme}, css=\"\"\"{css}\"\"\") as app:
    with gr.Row():
        gr.Markdown(f"# {name}\\n**Field:** {field}\\n\\n{description}")

    with gr.Row():
        inp = gr.Textbox(lines=5, label="Input Text", placeholder="Enter your text here...")
        out = gr.Textbox(lines=5, label="Output", interact=False)

    btn = gr.Button("Run {name}")
    btn.click(fn=process_input, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch()
"""
    return code

count = 0
used_names = set()

# Shuffle names to ensure random distribution
random.shuffle(names)

for i in range(len(names)):
    name = names[i]
    if name in used_names:
        continue
    used_names.add(name)

    # Pick a domain cyclically
    domain_info = domains[i % len(domains)]
    field, task, model, description = domain_info

    # Random framework and style
    framework = random.choice(["Streamlit", "Gradio"])
    style = random.choice(["Glassmorphic", "Neobrutalistic"])

    filename = f"{name}_{framework}.py"
    filepath = os.path.join(TOOLS_DIR, filename)

    if framework == "Streamlit":
        css = streamlit_glass_css if style == "Glassmorphic" else streamlit_neobrutal_css
        content = generate_streamlit_code(name, field, task, model, description, css, style)
    else:
        content = generate_gradio_code(name, field, task, model, description, style)

    with open(filepath, "w") as f:
        f.write(content)

    count += 1
    if count >= 105: # Generate a few extra
        break

print(f"Generated {count} tools in {TOOLS_DIR}")
