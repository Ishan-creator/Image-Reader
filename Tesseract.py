from dotenv import load_dotenv

load_dotenv() ##all the environments variabls from.env file
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai 
import pytesseract

   
def input_file_details(uploaded_file):
    if uploaded_file is not None:
        content_type = uploaded_file.type.lower()
        if content_type.startswith("image/"):
            text = extract_text_from_image(uploaded_file)
        else:
            raise ValueError("Unsupported file type. Please upload an image.")
        return text
    else:
        raise FileNotFoundError("No file uploaded")
    
def extract_text_from_image(uploaded_file):
    # Using Tesseract OCR for text extraction from images
    image = Image.open(uploaded_file)
    text = pytesseract.image_to_string(image)
    return text


uploaded_file = st.file_uploader("Choose an image" , type = ["jpg", "jpeg","png","pdf"])
text = " "

if uploaded_file is not None:
    text = input_file_details(uploaded_file)
    st.text("Extracted Text:")
    st.text(text)


