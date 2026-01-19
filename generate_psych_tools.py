import os
import random
import shutil

random.seed(42)

TOOLS_DIR = "psychology_inference_tools"

# Clear existing tools
if os.path.exists(TOOLS_DIR):
    shutil.rmtree(TOOLS_DIR)
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
    "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu",
    "Arcane", "Brave", "Crisp", "Drive", "Elan", "Fable", "Grace", "Hope", "Icon", "Joy",
    "Keen", "Lucid", "Muse", "Neon", "Pure", "Quiet", "Rave", "Soul", "True", "Wild",
    "Yore", "Zest", "Amber", "Coral", "Dusk", "Fern", "Glint", "Hush", "Ivory", "Jade",
    "Knack", "Lark", "Moss", "Opal", "Pearl", "Quartz", "Ruby", "Teal", "Umbra", "Vale",
    "Wisp", "Onyx", "Azure", "Cyan", "Lime", "Rose", "Violet", "Indigo", "Topaz", "Garnet"
]

# (Field, Task, Model, Description)
domains = [
    ("Clinical Psychology", "text-generation", "google/flan-t5-large", "Simulate therapeutic responses or generate coping strategies based on cognitive behavioral therapy principles."),
    ("Cognitive Psychology", "summarization", "facebook/bart-large-cnn", "Summarize complex psychological texts or patient notes to aid in memory retention and comprehension."),
    ("Social Psychology (Sentiment)", "text-classification", "cardiffnlp/twitter-roberta-base-sentiment-latest", "Analyze the social tone and emotional valence (positive/negative/neutral) in social media text or dialogue."),
    ("Social Psychology (Emotion)", "text-classification", "j-hartmann/emotion-english-distilroberta-base", "Detect specific emotions (anger, disgust, fear, joy, neutral, sadness, surprise) in social interactions."),
    ("Industrial-Organizational Psychology", "text-generation", "gpt2", "Generate professional feedback, leadership scenarios, or workplace conflict resolution scripts."),
    ("Developmental Psychology", "text-generation", "google/flan-t5-large", "Provide descriptions of developmental milestones or parenting advice for specific age groups."),
    ("Forensic Psychology", "zero-shot-classification", "facebook/bart-large-mnli", "Classify statements for potential risk markers (e.g., deception, aggression, distress)."),
    ("Health Psychology", "text-generation", "gpt2", "Generate relaxation scripts, mindfulness prompts, or health behavior nudges."),
    ("Educational Psychology", "text2text-generation", "google/flan-t5-small", "Simplify complex psychological concepts into easy-to-understand language for students."),
    ("Neuropsychology", "question-answering", "deepset/roberta-base-squad2", "Answer specific questions about brain functions and neurological phenomena based on context."),
    ("Evolutionary Psychology", "text-generation", "gpt2", "Generate hypotheses about the evolutionary origins of specific human behaviors."),
    ("Consumer Psychology", "text-classification", "cardiffnlp/twitter-roberta-base-sentiment-latest", "Analyze consumer reviews to determine sentiment towards products or services."),
    ("Environmental Psychology", "text-generation", "gpt2", "Describe the potential psychological impact of different environmental settings on well-being."),
    ("Sports Psychology", "text-generation", "google/flan-t5-large", "Generate visualization scripts, motivational speeches, or focus techniques for athletes."),
    ("Positive Psychology", "text-generation", "gpt2", "Generate gratitude prompts, positive affirmations, or strengths-based interventions."),
    ("Psychometrics", "zero-shot-classification", "facebook/bart-large-mnli", "Categorize personality descriptions into Big Five traits (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism)."),
    ("Biopsychology", "text-generation", "gpt2", "Explain the biological and hormonal underpinnings of specific emotional states."),
    ("Cross-Cultural Psychology", "translation_en_to_fr", "Helsinki-NLP/opus-mt-en-fr", "Translate psychological survey items or concepts to ensure cross-cultural validity (English to French)."),
    ("Comparative Psychology", "text-generation", "gpt2", "Compare specific behaviors between humans and other animal species."),
    ("Rehabilitation Psychology", "text-generation", "google/flan-t5-large", "Create personalized recovery plans and motivational support messages for rehabilitation patients."),
    ("Family Psychology", "text-generation", "gpt2", "Generate scripts for addressing family dynamics and conflict resolution using systemic approaches."),
    ("Crisis Intervention", "text-classification", "j-hartmann/emotion-english-distilroberta-base", "Rapidly identify the dominant emotion in a crisis text to inform immediate response."),
    ("Sleep Psychology", "text-generation", "gpt2", "Generate sleep hygiene tips and bedtime routines based on user descriptions of sleep issues."),
    ("Media Psychology", "zero-shot-classification", "facebook/bart-large-mnli", "Analyze media content for themes like violence, prosocial behavior, or consumerism."),
    ("Geropsychology", "text-generation", "google/flan-t5-large", "Generate cognitive exercises or reminiscence therapy prompts for older adults."),
    ("Cyberpsychology", "text-classification", "cardiffnlp/twitter-roberta-base-sentiment-latest", "Analyze online interactions for toxic sentiment or cyberbullying indicators.")
]

