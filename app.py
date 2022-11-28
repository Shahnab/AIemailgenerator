import streamlit as st
import openai
from ml_backend import ml_backend

# st.image("https://cdn-icons-png.flaticon.com/512/194/194300.png", width=100)
st.image("icons.jpg", width=100)
st.title("A.I. Based Email Generator Engine")
st.sidebar.header("About the App:")
st.sidebar.caption("This app is build using GPT3")
st.sidebar.markdown("GPT-3 (Generative Pre-trained Transformer 3) is one of the most popular language models")
st.sidebar.markdown("GPT-3 is an autoregressive language model that uses deep learning to produce human-like text")
st.sidebar.markdown("GPT-3 is trained on over 175 billion parameters on 45 TB of text sourced from all over the internet")

st.sidebar.header("About the GPT3 Engine:")
st.sidebar.markdown("Davinci is the most capable model and can do anything that any other model can do, and much more—often with fewer instructions")
st.sidebar.markdown("Davinci is able to solve logic problems, determine cause and effect, understand the intent of text, produce creative content, explain character motives, and handle complex summarization tasks")


st.sidebar.header("Powered by")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/OpenAI_Logo.svg/1280px-OpenAI_Logo.svg.png", width=150)


st.markdown("### Email Generator")

backend = ml_backend()

with st.form(key="form"):
    prompt = st.text_input("Describe the kind of Email you want to be generated.")
    st.text(f"(E.g: Write a professional email to my boss asking for leave of absence)")

    start = st.text_input("Begin writing the first few or several words of your email:")

    slider = st.slider("How many characters do you want your email to be? ", min_value=64, max_value=750)
    st.text("(A typical email is usually 100-500 characters)")

    submit_button = st.form_submit_button(label='Generate Email')

    if submit_button:
        with st.spinner("Generating Email..."):
            output = backend.generate_email(prompt, start)
        st.markdown("# Email Output:")
        st.subheader(start + output)
