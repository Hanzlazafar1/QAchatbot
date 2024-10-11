from langchain_community.llms import Ollama 
from  langchain.prompts import ChatPromptTemplate #  when we are using the anyother thirdparty in langchain it is in langchain_community
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()


os.environ["Langchain_tracing_v2"]="True"


prompt=ChatPromptTemplate.from_messages(
    [
        ("System","You are helpul assistant.Please response to user queries")
        ("User","Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain demo With openai api")
input_text=st.text_input("Search the topic u want")



# ollama llm
llm=Ollama(model="llama2") 
#first download the llama2 model on the loacla device from the ollama 
#ollama run gemma
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))