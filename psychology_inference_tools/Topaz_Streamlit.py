import streamlit as st
from transformers import pipeline

# Configuration
st.set_page_config(page_title="Topaz", layout="centered")

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
st.markdown('<div class="neo-container"><h1>Topaz</h1><p><b>Field:</b> Sports Psychology</p><p>Generate visualization scripts, motivational speeches, or focus techniques for athletes.</p></div>', unsafe_allow_html=True)

# Model Pipeline
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="google/flan-t5-large")

pipe = load_model()

# User Input
with st.container():
    st.markdown('<div class="neo-container">', unsafe_allow_html=True)
    user_input = st.text_area("Enter text for analysis/generation:", height=150)

    if st.button("Run Topaz"):
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
st.markdown(f"*Topaz - A tool for Sports Psychology*")
