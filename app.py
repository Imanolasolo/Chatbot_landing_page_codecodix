import streamlit as st
import base64

# Chatbot Landing page

# Page config
st.set_page_config(page_title="Chatbot Landing page", page_icon="🤖", layout="wide")

# Function to encode image as base64 to set as background
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Encode the background image
img_base64 = get_base64_of_bin_file('fondo.jpg')

# Set the background image using the encoded base64 string
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url('data:image/jpeg;base64,{img_base64}') no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Chatbot Landing page links
st.title("Chatbot Landing page")
st.markdown("### Welcome to the Chatbot Landing page")
st.markdown("#### Click on the links below to access the chatbots")
st.link_button("AI Medicare Chat", "https://ai-medicare-chat.streamlit.app/")
st.link_button("CodeCodix Chat", "https://codecodix-chat.streamlit.app/")
st.link_button("MHC Chat", "https://mhc-chat.streamlit.app/")
st.link_button("AI Profile VCard", "https://aiprofilevcard.streamlit.app/")

# Footer
st.markdown('---')
st.markdown("Made by CodeCodix @ 2024")