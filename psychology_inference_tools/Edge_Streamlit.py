import streamlit as st
from transformers import pipeline

# Configuration
st.set_page_config(page_title="Edge", layout="centered")

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
st.markdown('<div class="glass-container"><h1>Edge</h1><p><b>Field:</b> Neuropsychology</p><p>Answer specific questions about brain functions and neurological phenomena based on context.</p></div>', unsafe_allow_html=True)

# Model Pipeline
@st.cache_resource
def load_model():
    return pipeline("question-answering", model="deepset/roberta-base-squad2")

pipe = load_model()

# User Input
with st.container():
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)

    context = st.text_area("Enter Context (e.g., a patient note or article):", height=150)
    question = st.text_input("Enter Question:")
    user_input = context and question # simple check


    if st.button("Run Edge"):
        if user_input:
            with st.spinner("Processing..."):
                try:

                    if context and question:
                        result = pipe(question=question, context=context)
                        output = f"**Answer:** {result['answer']}\n\n*Score:* {result['score']:.4f}"
                    else:
                        st.warning("Please enter both context and question.")
                        output = None


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
st.markdown(f"*Edge - A tool for Neuropsychology*")
