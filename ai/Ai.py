# api_key = "AIzaSyCgSIYXikg8bR7FVBaNBFraweMLtRlEoN8"

import streamlit as st
import google.generativeai as genai

# Set your API key
api_key = "AIzaSyCgSIYXikg8bR7FVBaNBFraweMLtRlEoN8"
genai.configure(api_key=api_key)

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text

# Streamlit app layout
st.title("AI Content Generator")
st.write("This app uses Google Generative AI to create content based on your prompt.")

# Input prompt from the user
prompt = st.text_input("Enter a prompt for the AI to generate content:")

if st.button("Generate Content"):
    if prompt:
        with st.spinner("Generating content..."):
            result = generate_content(prompt)
            st.success("Content generated successfully!")
            st.write(result)
    else:
        st.error("Please enter a prompt.")

# Run the app with `streamlit run app.py`
