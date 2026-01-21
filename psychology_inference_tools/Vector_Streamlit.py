import streamlit as st
from transformers import pipeline

# Configuration
st.set_page_config(page_title="Vector", layout="centered")

# Style: Glassmorphic
st.markdown("""
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
""", unsafe_allow_html=True)

# Application Header
st.markdown('<div class="glass-container"><h1>Vector</h1><p><b>Field:</b> Forensic Psychology</p><p>Classify statements for potential risk markers (e.g., deception, aggression, distress).</p></div>', unsafe_allow_html=True)

# Model Pipeline
@st.cache_resource
def load_model():
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

pipe = load_model()

# User Input
with st.container():
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    user_input = st.text_area("Enter text for analysis/generation:", height=150)

    if st.button("Run Vector"):
        if user_input:
            with st.spinner("Processing..."):
                try:

                    labels = ["risk", "safety", "neutral", "positive", "negative"] # Default labels, could be customized
                    result = pipe(user_input, candidate_labels=labels)

                    output = "### Predictions:\n"
                    for label, score in zip(result['labels'], result['scores']):
                        output += f"- **{label}**: {score:.4f}\n"


                    if output:
                        st.success("Completed!")
                        st.markdown("### Result:")
                        st.write(output)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please provide the required input.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(f"*Vector - A tool for Forensic Psychology*")
