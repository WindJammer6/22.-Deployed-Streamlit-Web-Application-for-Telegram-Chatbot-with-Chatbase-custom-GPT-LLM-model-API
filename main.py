import streamlit as st
import pymysql

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


    # Setting up the MySQL server:
    my_sql_relational_database_connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="urop_telegram_chatbot_db"
    )

    cursor = my_sql_relational_database_connection.cursor()


    # //////////////////////////////////////////////////////////////////////////////////////////


    st.sidebar.header("Course: Computational Thinking and Design (10.014)")
    search = st.sidebar.text_input("Search for a course...")
    st.sidebar.button("View Assignment")
    st.sidebar.header("Search by AssignmentID")
    assignments = ["ID: 123) Two Sum", "ID: 124) Add 2 numbers", "ID: 125) Longest Sub...", "ID: 126) Median of T...", "ID: 127) Longest Pal...", "ID: 128) Zigzag Conv..."]
    for assignment in assignments:
        st.sidebar.write(assignment)


    # ////////////////////////////////////////////////////////////////////////////////////////////////////////


    # MySQL server's Relational Database's table to Streamlit website things

    cursor.execute("SELECT * FROM telegram_chatbot_history")
    rows_in_a_tuple = cursor.fetchall()
    
    # Main content
    st.subheader("Assignments")
    for row in rows_in_a_tuple:
        st.write("**Student Prompt**")
        st.write(f"{row[1]}")
        st.write("**Telegram Chatbot Response**")
        st.write(f"{row[2]}")
        st.write("---")


    # ////////////////////////////////////////////////////////////////////////////////////////////////////////


    # Back to Homepage button
    if st.button("Back to Homepage"):
        st.write("Back to homepage button clicked")
