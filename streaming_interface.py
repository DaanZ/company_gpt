
import openai
import streamlit as st
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from chatgpt import llm_stream, process_stream
from history import History

chat = ChatOpenAI(model="gpt-4o")


def streaming_interface(company_name: str, emoji: str, history: History, optional: str = "", prompt=None, pages=None):
    st.set_page_config(
        page_title=f"{company_name} GPT",
        page_icon=emoji,
        layout="wide"
    )
    st.title(f"{company_name} Marketing GPT")

    # Initialize history if not already in session state
    if "history" not in st.session_state.keys():
        st.session_state.history = history
        if prompt is None:
            st.session_state.history.system(
                f"""You are a very kindly and friendly marketing assistant for {company_name}. 
            You are currently having a conversation with a marketing person. Answer the questions in a kind and friendly 
            way, being the expert for {company_name} to answer any questions about marketing.""")
        else:
            st.session_state.history.system(prompt)

        if optional:
            st.session_state.history.system(optional)
            with st.chat_message("system"):
                st.markdown(optional)

        st.session_state.history.assistant(f"Hello there, how can I help you? {emoji}\n")

    # Display all previous messages
    for message in st.session_state.history.logs:
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_prompt = st.chat_input()  # Input box for the user

    if user_prompt is not None:
        st.session_state.history.user(user_prompt)
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # Placeholder for the assistant's reply
        assistant_message_placeholder = st.chat_message("assistant")
        assistant_text = assistant_message_placeholder.empty()

        # Stream response
        with st.spinner("Loading..."):
            if pages:
                print("langchain")
                db = FAISS.from_documents(pages, OpenAIEmbeddings())
                for response in db.similarity_search(user_prompt, k=3):
                    print("article: " + response.page_content)
                    st.session_state.history.system(response.page_content)
                response_stream = llm_stream(st.session_state.history)
            else:
                response_stream = llm_stream(st.session_state.history)
            answers = process_stream(response_stream)
            chunk = ""
            for chunk in answers:
                assistant_text.markdown(chunk)  # Update progressively
            st.session_state.history.assistant(chunk)  # Save final message in history
