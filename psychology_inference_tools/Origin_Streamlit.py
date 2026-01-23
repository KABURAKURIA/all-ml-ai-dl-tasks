import streamlit as st
from transformers import pipeline

# Configuration
st.set_page_config(page_title="Origin", layout="centered")

# Style: Neobrutalistic
st.markdown("""
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
""", unsafe_allow_html=True)

# Application Header
st.markdown('<div class="neo-container"><h1>Origin</h1><p><b>Field:</b> Neuropsychology</p><p>Answer specific questions about brain functions and neurological phenomena based on context.</p></div>', unsafe_allow_html=True)

# Model Pipeline
@st.cache_resource
def load_model():
    return pipeline("question-answering", model="deepset/roberta-base-squad2")

pipe = load_model()

# User Input
with st.container():
    st.markdown('<div class="neo-container">', unsafe_allow_html=True)

    context = st.text_area("Enter Context (e.g., a patient note or article):", height=150)
    question = st.text_input("Enter Question:")
    user_input = context and question # simple check


    if st.button("Run Origin"):
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
st.markdown(f"*Origin - A tool for Neuropsychology*")
