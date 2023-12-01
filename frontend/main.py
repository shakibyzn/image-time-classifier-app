from pathlib import Path
import streamlit as st
import time
import requests
import os

st.markdown("## Classifying images by the time of day")

image_file = st.file_uploader("Upload your image")
image_path = None
if image_file:

    # saving file
    image_path = str(Path('..', 'images', image_file.name))
    if not os.path.exists(image_path):
        os.makedirs('../images')

    with open(image_path, "wb") as f:
        f.write(image_file.getbuffer())

data = {'path': image_path}
if st.button('predict'):
    res = requests.post(url="http://localhost:8000/predict", json=data)

    title_container = st.container()
    col1, col2 = st.columns([15, 5])
    with title_container:
        with col1:
            st.image(image_file)
        with col2:
            st.markdown(f'<h1 style="color: black;">{res.text}</h1>',
                        unsafe_allow_html=True)

# containerize fastapi with docker
# test
# https://github.com/Shikha-code36/ImageDetection-FastApi/tree/main readme