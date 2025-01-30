import streamlit as st
import json

# Load predefined questions and answers
def load_qa_data():
    with open("qa_data.json", "r") as file:
        return json.load(file)

qa_data = load_qa_data()

# Streamlit UI
st.title("Simple Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
user_input = st.chat_input("Type your message...")

if user_input:
    # Store and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Find response from JSON
    response = qa_data.get(user_input.lower(), "I'm sorry, I don't understand that.")

    # Store and display bot response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
