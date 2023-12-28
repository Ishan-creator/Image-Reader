from dotenv import load_dotenv

load_dotenv() ##all the environments variabls from.env file
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai 


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model= genai.GenerativeModel('gemini-pro-vision')

def get_gimini_responce(input, image,prompt):
    response=model.generate_content([input,image[0], prompt])
    return response.text



def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data= uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file Uploaded")


st.set_page_config(page_title='MultiLanguage Invoice Extractor')

st.header('MultiLanguage Invoice Extractor')
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the Invoice" , type = ["jpg", "jpeg","png","pdf"])
image = " "

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width= True)

submit = st.button("Tell me about the invoice")


input_prompt = """
You are an expert in understanding different types of images. We will upload a image and you will have to answer any question based on
the uploaded image.
"""

if submit:
    image_data = input_image_details(uploaded_file)
    responce= get_gimini_responce(input_prompt, image_data, input)
    st.subheader("The responce is")
    st.write(responce)