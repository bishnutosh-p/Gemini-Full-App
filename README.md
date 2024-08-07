---

# Gemini API Application

---

This project utilizes the Gemini API to query generative AI models based on image and text inputs, producing text outputs. The application is built using Python and offers a straightforward interface for interacting with the Gemini API, along with a Streamlit-based frontend.

## Features

- **Image and Text Inputs**: Accepts both image and text inputs for querying the Gemini API.
- **Text Output**: Generates and retrieves text-based responses from the AI model.
- **Streamlit Interface**: Provides an easy-to-use web interface for interaction with the application.
- **Modular Design**: Easily extendable for different use cases or additional functionalities.

## Screenshots

1. Streamlit App for Visual/Image Input ( vision_app.py )
![alt text](image.png)

Link : https://vision-app.streamlit.app/

2. Streamlit App for Text Input ( single_query_app.py )
![alt text](image-1.png)

3. Streamlit App for Question and Answer Chat ( qna_chat_app.py )
![alt text](image-3.png)

Link : https://chat-app-gemini-qna.streamlit.app/

4. CLI App for Local Running ( local_app.py )
![alt text](image-2.png)

## Requirements/Prerequisites

- Python 3
- Gemini API Key
- Streamlit

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/bishnutosh-p/Gemini-API-Applications.git
   cd gemini-api-applications
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your Gemini API key:
   ```bash
   API_KEY="your_api_key_here"
   ```
   Incase you are deploying using Streamlit then create a folder of .streamlit and add secret.toml file inside which you store your secret/api key.

### Running the Streamlit Application

1. **Start the Streamlit App**:
   ```bash
   streamlit run <app_name>.py
   ```
   <app_name> can be substituted with the following
   - vision_app.py
   - qna_chat_app.py
   - single_query_app.py

2. **Access the Web Interface**:
   Open your browser and go to `http://localhost:8501` to use the application.

3. **Input Your Query**:
   - You can input an image by uploading it or text directly into the provided fields.
   - The application will process the input and generate a text response.

4. **You can run the Local**
   ```bash
   python local_app.py
   ```

## Project Structure

```
gemini-api-applications/
│
├── vision_app.py       # Main Streamlit application file for image based
├── qna_chat_app.py     # Main Streamlit application file for text based continues communication
├── local_app.py        # App which runs locally
├── single_query_app.py # Main Streamlit application file for text based
├── .gitignore          # Utility functions for image and text processing
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any features, bugs, or suggestions.

## Thank You.. :)
---