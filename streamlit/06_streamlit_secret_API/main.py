import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

st.title('🦜🔗 Quickstart App')
#openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
openai_api_key = st.secrets['OPENAI_API_KEY']

def generate_response(input_text):
    llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)
    prompt = PromptTemplate.from_template("Tell me something interesting about {topic}")
    chain = prompt | llm
    response = chain.invoke({"topic": input_text})
    st.info(response.content)

with st.form('my_form'):
    text = st.text_area('Enter text:', '....')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)