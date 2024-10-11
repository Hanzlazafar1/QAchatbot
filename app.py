from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os 
from dotenv import load_dotenv

os.environ["openaiapi"]=os.getenv("openaiapi")
os.environ["Langchain_tracing_v2"]="True"
os.environ["langchainapi"]=os.getenv("langchainapi")

#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("System","You are helpul assistant.Please response to user queries")
        ("User","Question:{question}")
    ]
)
## streamlit framework
st.title("Langchain demo With openai api")
input_text=st.text_input("Search the topic u want")

# openai llm
llm=ChatOpenAI(model="gpt-3.5-turbo")

output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))