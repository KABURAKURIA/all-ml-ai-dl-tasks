import streamlit as st
from transformers import pipeline

# Configuration
st.set_page_config(page_title="Zest", layout="centered")

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
st.markdown('<div class="neo-container"><h1>Zest</h1><p><b>Field:</b> Sound Therapy</p><p>Generate ambient music and binaural beats for meditation and brainwave entrainment.</p></div>', unsafe_allow_html=True)

# Model Pipeline
@st.cache_resource
def load_model():
    return pipeline("text-to-audio", model="facebook/musicgen-small")

pipe = load_model()

# User Input
with st.container():
    st.markdown('<div class="neo-container">', unsafe_allow_html=True)
    user_input = st.text_area("Enter text for analysis/generation:", height=150)

    if st.button("Run Zest"):
        if user_input:
            with st.spinner("Processing..."):
                try:

                    # MusicGen expects max_new_tokens for duration
                    result = pipe(user_input, forward_params={"max_new_tokens": 256})
                    if isinstance(result, list):
                        result = result[0]

                    audio_data = result["audio"]
                    # Fix: Streamlit expects (samples, channels) or (samples,)
                    # Pipeline output is often (channels, samples) e.g. (1, N)
                    if audio_data.ndim > 1 and audio_data.shape[0] < audio_data.shape[1]:
                        audio_data = audio_data.T

                    sample_rate = result["sampling_rate"]

                    st.audio(audio_data, sample_rate=sample_rate)
                    output = "Audio generated successfully."


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
st.markdown(f"*Zest - A tool for Sound Therapy*")