streamlit_glass_css = """
<style>
.stApp {
    background-image: linear-gradient(to right top, #d16ba5, #c777b9, #ba83ca, #aa8fd8, #9a9ae1, #8aa7ec, #79b3f4, #69bff8, #52cffe, #41dfff, #46eefa, #5ffbf1);
    background-attachment: fixed;
    background-size: cover;
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
    transition: all 0.3s ease;
}
.stButton > button:hover {
    background: rgba(255, 255, 255, 0.5);
    transform: scale(1.05);
}
h1, h2, h3, p, label, .stMarkdown {
    color: white !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.glass-container {
    background: rgba(255, 255, 255, 0.25);
    border-radius: 16px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.4);
    padding: 25px;
    margin-bottom: 25px;
}
</style>
"""

streamlit_neobrutal_css = """
<style>
.stApp {
    background-color: #FFDEE9;
    background-image: linear-gradient(0deg, #FFDEE9 0%, #B5FFFC 100%);
    background-attachment: fixed;
}
.stTextInput > div > div > input, .stTextArea > div > div > textarea {
    background-color: #fff;
    border: 3px solid black;
    box-shadow: 5px 5px 0px 0px #000000;
    border-radius: 0px;
    color: black;
    font-family: 'Courier New', Courier, monospace;
    font-weight: bold;
}
.stButton > button {
    background-color: #FF9A8B;
    border: 3px solid black;
    box-shadow: 5px 5px 0px 0px #000000;
    color: black;
    font-weight: 900;
    border-radius: 0px;
    text-transform: uppercase;
    font-family: 'Courier New', Courier, monospace;
    transition: all 0.1s;
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
    margin-bottom: 20px;
}
.neo-container {
    background-color: #8BC6EC;
    border: 3px solid black;
    box-shadow: 8px 8px 0px 0px #000000;
    padding: 20px;
    margin-bottom: 20px;
    font-family: 'Courier New', Courier, monospace;
}
p, label, .stMarkdown {
    color: black;
    font-family: 'Courier New', Courier, monospace;
    font-weight: 600;
}
</style>
"""

