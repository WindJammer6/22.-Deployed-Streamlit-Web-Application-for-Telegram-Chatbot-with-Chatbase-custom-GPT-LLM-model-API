# Difference between v3 and v2 is that v3 got an extra feature that allows teacher to add their own assignments
# to the database page of the website, which will automatically be added to the side panel of the database page

# (Note: adding a new assignment does not train the chatbase model with that assignment, you still need to
#  train the chatbase model by uploading that assignment again separately, and deleting that assignment
#  from the database page of the website also does not make the chatbase custom GPT LLM forget about the assignment...
#  If you want the chatbase custom GPT LLM to forget about that assignment you need to remove the assignment's training 
#  data from the chatbase custom GPT LLM training data in the chatbase website separately)


# I think for this version I removed the idea of this telegram chatbot project being 'transferrable'
# to other courses first... since its too tedious for now. This version can only work for a single
# course and is not designed to be 'transferrable' between multiple courses... I will only leave that for future versions for
# improvement...


# I also set for the popover to only include ID and name for the assignment to be added because even though
# the telegram chatbot might already be trained with these assignments, but the creation of the assignments here
# allow the telegram chatbot to start adding submissions/conversations for this particular assignment in this databse.
# So this creation of assignments here technically creates the option for students to talk about this
# assignment to the telegram chatbot! 
import streamlit as st
from firebase_admin import db
import firebase_admin


# ////////////////////////////////////////////////////////////////////////////////////


# Realised to fix the issue of the Streamlit website's database page refreshing too often, making it annoying to view the 
# Streamlit website's database page due to the database disappearing due to refreshing every few seconds, is to remove this
# 'st_autorefresh' function:

# # This is an imported function from some guy from Github who managed to create an 'autorefresh' functionality of 
# # Streamlit (Python) web applications. 'st_autorefresh()' is the command from the self-made library 
# # 'streamlit_autorefresh' that allows us to do this.
# # (Link: https://github.com/kmcgrady/streamlit-autorefresh#how-does-this-component-help (kmcgrady, Ken McGrady))
# from streamlit_autorefresh import st_autorefresh


# ////////////////////////////////////////////////////////////////////////////////////


# Page configuration
st.set_page_config(page_title="Course Dashboard", layout="centered")

# Title and logo
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <img src="https://www.xenioo.com/wp-content/uploads/2021/04/telegram-chatbot-1-768x379.png" width="800"/>
    </div>
    """,
    unsafe_allow_html=True
)
st.image("https://tse4.mm.bing.net/th?id=OIP.Z5OdycHGMDwAP-NciVOAkQHaBs&pid=Api&P=0&h=180", width=300)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Details'

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button('View Details'):
        st.session_state.page = 'Details'

with col2:
    if st.button('View Database'):
        st.session_state.page = 'Database'


# //////////////////////////////////////////////////////////////////////////////////////////////////////


# Page content based on the current page

# 'Details' website page
if st.session_state.page == 'Details':
    name_of_chatbase_custom_GPT_LLM_model = "SUTD's Computation Thinking and Design (CTD) (10.014) module Telegram Chatbot Teaching Assistant"


    st.header("Name of the Telegram Chatbot Chatbase custom GPT LLM model:")
    st.write(name_of_chatbase_custom_GPT_LLM_model)
    st.write("---")
    # To take in a text input instead:
    # name = st.text_input("Name of the chatbot", "CTD Chatbot", label_visibility='collapsed')


    st.header(f"Role of the {name_of_chatbase_custom_GPT_LLM_model}")
    st.write("You are a teaching assistant for the students in SUTD's Computation Thinking and Design (CTD) (10.014) module that helps novice programmers learn programming.")
    st.write("---")
    # To take in a text input instead:
    # role = st.text_area("You are a teaching assistant for the students in SUTD's Computation Thinking and Design (CTD) (10.014) module.", label_visibility='collapsed')

    
    st.header(f"Craft suggested responses for the {name_of_chatbase_custom_GPT_LLM_model}:")
    st.write("""
            You will receive prompts from students in this SUTD's Computation Thinking and Design (CTD) (10.014) module in the following format:
