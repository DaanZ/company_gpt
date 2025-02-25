import uuid
from datetime import datetime
import os

import rootpath
import streamlit as st

from core.files import json_write_file
from core.loader import load_executive, read_pdfs, json_read_file, load_knowledge, load_knowledge_pages
from core.streaming_interface import streaming_interface
from core.vault.conversation import Conversation


def start_stream(submitted):
    print(submitted)


def start_interface(company_name: str):
    # Center everything with custom CSS
    st.session_state.initial = st.container()
    with st.session_state.initial:
        st.title("")
        st.title(f"{company_name} GPT")
        st.markdown(
            f"""
            <style>
            .container {{
                display: flex;
                justify-content: left;
                align-items: center;
            }}
            .content {{
                text-align: left;
                width: 100%;
            }}
            div[data-testid="stChatInput"] textarea {{
                height: 100px !important;
            }}
            </style>
            <div class="container">
                <div class="content">
                    <h3>How can I help you today?</h3>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Streamlit components within the centered content
        col1, col2 = st.columns([100, 1])
        with col1:
            answer = st.chat_input("Ask anything")
            print("answer", answer)
            return answer


def start_menu(company_name, company_id, system_prompt=None):
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    if "documents" not in st.session_state:
        st.session_state.path = os.path.join(rootpath.detect(), "data", f"{company_id}.json")
        # TODO differently reading documents
        st.session_state.documents = load_knowledge_pages(st.session_state.path)
        print(len(st.session_state.documents))

    if "conversation" not in st.session_state:
        answer = start_interface(company_name)
        if answer is not None:
            st.session_state.conversation = load_executive(st.session_state.path)
            if system_prompt:
                st.session_state.conversation.system(system_prompt)
            st.session_state.initial = st.empty()
            st.session_state.question = answer
            st.rerun()
    else:
        streaming_interface(company_name, st.session_state.question)
        st.session_state.question = None


if __name__ == "__main__":
    company_name = "360 Pet Nutrition"
    company_id = "360_pet_nutrition"
    start_menu(company_name, company_id)

