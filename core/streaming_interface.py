import os

import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from pydantic import Field, BaseModel

from core.chatgpt import llm_stream, process_stream, llm_strict
from core.files import json_write_file, json_read_file
from core.history import History


def ask_question(user_prompt: str):
    st.session_state.conversation.user(user_prompt)
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
            st.session_state.conversation.system(response.page_content)
        st.session_state.conversation.system("Return answer to the user in markdown:")
        response_stream = llm_stream(st.session_state.conversation)
        answers = process_stream(response_stream)
        chunk = ""
        for chunk in answers:
            assistant_text.markdown(chunk)  # Update progressively
        st.session_state.conversation.assistant(chunk)  # Save final message in history
    return chunk


class TitleConversationModel(BaseModel):
    title: str = Field(..., description="Short title of the conversation so far.")


def streaming_interface(company_name: str, question=None):
    st.title(f"{company_name} GPT")

    # Display all previous messages
    for message in st.session_state.conversation.logs:
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_prompt = st.chat_input()  # Input box for the user
    if user_prompt is not None:
        question = user_prompt

    if question:

        chunk = ask_question(question)
