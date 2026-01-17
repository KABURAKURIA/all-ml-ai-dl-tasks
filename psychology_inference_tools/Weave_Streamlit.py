import streamlit as st
from transformers import pipeline

# Configuration
st.set_page_config(page_title="Weave", layout="centered")

# Style: Glassmorphic
st.markdown("""
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
""", unsafe_allow_html=True)

# Application Header
st.markdown('<div class="glass-container"><h1>Weave</h1><p><b>Field:</b> Clinical Psychology</p><p>Simulate therapeutic responses or generate coping strategies.</p></div>', unsafe_allow_html=True)

# Model Pipeline
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

pipe = load_model()

# User Input
with st.container():
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    user_input = st.text_area("Enter text for analysis/generation:", height=150)

    if st.button("Run Weave"):
        if user_input:
            with st.spinner("Processing..."):
                try:
                    # Adjust parameters based on task for better results
                    if "text-generation" == "text-generation":
                        result = pipe(user_input, max_length=150, num_return_sequences=1)
                        output = result[0]['generated_text']
                    elif "text-generation" == "zero-shot-classification":
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
st.markdown(f"*Weave - A tool for Clinical Psychology*")
