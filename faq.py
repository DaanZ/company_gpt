from functools import partial

import streamlit as st
from pydantic import BaseModel, Field

from chatgpt import llm_strict
from loader import load_knowledge_logs
from streaming_interface import streaming_interface


class FAQQuestions(BaseModel):
    industry_question: str = Field(..., description="Question about the industry insights from the report")
    competitors_question: str = Field(..., description="Question about the competitors insights from the report")
    customer_question: str = Field(..., description="Question about the customer insights from the report")
    trends_question: str = Field(..., description="Question about the trends insights from the report")
    content_question: str = Field(..., description="Question about the content insights from the report")


def FAQ_interface(company_id, company_name, emoji):
    st.set_page_config(
        page_title=f"{company_name} GPT",
        page_icon=emoji,
        layout="wide"
    )
    if "first_run" not in st.session_state:
        st.session_state.first_run = False
        st.session_state.skip = False

    if "history" not in st.session_state:
        st.session_state.first_run = True
        st.session_state.history = load_knowledge_logs(company_name, f"data/{company_id}.json")
        st.session_state.history.system(
            f"""You are a very kindly and friendly marketing assistant for {company_name}. 
                        You are currently having a conversation with a marketing person. Answer the questions in a kind and friendly 
                        way, being the expert for {company_name} to answer any questions about marketing.""")
        st.session_state.history.assistant(f"Hello there, how can I help you? {emoji}\n")


        # Main program logic (call this function when you want to start the thread)
    if not st.session_state.skip:
        try:
            streaming_interface(company_name)
        except KeyboardInterrupt:
            print("Program interrupted.")
    else:
        st.session_state.skip = False

    if st.session_state.first_run:
        faq_model: FAQQuestions = llm_strict(st.session_state.history, base_model=FAQQuestions)
        st.markdown("We have prepared some frequently asked questions based on the report we generated:")
        st.button("**Industry:** " + faq_model.industry_question, on_click=partial(streaming_interface, company_name, faq_model.industry_question))
        st.button("**Competitors:** " + faq_model.competitors_question, on_click=partial(streaming_interface, company_name, faq_model.competitors_question))
        st.button("**Trends:** " + faq_model.trends_question, on_click=partial(streaming_interface, company_name, faq_model.trends_question))
        st.button("**Customer:** " + faq_model.customer_question, on_click=partial(streaming_interface, company_name, faq_model.customer_question))
        st.button("**Content:** " + faq_model.content_question, on_click=partial(streaming_interface, company_name, faq_model.content_question))
        st.session_state.first_run = False
        st.session_state.skip = True
