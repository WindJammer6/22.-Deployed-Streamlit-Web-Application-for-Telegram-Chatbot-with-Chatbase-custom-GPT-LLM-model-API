import streamlit as st

# Page configuration
st.set_page_config(page_title="Telegram Chatbot Teaching Assistant", layout="centered")

# Title and logo
st.image("https://www.xenioo.com/wp-content/uploads/2021/04/telegram-chatbot-1-768x379.png", width=80)
st.title("SUTD")

# Form fields
st.header("Name of your Telegram Chatbot Teaching Assistant")
name = st.text_input("Name of the chatbot", "CTD Chatbot", label_visibility='collapsed')

st.header("Role of your Telegram Chatbot Teaching Assistant")
role = st.text_area("Role of the chatbot", "I would like you to act as a teaching assistant for the students in the CTD module I am teaching in SUTD", label_visibility='collapsed')

st.header("Craft suggested prompts in the Telegram Chatbot Teaching Assistant")
prompt1 = st.text_input("Prompt 1", "", label_visibility='collapsed')
prompt2 = st.text_input("Prompt 2", "", label_visibility='collapsed')
prompt3 = st.text_input("Prompt 3", "", label_visibility='collapsed')
prompt4 = st.text_input("Prompt 4", "", label_visibility='collapsed')

st.header("Train your Telegram Chatbot Teaching Assistant")
st.text_area("Training instructions", "Go to this website to feed your teaching material and assignments to the Telegram Chatbot Teaching Assistant:\nhttps://chatbase.com/trainmodelhere/notreallink", height=100, label_visibility='collapsed')

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Back to Homepage"):
        st.write("Back to homepage button clicked")

with col2:
    if st.button("Update Telegram Chatbot"):
        st.write("Update Telegram Chatbot button clicked")
