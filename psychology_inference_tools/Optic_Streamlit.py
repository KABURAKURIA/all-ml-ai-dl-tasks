import streamlit as st
from transformers import pipeline

# Configuration
st.set_page_config(page_title="Optic", layout="centered")

# Style: Neobrutalistic
st.markdown("""
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
""", unsafe_allow_html=True)

# Application Header
st.markdown('<div class="neo-container"><h1>Optic</h1><p><b>Field:</b> Cross-Cultural Psychology</p><p>Translate psychological concepts across languages (Simulated).</p></div>', unsafe_allow_html=True)

# Model Pipeline
@st.cache_resource
def load_model():
    return pipeline("translation_en_to_fr", model="t5-small")

pipe = load_model()

# User Input
with st.container():
    st.markdown('<div class="neo-container">', unsafe_allow_html=True)
    user_input = st.text_area("Enter text for analysis/generation:", height=150)

    if st.button("Run Optic"):
        if user_input:
            with st.spinner("Processing..."):
                try:
                    # Adjust parameters based on task for better results
                    if "translation_en_to_fr" == "text-generation":
                        result = pipe(user_input, max_length=150, num_return_sequences=1)
                        output = result[0]['generated_text']
                    elif "translation_en_to_fr" == "zero-shot-classification":
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
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter some text.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(f"*Optic - A tool for Cross-Cultural Psychology*")
