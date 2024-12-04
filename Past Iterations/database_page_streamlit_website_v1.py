import streamlit as st

# Page configuration
st.set_page_config(page_title="Course Dashboard", layout="centered")

# Title and logo
st.image("https://www.xenioo.com/wp-content/uploads/2021/04/telegram-chatbot-1-768x379.png", width=80)
st.title("SUTD")

# Sidebar for course selection
st.sidebar.header("Course: Computational Thinking and Design (10.014)")
search = st.sidebar.text_input("Search for a course...")
st.sidebar.button("View Assignment")
st.sidebar.header("Search by AssignmentID")
assignments = ["ID: 123) Two Sum", "ID: 124) Add 2 numbers", "ID: 125) Longest Sub...", "ID: 126) Median of T...", "ID: 127) Longest Pal...", "ID: 128) Zigzag Conv..."]
for assignment in assignments:
    st.sidebar.write(assignment)

# Main content
st.subheader("Assignments")
for i in range(2):  # Example with two users
    st.write(f"**UserID: {73264879283 + i} | CourseID: 10.014 | AssignmentID: 123 (Two Sum)**")
    st.text_area("Python code:", "import random\n\nprint('Hello world')\n\nfor i in range():\n...", height=150, key=f"code{i}")
    st.write("**Telegram Chatbot Teaching Assistant:**")
    st.write("Test score: 0/10\nTest cases failed: 1,2,3,4,5,6,7,8,9,10")
    st.write("Recommended changes/advice to the Python code:\nYou forgot to add a parameter into the `range()` function of the for loop.")
    st.write("---")

# Back to Homepage button
if st.button("Back to Homepage"):
    st.write("Back to homepage button clicked")

