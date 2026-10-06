import os
import streamlit as st
from google import genai

st.set_page_config(page_title="GovGuard", page_icon="???", layout="wide")
st.title("??? GovGuard: AI-Powered Public Infrastructure Integrity Ledger")

api_key_input = st.sidebar.text_input("Enter your Google AI Studio API Key", type="password")
if api_key_input:
    os.environ["GEMINI_API_KEY"] = api_key_input

project_name = st.text_input("Project Name", "Municipal Flyover Phase-2")
if st.button("Run GovGuard AI Audit"):
    if not api_key_input:
        st.error("Please enter your API Key in the sidebar!")
    else:
        client = genai.Client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Generate a professional anti-corruption audit report for public infrastructure project: {project_name}"
        )
        st.markdown(response.text)