'''
🎉 Thanks for sharing your code! Here's a quick recap of everything you've provided:\n\n📌 Student ID: ['student_id']}\n\n📌 Assignment: ['assignment']}\n\n📌 Code: ['code_submitted']}\n\nLooking good? Ready to submit it for evaluation? 😄
'''
where, 
- ['student_id'] will be the student's identification number
- ['assignment'] will be the assignment that the student would like to submit their code for
- ['code_submitted'] will be the code the student will be submitting for the following assignment

            
If any of these 3 information seems unexpected or incomplete please respond with: 'The student id/assignment id/code submitted seems unexpected or incomplete. Please resubmit the assignment!'

Otherwise, if the 3 information is expected and seems complete, I would like you to respond in the following format:
'
- Test cases failed for the assignment:
- Test cases score for the assignment:
- Recommended changes/advice to the code for the assignment with explanation:
'
""")
    st.write("---")
    # To take in a text input instead:
    # prompt1 = st.text_input("Prompt 1", "", label_visibility='collapsed')
    # prompt2 = st.text_input("Prompt 2", "", label_visibility='collapsed')
    # prompt3 = st.text_input("Prompt 3", "", label_visibility='collapsed')
    # prompt4 = st.text_input("Prompt 4", "", label_visibility='collapsed')


    st.header(f"Train {name_of_chatbase_custom_GPT_LLM_model}")
    st.write("Go to this website: \n\nhttps://www.chatbase.co/dashboard/goh-jet-wei-team-91859289/chatbot/wGS8ehg-39TolweihWY3w\n\nto train the Chatbase custom GPT LLM model with your teaching material and assignments.")





# 'Database' website page
elif st.session_state.page == 'Database':


    # //////////////////////////////////////////////////////////////////////////////////////////


    # Realised to fix the issue of the Streamlit website's database page refreshing too often, making it annoying to view the 
    # Streamlit website's database page due to the database disappearing due to refreshing every few seconds, is to remove this
    # 'st_autorefresh' function:
    
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
    # st_autorefresh(interval=10000, key="dataframerefresh")


    # //////////////////////////////////////////////////////////////////////////////////////////


    # Initialising multiple Firebase Realtime Database/projects in the same Python file


    # Setting up the Firebase database for the conversations:

    #Here is the link that goes directly to this UROP Telegram Chatbot project's Firebase Realtime database:
    #https://console.firebase.google.com/u/0/project/urop-telegram-chatbot/database/urop-telegram-chatbot-default-rtdb/data

    #This if statement, accompanied by the condition with the function 'firebase_admin._apps', is used to prevent
    #any error from creating multiple Firebase apps with the same name. 
    
    #The 'firebase_app = firebase_admin.initialize_app' within this if statement will instantiate a Firebase app 
    #if it is not already created, which is what the 'firebase_admin._apps' does, as an internal variable that 
    #keeps track of the initialized Firebase apps. It is a dictionary-like object that holds information about 
    #the Firebase apps that have been initialized in your Python application.
    if "conversations" not in firebase_admin._apps:
        # Initialize Firebase
        credentials_object_conversations = firebase_admin.credentials.Certificate("firebase_key_conversations.json")
        firebase_admin.initialize_app(credentials_object_conversations, {
            'databaseURL': 'https://urop-telegram-chatbot-default-rtdb.asia-southeast1.firebasedatabase.app/'
        }, name='conversations')

    # Get a reference to the database
    reference_to_database_conversations = db.reference('/', app=firebase_admin.get_app('conversations'))



    # Setting up the Firebase database for the assignments:

    #Here is the link that goes directly to this UROP Telegram Chatbot project's Firebase Realtime database:
    #https://console.firebase.google.com/u/0/project/urop-chatbot-assignments/database/urop-chatbot-assignments-default-rtdb/data

    #This if statement, accompanied by the condition with the function 'firebase_admin._apps', is used to prevent
    #any error from creating multiple Firebase apps with the same name. 
    
    #The 'firebase_app = firebase_admin.initialize_app' within this if statement will instantiate a Firebase app 
    #if it is not already created, which is what the 'firebase_admin._apps' does, as an internal variable that 
    #keeps track of the initialized Firebase apps. It is a dictionary-like object that holds information about 
    #the Firebase apps that have been initialized in your Python application.    
    if "assignments" not in firebase_admin._apps:
        # Initialize Firebase
        credentials_object_assignments = firebase_admin.credentials.Certificate("firebase_key_assignments.json")
        firebase_admin.initialize_app(credentials_object_assignments, {
            'databaseURL': 'https://urop-chatbot-assignments-default-rtdb.asia-southeast1.firebasedatabase.app/'
        }, name='assignments')

    # Get a reference to the database
    reference_to_database_assignments = db.reference('/', app=firebase_admin.get_app('assignments'))


    # ////////////////////////////////////////////////////////////////////////////////////////////////////////


    # Firebase's Database for assignments to Streamlit website things

    # Read data from the Realtime Database from Firebase
    database_data_assignments = reference_to_database_assignments.get()

    print("Firebase UROP Telegram Chatbot assignments Realtime Database Data:", database_data_assignments)

    # Check if the Firebase Realtime database is None or empty
    if database_data_assignments is None:
        st.write("No data found in the Firebase Realtime Database.")
    else:
        # Converting the Firebase Realtime Database to a list of dictionaries
        if isinstance(database_data_assignments, dict):
            database_data_assignments = list(database_data_assignments.values())

            print(f"Database data assignments variable: {database_data_assignments}")


    # ////////////////////////////////////////////////////////////////////////////////////////////////////////


    # Sidebar of the 'Database' website page
    
    # Course: Computational Thinking and Design (10.014) title section
    st.sidebar.header("Course: Computational Thinking and Design (10.014)")


    # Add Assignment popup section
    with st.sidebar.popover("Add Assignment"):
        st.markdown(
            """
            <style>
            .big-font {
                font-size:30px !important;
            }
            </style>
            <p class="big-font">Add a new Assignment:</p>
            """,
            unsafe_allow_html=True
        )
        st.write("Just click the 'Add Assignment' button once! Then click the 'Refresh page' button for the added assignment to show up!")
        assignment_name = st.text_input("Name of the assignment:")
        assignment_link = st.text_input("Link to the assignment:")

        if st.button("Add Assignment"):
            #If confirmation add assignment button is pressed in the Streamlit (Python) web application, the program will 'push' 
            #basically add this new pieces of user data into the Realtime database in Firebase  
            reference_to_database_assignments.push({"assignment_name" : assignment_name, "assignment_link" : assignment_link})    


    # Remove Assignment popup section
    with st.sidebar.popover("Remove Assignment"):
        st.markdown(
            """
            <style>
            .big-font {
                font-size:30px !important;
            }
            </style>
            <p class="big-font">Remove an Assignment by clicking the corresponding button:</p>
            """,
            unsafe_allow_html=True
        )
        st.write("Just click assignment to be removed button once! Then click the 'Refresh page' button for the removed assignment to be deleted!")
    
        if database_data_assignments is not None:
            for i, assignment in enumerate(database_data_assignments):

                if st.button(f"{assignment['assignment_name']}", key=f"assignment_{i}"):
                    for key, value in reference_to_database_assignments.get().items():
                        if value.get('assignment_name') == assignment['assignment_name']:
                            # Remove the data based on the key
                            reference_to_database_assignments.child(key).delete()
                            print(f"Removed assignment with key: {key} and assignment name: {assignment['assignment_name']}")
                            break
                    else:
                        print("No matching records found.")


    # Refresh page section
    st.sidebar.write("")
    st.sidebar.write("Added or removed an assignment? Click refresh to see the changes on the Streamlit website!")
    if st.sidebar.button("Refresh page"):
        pass


    st.sidebar.write("---")


    # Search by Student ID section
    st.sidebar.header("Search by Student ID")
    search_by_student_id = st.sidebar.text_input("")
    if st.sidebar.button("Search"):


        # ////////////////////////////////////////////////////////////////////////////////////////////////////////


        # Firebase's Database for conversations to Streamlit website things

        # Read data from the Realtime Database from Firebase
        database_data_conversations = reference_to_database_conversations.get()

        print("Firebase UROP Telegram Chatbot conversations Realtime Database Data:", database_data_conversations)

        # Check if the Firebase Realtime database is None or empty
        if database_data_conversations is None:
            st.write("No data found in the Firebase Realtime Database.")
        else:
            # Converting the Firebase Realtime Database to a list of dictionaries
            if isinstance(database_data_conversations, dict):
                database_data_conversations = list(database_data_conversations.values())

                print(f"Database data conversations variable: {database_data_conversations}")
            
            # Main content
            st.subheader(f"Search by Student ID: {search_by_student_id}")
            st.write("---")
            for i in range(len(database_data_conversations)-1, -1, -1):
                if database_data_conversations[i]['student_id'] == search_by_student_id:
                    st.write(f"**Student ID:** {database_data_conversations[i]['student_id']} | **Assignment ID:** {database_data_conversations[i]['assignment']} | **Date and time of submission:** {database_data_conversations[i]['date_and_time_of_submission']}")
                    st.write("**Code Submitted:**")
                    st.code(f"{database_data_conversations[i]['code_submitted']}")
                    st.write("**Chatbase custom GPT LLM model Response:**")
                    st.write(f"{database_data_conversations[i]['telegram_chatbot_chatbase_response']}")
                    st.write("---")

        
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////


    st.sidebar.write("---")



    # Search by Assignment section
    st.sidebar.header("Search by Assignments")

    if database_data_assignments is not None:
        for i, assignment in enumerate(database_data_assignments):

            if st.sidebar.button(f"{assignment['assignment_name']}", key=f"assignment_{i+1000}"):
                search_by_assignment = f"{assignment['assignment_name']}"
                print(search_by_assignment)


                # ////////////////////////////////////////////////////////////////////////////////////////////////////////


                # Firebase's Database for conversations to Streamlit website things

                # Read data from the Realtime Database from Firebase
                database_data_conversations = reference_to_database_conversations.get()

                print("Firebase UROP Telegram Chatbot conversations Realtime Database Data:", database_data_conversations)

                # Check if the Firebase Realtime database is None or empty
                if database_data_conversations is None:
                    st.write("No data found in the Firebase Realtime Database.")
                else:
                    # Converting the Firebase Realtime Database to a list of dictionaries
                    if isinstance(database_data_conversations, dict):
                        database_data_conversations = list(database_data_conversations.values())

                        print(f"Database data conversations variable: {database_data_conversations}")

                    
                    # Main content
                    st.subheader(f"Search by {assignment['assignment_name']}")
                    st.write("---")
                    for i in range(len(database_data_conversations)-1, -1, -1):
                        if database_data_conversations[i]['assignment'] == search_by_assignment:
                            st.write(f"**Student ID:** {database_data_conversations[i]['student_id']} | **Assignment ID:** {database_data_conversations[i]['assignment']} | **Date and time of submission:** {database_data_conversations[i]['date_and_time_of_submission']}")
                            st.write("**Code Submitted:**")
                            st.code(f"{database_data_conversations[i]['code_submitted']}")
                            st.write("**Chatbase custom GPT LLM model Response:**")
                            st.write(f"{database_data_conversations[i]['telegram_chatbot_chatbase_response']}")
                            st.write("---")
