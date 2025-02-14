
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from chatgpt import llm_stream, process_stream


def ask_question(user_prompt: str):
    st.session_state.history.user(user_prompt)
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Placeholder for the assistant's reply
    assistant_message_placeholder = st.chat_message("assistant")
    assistant_text = assistant_message_placeholder.empty()

    # Stream response
    with st.spinner("Loading..."):
        db = FAISS.from_documents(st.session_state.documents, OpenAIEmbeddings())
        for response in db.similarity_search(user_prompt, k=3):
            print("article: " + response.page_content)
            st.session_state.history.system(response.page_content)
        st.session_state.history.system("Return answer to the user in markdown:")
        response_stream = llm_stream(st.session_state.history)
        answers = process_stream(response_stream)
        chunk = ""
        for chunk in answers:
            assistant_text.markdown(chunk)  # Update progressively
        st.session_state.history.assistant(chunk)  # Save final message in history


def streaming_interface(company_name: str, question=None):
    st.title(f"{company_name} GPT")

    # Display all previous messages
    for message in st.session_state.history.logs:
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_prompt = st.chat_input()  # Input box for the user
    if user_prompt is not None:
        question = user_prompt

    if question:
        ask_question(question)
