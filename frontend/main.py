from pathlib import Path
import streamlit as st
import requests
import os

st.markdown("## Classifying images by the time of day")

image_file = st.file_uploader("Upload your image")
image_path = None
if image_file:

    # Saving file to the shared folder
    shared_folder_path = Path('shared_folder')
    image_path = shared_folder_path / image_file.name

    if not shared_folder_path.exists():
        shared_folder_path.mkdir()

    with open(image_path, "wb") as f:
        f.write(image_file.getbuffer())

data = {'path': str(image_path)}  # Sending the full path to the backend
if st.button('predict'):
    backend_url = "http://backend:8000"  # Use the service name as the hostname
    predict_endpoint = "/predict"
    res = requests.post(url=f"{backend_url}{predict_endpoint}", json=data)

    title_container = st.container()
    col1, col2 = st.columns([15, 5])
    with title_container:
        with col1:
            st.image(image_file)
        with col2:
            st.markdown(f'<h1 style="color: black;">{res.text}</h1>',
                        unsafe_allow_html=True)
