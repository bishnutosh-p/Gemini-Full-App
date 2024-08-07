import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to My Gemini API Based Application Suite! 👋")

st.sidebar.success("Select a Demo From Above Pages.")

st.markdown(
    """
    This application is created & hosted using Streamlit. It uses Google Gemini API to fetch and provide generative text from Image and Text prompts/queries.
    **👈 Select a demo from the sidebar** 
    ### Want to learn more?
    - GitHub Repository : https://github.com/bishnutosh-p/Gemini-API-Applications
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    ### Disclaimer
    The above applications are powered by Google Gemini, a generative AI model designed to provide text-based responses. The information provided by the AI is for informational purposes only and should not be considered as professional advice. The responses generated may not always be accurate, complete, or up-to-date. Users are encouraged to verify the information independently before making decisions based on the content. Use of this application is at your own risk.
    """
)