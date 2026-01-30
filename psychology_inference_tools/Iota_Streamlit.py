import streamlit as st
from transformers import pipeline

# Configuration
st.set_page_config(page_title="Iota", layout="centered")

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
st.markdown('<div class="glass-container"><h1>Iota</h1><p><b>Field:</b> Sports Psychology</p><p>Generate visualization scripts, motivational speeches, or focus techniques for athletes.</p></div>', unsafe_allow_html=True)

# Model Pipeline
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-large")

pipe = load_model()

# User Input
with st.container():
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    user_input = st.text_area("Enter text for analysis/generation:", height=150)

    if st.button("Run Iota"):
        if user_input:
            with st.spinner("Processing..."):
                try:

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
st.markdown(f"*Iota - A tool for Sports Psychology*")
