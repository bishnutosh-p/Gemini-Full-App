from PIL import Image
import streamlit as st
import google.generativeai as genai

# Enter your Gemini API key which you can get from https://console.cloud.google.com/

# api_key = "YOUR API KEY"  # Uncomment this and add your key here..
# genai.configure(api_key = api_key)

# This line allows you to access the API key from the secrets file in Streamlit Sharing. 
# If you are running this code locally, you can comment the below 2 lines and uncomment the above part.
api_key = st.secrets['API_KEY']
genai.configure(api_key = api_key)

# Choosing among the available models present in GEmini.
model = genai.GenerativeModel("gemini-1.5-pro")

def get_reponse(input,image):
    if input != '':
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Vision App", page_icon=":photo:",layout="wide")

st.header("Gemini Image Application")

input = st.text_input("Input : ", key = "input")

uploaded_image = st.file_uploader("Upload Your Query Image", type = ['jpg', 'png', 'jpeg'])

image = ""
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption = "Your Uploaded Image.", use_column_width = True)

submit = st.button("Submit")

if submit:
    response = get_reponse(input, image)
    st.markdown(response)