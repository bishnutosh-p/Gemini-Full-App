# from dotenv import load_dotenv
# load_dotenv()

from PIL import Image
import streamlit as st
import os
import google.generativeai as genai

api_key = st.secrets['API_KEY']
genai.configure(api_key = api_key)


# genai.configure(api_key = os.getenv('API_KEY'))

model = genai.GenerativeModel("gemini-1.5-pro")

chat = model.start_chat(history = [])

def get_response(query):
    response = chat.send_message(query, stream = True)
    return response

st.set_page_config(page_title="Gemini Chat App", page_icon=":rocket:",layout="wide")
st.header("Google Gemini Chat Application")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

input = st.text_input("Input : ", key = "input")
submit = st.button("Submit")

if submit and input:
    response = get_response(input)
    # st.session_state.chat_history.append(f"User: {input}")
    # st.session_state.chat_history.append(f"Google Gemini: {response}")
    # st.text("\n".join(st.session_state.chat_history))
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response is:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Google Gemini",chunk.text))

st.subheader("Chat History is:")

for role,text in st.session_state["chat_history"]:
    st.write(f"{role}:{text}")