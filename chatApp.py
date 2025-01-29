import streamlit as st
from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_mistralai import ChatMistralAI
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("MISTRAL_API_KEY is not set in the environment variables.")

# Setup Firestore and session variables
PROJECT_ID = "langchain-e1336"
SESSION_ID = "user_session_new"  # This could be a username or unique session ID
COLLECTION_NAME = "chat_history"

# Initialize Firestore Client
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)

# Initialize Mistral AI model
model = ChatMistralAI(api_key=api_key, model="mistral-large-latest")

# Streamlit UI for the chat application
st.title("AI Chat Application")
st.write("Start chatting with the AI.")

# Chat history display
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.markdown(f"**User**: {message['content']}")
    else:
        st.markdown(f"**AI**: {message['content']}")

# User input form
user_input = st.text_input("Type your message:")

# Handle user input and AI response
if user_input:
    # Add user's message to chat history
    chat_history.add_user_message(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Get AI's response
    ai_response = model.invoke(chat_history.messages)

    # Ensure response is valid
    if ai_response and ai_response.content:
        # Add AI's message to chat history
        chat_history.add_ai_message(ai_response.content)
        st.session_state["messages"].append({"role": "ai", "content": ai_response.content})
    else:
        st.session_state["messages"].append({"role": "ai", "content": "Sorry, I didn't understand that."})

# Option to reset chat history
if st.button("Reset Chat"):
    st.session_state["messages"] = []
    st.rerun()

