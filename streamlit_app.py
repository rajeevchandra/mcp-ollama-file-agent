import streamlit as st
import requests

MCP_API = "http://host.docker.internal:3333"  # Changed for Docker compatibility

st.title("📁 Local File Summarizer with Ollama + MCP")

directory = st.text_input("Directory Path", "./docs")
if st.button("List Files"):
    try:
        resp = requests.post(f"{MCP_API}/list_files", json={"directory": directory})
        files = resp.json()
        st.write(files)
    except Exception as e:
        st.error(f"Failed to list files: {e}")

selected_file = st.text_input("Filename to Summarize")
if st.button("Summarize"):
    try:
        resp = requests.post(f"{MCP_API}/read_and_summarize", json={"filepath": f"{directory}/{selected_file}"})
        st.write(resp.json())
    except Exception as e:
        st.error(f"Failed to summarize file: {e}")