def generate_streamlit_code(name, field, task, model, description, style_css, style_name):
    # Logic to handle specific inputs based on task
    input_section = 'user_input = st.text_area("Enter text for analysis/generation:", height=150)'
    run_logic = ""

    if task == "question-answering":
        input_section = """
    context = st.text_area("Enter Context (e.g., a patient note or article):", height=150)
    question = st.text_input("Enter Question:")
    user_input = context and question # simple check
        """
        run_logic = f"""
                    if context and question:
                        result = pipe(question=question, context=context)
                        output = f"**Answer:** {{result['answer']}}\\n\\n*Score:* {{result['score']:.4f}}"
                    else:
                        st.warning("Please enter both context and question.")
                        output = None
        """
    elif task == "text-classification":
         run_logic = f"""
                    result = pipe(user_input)
                    # Handle list of lists or single list
                    if isinstance(result, list) and isinstance(result[0], list):
                        result = result[0]

                    # Sort by score if multiple
                    result = sorted(result, key=lambda x: x['score'], reverse=True)

                    output = "### Predictions:\\n"
                    for res in result:
                        label = res['label']
                        score = res['score']
                        output += f"- **{{label}}**: {{score:.4f}}\\n"
         """
    elif task == "zero-shot-classification":
         run_logic = f"""
                    labels = ["risk", "safety", "neutral", "positive", "negative"] # Default labels, could be customized
                    result = pipe(user_input, candidate_labels=labels)

                    output = "### Predictions:\\n"
                    for label, score in zip(result['labels'], result['scores']):
                        output += f"- **{{label}}**: {{score:.4f}}\\n"
         """
    elif task == "translation_en_to_fr":
         run_logic = f"""
                    result = pipe(user_input)
                    output = result[0]['translation_text']
         """
    elif "text-generation" in task or "text2text" in task:
         run_logic = f"""
                    result = pipe(user_input, max_length=200, num_return_sequences=1)
                    if isinstance(result, list):
                        if 'generated_text' in result[0]:
                            output = result[0]['generated_text']
                        elif 'summary_text' in result[0]:
                            output = result[0]['summary_text']
                        else:
                            output = str(result[0])
                    else:
                        output = str(result)
         """
    elif task == "summarization":
         run_logic = f"""
                    result = pipe(user_input, max_length=150, min_length=30, do_sample=False)
                    output = result[0]['summary_text']
         """
    else:
         run_logic = f"""
                    result = pipe(user_input)
                    output = str(result)
         """

    if output_var_assign := "output = None" not in run_logic:
        pass # placeholder

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
    {input_section}

    if st.button("Run {name}"):
        if user_input:
            with st.spinner("Processing..."):
                try:
                    {run_logic}

                    if output:
                        st.success("Completed!")
                        st.markdown("### Result:")
                        st.write(output)
                except Exception as e:
                    st.error(f"Error: {{e}}")
        else:
            st.warning("Please provide the required input.")
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
        theme = "gr.themes.Soft(primary_hue='red', secondary_hue='pink', neutral_hue='slate', font=['Courier New', 'monospace'])"

    css = ""
    if style_type == "Neobrutalistic":
        css = """
        body { background-color: #FFDEE9; background-image: linear-gradient(0deg, #FFDEE9 0%, #B5FFFC 100%); }
        .gradio-container { border: 3px solid black !important; box-shadow: 8px 8px 0px 0px #000000 !important; background-color: white !important; }
        button { border: 2px solid black !important; box-shadow: 4px 4px 0px 0px #000000 !important; border-radius: 0 !important; font-weight: bold !important; background-color: #FF9A8B !important; color: black !important; }
        button:hover { transform: translate(2px, 2px); box-shadow: 2px 2px 0px 0px #000000 !important; }
        input, textarea, .gr-input { border: 2px solid black !important; border-radius: 0 !important; font-family: 'Courier New', monospace !important; }
        label { font-weight: bold !important; color: black !important; }
        h1, h2, p { font-family: 'Courier New', monospace !important; color: black !important; }
        .prose { font-family: 'Courier New', monospace !important; }
        """
    elif style_type == "Glassmorphic":
        css = """
        .gradio-container { background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 20px; }
        button { background: rgba(255, 255, 255, 0.3) !important; backdrop-filter: blur(5px); border: 1px solid rgba(255, 255, 255, 0.5) !important; color: white !important; }
        label, span, p, h1 { color: white !important; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); }
        .prose { color: white !important; }
        input, textarea { background: rgba(255, 255, 255, 0.1) !important; color: white !important; border: 1px solid rgba(255, 255, 255, 0.3) !important; }
        """

    # Processing logic
    process_func = ""
    inputs = ""

    if task == "question-answering":
        inputs = "[gr.Textbox(label='Context', lines=5), gr.Textbox(label='Question')]"
        process_func = f"""
def process_input(context, question):
    if not context or not question:
        return "Please enter both context and question."
    try:
        result = pipe(question=question, context=context)
        return f"Answer: {{result['answer']}}\\nScore: {{result['score']:.4f}}"
    except Exception as e:
        return f"Error: {{e}}"
        """
    elif task == "zero-shot-classification":
        inputs = "gr.Textbox(label='Input Text', lines=5)"
        process_func = f"""
def process_input(text):
    if not text:
        return "Please enter text."
    try:
        labels = ["risk", "safety", "neutral", "positive", "negative"]
        result = pipe(text, candidate_labels=labels)
        output = "Predictions:\\n"
        for label, score in zip(result['labels'], result['scores']):
            output += f"- {{label}}: {{score:.4f}}\\n"
        return output
    except Exception as e:
        return f"Error: {{e}}"
        """
    elif task == "text-classification":
         inputs = "gr.Textbox(label='Input Text', lines=5)"
         process_func = f"""
def process_input(text):
    if not text:
        return "Please enter text."
    try:
        result = pipe(text)
        if isinstance(result, list) and isinstance(result[0], list):
             result = result[0]
        # Sort
        result = sorted(result, key=lambda x: x['score'], reverse=True)
        output = "Predictions:\\n"
        for res in result:
             output += f"- {{res['label']}}: {{res['score']:.4f}}\\n"
        return output
    except Exception as e:
        return f"Error: {{e}}"
         """
    else: # generation, summarization, translation
        inputs = "gr.Textbox(label='Input Text', lines=5)"
        process_func = f"""
def process_input(text):
    if not text:
        return "Please enter text."
    try:
        if "{task}" == "summarization":
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
        return f"Error: {{e}}"
        """

    code = f"""import gradio as gr
from transformers import pipeline

# Model
pipe = pipeline("{task}", model="{model}")

{process_func}

# Interface
with gr.Blocks() as app:
    with gr.Row():
        gr.Markdown(f"# {name}\\n**Field:** {field}\\n\\n{description}")

    with gr.Row():
        inp = {inputs}
        out = gr.Textbox(lines=5, label="Output", interactive=False)

    btn = gr.Button("Run {name}")
    btn.click(fn=process_input, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch(theme={theme}, css=\"\"\"{css}\"\"\")
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
    if count >= 110: # Generate a few extra to be safe
        break

print(f"Generated {count} tools in {TOOLS_DIR}")
