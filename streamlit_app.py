import streamlit as st
from langchain_core.messages import HumanMessage

from app.mentor import get_mentor_response

st.set_page_config(
    page_title="AI Interview Mentor",
    page_icon="🎯",
    layout="centered",
)

st.title("AI Interview Preparation Mentor")
st.caption("Powered by LangChain + Ollama (llama3.2)")

# Initialize chat history once per browser session (persists across reruns)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar control to start a fresh interview session
with st.sidebar:
    st.header("Session Controls")
    if st.button("Clear Conversation", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# Render all previous turns from the single chat_history list
for message in st.session_state.chat_history:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# Read new user input from the chat box
user_input = st.chat_input("Ask an interview question or share your target role...")

if user_input:
    cleaned_input = user_input.strip()
    if not cleaned_input:
        st.warning("Please enter a question.")
    else:
        with st.chat_message("user"):
            st.markdown(cleaned_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = get_mentor_response(
                        cleaned_input,
                        st.session_state.chat_history,
                    )
                    st.markdown(response)
                except Exception as exc:
                    st.error(f"Something went wrong: {exc}")