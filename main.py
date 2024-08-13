import streamlit as st
from firebase_admin import db
import firebase_admin

# This is an imported function from some guy from Github who managed to create an 'autorefresh' functionality of 
# Streamlit (Python) web applications. 'st_autorefresh()' is the command from the self-made library 
# 'streamlit_autorefresh' that allows us to do this.
# (Link: https://github.com/kmcgrady/streamlit-autorefresh#how-does-this-component-help (kmcgrady, Ken McGrady))
from streamlit_autorefresh import st_autorefresh

# Page configuration
st.set_page_config(page_title="Course Dashboard", layout="centered")

# Title and logo
st.image("https://www.xenioo.com/wp-content/uploads/2021/04/telegram-chatbot-1-768x379.png", width=80)
st.title("SUTD")

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Details'

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button('Details'):
        st.session_state.page = 'Details'

with col2:
    if st.button('Database'):
        st.session_state.page = 'Database'


# //////////////////////////////////////////////////////////////////////////////////////////////////////


# Page content based on the current page

# 'Details' website page
if st.session_state.page == 'Details':
    # Details Page
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
            print(f"Prompt 4 Submitted: {prompt4}")
            st.write("Submitted!", icon="✅")





# 'Database' website page
elif st.session_state.page == 'Database':


    # //////////////////////////////////////////////////////////////////////////////////////////


    ##########################
    #THE AUTOREFRESH FUNCTION#
    ##########################
    #Here is the 'st_autorefresh' function from the self-made library 'streamlit_autorefresh' created by Ken McGrady
    #on Github that allows autorefresh functionality of the Streamlit (Python) web application

    # 'st_autorefresh()' function's parameters:
    # -> interval: int. 
    #    - Amount of time in milliseconds to limit
    # -> limit: int or None. 
    #    - Amount of refreshes to allow. If none, it will refresh infinitely. While infinite refreshes sounds nice, 
    #      it will continue to utilize computing resources.
    # -> debounce: boolean.
    #    - Whether to delay the autorefresh when user interaction occurs. Defaults to True in order to avoid 
    #      refreshes interfering with interaction effects on scripts.
    # -> key: str or None.
    #    - An optional key that uniquely identifies this component. If this is None, and the component's arguments 
    #      are changed, the component will be re-mounted in the Streamlit frontend and lose its current state. 
    st_autorefresh(interval=10000, key="dataframerefresh")


    # //////////////////////////////////////////////////////////////////////////////////////////


    # Setting up the Firebase database:

    #Here is the link that goes directly to this UROP Telegram Chatbot project's Firebase Realtime database:
    #https://console.firebase.google.com/u/0/project/urop-telegram-chatbot/database/urop-telegram-chatbot-default-rtdb/data

    #This if statement, accompanied by the condition with the function 'firebase_admin._apps', is used to prevent
    #any error from creating multiple Firebase apps with the same name. 
    
    #The 'firebase_app = firebase_admin.initialize_app' within this if statement will instantiate a Firebase app 
    #if it is not already created, which is what the 'firebase_admin._apps' does, as an internal variable that 
    #keeps track of the initialized Firebase apps. It is a dictionary-like object that holds information about 
    #the Firebase apps that have been initialized in your Python application.
    if not firebase_admin._apps:
        # Initialize Firebase
        credentials_object = firebase_admin.credentials.Certificate("firebase_key.json")
        firebase_admin.initialize_app(credentials_object, {
            'databaseURL': 'https://urop-telegram-chatbot-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })

    # Get a reference to the database
    reference_to_database = db.reference('/')
    
    # Read data from the Realtime Database from Firebase
    print(reference_to_database.get())


    # //////////////////////////////////////////////////////////////////////////////////////////


    st.sidebar.header("Course: Computational Thinking and Design (10.014)")
    search = st.sidebar.text_input("Search for a course...")
    st.sidebar.button("View Assignment")
    st.sidebar.header("Search by AssignmentID")
    assignments = ["ID: 123) Two Sum", "ID: 124) Add 2 numbers", "ID: 125) Longest Sub...", "ID: 126) Median of T...", "ID: 127) Longest Pal...", "ID: 128) Zigzag Conv..."]
    for assignment in assignments:
        st.sidebar.write(assignment)


    # ////////////////////////////////////////////////////////////////////////////////////////////////////////


    # Firebase's Database to Streamlit website things

    # Read data from the Realtime Database from Firebase
    database_data = reference_to_database.get()

    print("Database Data:", database_data)

    # Check if the Firebase Realtime database is None or empty
    if database_data is None:
        st.write("No data found in the Firebase Realtime Database.")
    else:
        # Converting the Firebase Realtime Database to a list of dictionaries
        if isinstance(database_data, dict):
            database_data = list(database_data.values())

        # Main content
        st.subheader("Assignments")
        for i in range(len(database_data)):
            st.write("**Student Prompt**")
            st.write(f"{database_data[i]['student_prompt']}")
            st.write("**Telegram Chatbot Response**")
            st.write(f"{database_data[i]['telegram_chatbot_response']}")
            st.write("---")

    
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////


    # Back to Homepage button
    if st.button("Back to Homepage"):
        st.write("Back to homepage button clicked")
