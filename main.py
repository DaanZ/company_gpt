import streamlit as st
from cto_toolshed.ai.documents.query import langchain_history
from cto_toolshed.ai.llm.history import History
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS

from company import openai_embeddings
from loader import load_knowledge_documents

company_name = "Geico"
st.set_page_config(
    page_title=f"{company_name} GPT",
    page_icon="🦎",
    layout="wide"
)

pages = load_knowledge_documents()
vectorstore = FAISS.from_documents(pages, openai_embeddings)
chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(temperature=0.0, model_name="gpt-4o"),
    retriever=vectorstore.as_retriever(),
)
print(len(pages))
st.title(f"{company_name} GPT")

# check for messages in session and create if not exists
if "history" not in st.session_state.keys():
    st.session_state.history = History()
    st.session_state.history.system(f"""You are a very kindly and friendly marketing assistant for {company_name} Athletics. You are
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

            logs = langchain_history(st.session_state.history)
            print({"question": user_prompt, "chat_history": st.session_state.history.logs})
            chat = chain.invoke({"question": user_prompt, "chat_history": logs})["answer"]
            st.write(chat)
    st.session_state.history.assistant(chat)