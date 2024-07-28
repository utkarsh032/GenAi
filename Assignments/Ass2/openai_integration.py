import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
load_dotenv()

api_key = os.getenv('API_KEY')

st.markdown("<h1 style='text-align: center;'>Ask Me Anything!</h1>", unsafe_allow_html=True)

user_prompt = st.text_area("", placeholder="Enter your prompt")

col1, col2 = st.columns([4, 1])
with col1:
    st.write("")
with col2:
    generate_button = st.button("Generate")
if generate_button:
    if not api_key:
        st.error("API key not found. Please set it as an environment variable or in the .env file.")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        try:
            response = model.generate_content(user_prompt)
            if response and hasattr(response, 'candidates') and response.candidates:
                generated_text = ""
                for candidate in response.candidates:
                    if hasattr(candidate, 'content') and candidate.content.parts:
                        for part in candidate.content.parts:
                            if hasattr(part, 'text'):
                                generated_text += part.text + "\n"
                            else:
                                st.warning("No text found in this part.")
                    else:
                        st.warning("No content found in this candidate.")
                if generated_text:
                    st.header("AI's response:")
                    st.write(generated_text)
                else:
                    st.warning("No valid candidates found in the response.")
            else:
                st.warning("No valid candidates found in the response.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            

