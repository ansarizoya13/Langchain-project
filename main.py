import streamlit as st
import cohere  # Replace with your chosen API, e.g., cohere or another service

# Initialize the language model client with your API key
cohere_client = cohere.Client('xkC6EI5tnyTj6ABzdaPGS2Lv31CuVWgAjnWlFfQC')   # For OpenAI, replace with your actual API key

def generate_code(language, task):
    prompt = f"Generate a simple {language} code to {task}."
    response = cohere_client.generate(
        model='command-xlarge-nightly',  # Example model
        prompt=prompt,
        max_tokens=150,
        temperature=0.5
    )
    return response.generations[0].text.strip()

def debug_code(code):
    prompt = f"The following code has an issue. Provide debugging suggestions:\n{code}"
    response = cohere_client.generate(
        model='command-xlarge-nightly',  # Example model
        prompt=prompt,
        max_tokens=150,
        temperature=0.5
    )
    return response.generations[0].text.strip()

# Streamlit interface
st.title('Code Generator and Debugger')

st.subheader('Generate Code')
language = st.selectbox("Select programming language", ["Python", "JavaScript", "C++", "Java"])
task = st.text_input("Enter the task description")

if st.button('Generate Code'):
    code = generate_code(language, task)
    st.text_area("Generated Code", value=code, height=200)

st.subheader('Debug Code')
code_to_debug = st.text_area("Enter the code to debug")

if st.button('Debug Code'):
    debug_suggestions = debug_code(code_to_debug)
    st.text_area("Debugging Suggestions", value=debug_suggestions, height=200)