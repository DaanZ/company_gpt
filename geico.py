
import streamlit as st

from chatgpt import llm_chat
from loader import load_knowledge_logs

company_name = "Geico"
st.set_page_config(
    page_title=f"{company_name} GPT",
    page_icon="🦎",
    layout="wide"
)

st.title(f"{company_name} Marketing GPT")

# check for messages in session and create if not exists
if "history" not in st.session_state.keys():
    st.session_state.history = load_knowledge_logs("geico.json")
    st.session_state.history.system(f"""You are a very kindly and friendly marketing assistant for {company_name}. You are
    currently having a conversation with a marketing person. Answer the questions in a kind and friendly 
    with you being the expert for {company_name} to answer any questions about marketing.""")
    st.session_state.history.assistant("Hello there, how can I help you? 🦎")


# Display all messages
for message in st.session_state.history.logs:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.history.user(user_prompt)
    with st.chat_message("user"):
        st.write(user_prompt)

if st.session_state.history.logs[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            chat = llm_chat(st.session_state.history)
            st.write(chat)
    st.session_state.history.assistant(chat)
