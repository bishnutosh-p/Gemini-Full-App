# from dotenv import load_dotenv
# load_dotenv()                           # Loads all the env varibles.

import streamlit as st
# import os
import google.generativeai as genai
# import pyfiglet                         # Optional, for the banner. Can be used while running locally.
# import re                               # For the regular expression based cleaning of the output text.

# If you are using Streamlit and hosting it then you might want to uncomment this and comment the next line.
api_key = st.secrets['API_KEY']
genai.configure(api_key = api_key)

# genai.configure(api_key = os.getenv('API_KEY')) #If you are using local install and not using Streamlit Sharing then comment this.



def create_gemini_model(type = 'gemini-1.5-flash-latest'):
    '''
    This function creates a Google Gemini Model with the specified type of parameter which is supplied. This can be any of the following as of now:
        gemini-1.0-pro
        gemini-1.0-pro-001
        gemini-1.0-pro-latest
        gemini-1.0-pro-vision-latest
        gemini-1.5-flash
        gemini-1.5-flash-001
        gemini-1.5-flash-latest
        gemini-1.5-pro
        gemini-1.5-pro-001
        gemini-1.5-pro-latest
        gemini-pro
        gemini-pro-vision
    '''
    model = genai.GenerativeModel(type)
    return model

def generate_response(model, prompt):
    '''
    This function generates a response using the Google Gemini model. The prompt is the input sentence from the user. Model is the model which answers the prompt it can be any model which is generated through the 'create_gemini_model'.
    '''
    print('Generating content...')
    response = model.generate_content(prompt)
    return response.text

def clean_response(response):
    '''
    This function cleans the response text by removing any special characters like *, #, etc. It uses the re library for this purpose.
    '''
    cleaned_response = re.sub(r'[\*\#]', '', response.text)
    return cleaned_response

def test():
    '''
    This Function can be used to test out the installation and overall setup of this application. It uses powershell/bash to execute the program and gives an overall idea if the program is working or not. 
    '''
    banner = pyfiglet.figlet_format("Gemini Chat App")
    print(banner)
    print("Welcome to the Google Gemini based Chat app. Type 'exit' to quit.")
    print("-" * 65)

    user_name = input("Enter your Name : ") or "Guest User"
    print(f"Hello {user_name} !!")
    exit = False
    model = create_gemini_model()
    while(not exit):
        user_input = input(f"{user_name} : ")
        if(user_input == "exit"):
            exit = True
            print("\nThank you for using the Gemini Chat App. Goodbye! :) \n")
        else:
            print("\nthinking.....\n")
            try:
                response = model.generate_content(user_input)
                cleaned_response = clean_response(response)
                print(f"Gemini : {cleaned_response}")
            except Exception as e:
                print(f"Error occurred while generating content: {str(e)}")

def main():
    '''
    This is the main function and the execution starts through this function. Any functions and/or code will begin its execution from here.
    '''
    # test()
    st.set_page_config(page_title="Gemini Chat App", page_icon=":smile:",layout="wide")
    st.header("Google Gemini Text Input Application")
    input_box = st.text_input("Input : ", key = "input")
    submit_btn = st.button("Submit")

    if submit_btn:
        model = create_gemini_model()
        response = generate_response(model, input_box)
        st.markdown(response)


if __name__ == "__main__":
    main()
