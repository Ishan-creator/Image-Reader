import google.generativeai as genai
import PIL.Image

img = PIL.Image.open('image.jpg')

genai.configure(api_key='Your_api_key')

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(["what is the total?", img])

print(response.text)