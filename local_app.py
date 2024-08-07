# Getting the Gemini API Key from the config.json file.
# import json
# with open('config.json', 'r') as config_file:
#     config = json.load(config_file)
# API_KEY = config['api_key']

# Importing all other necessary libraries.
import os
import google.generativeai as genai     # This is needed for handling the Google API calls.
import pyfiglet                         # For the App banner.

# There is another way to include the API key in the code, it is from the .env file.
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Testing the API and trying to generate content. Copied straight from the official docs of Google Gemini.
# response = model.generate_content("Write a story about a AI and magic")
# print(response.text)

def print_banner():
    banner = pyfiglet.figlet_format("Gemini Chat App")
    print(banner)
    print("Welcome to the Google Gemini based Chat app. Type 'exit' to quit.")
    print("-" * 65)

print_banner()
user_name = input("Enter your Name : ") or "Guest User"
exit = False
while(not exit):
    user_input = input(f"Hello {user_name},\nEnter your query : ")
    if(user_input == "exit"):
        exit = True
        print("\nThank you for using the Gemini Chat App. Goodbye! :) \n")
    else:
        print("\nthinking.....\n")
        try:
            response = model.generate_content(user_input)
            print(f"\nGemini : {response.text}\n")
        except Exception as e:
            print(f"Error occurred while generating content: {str(e)}")