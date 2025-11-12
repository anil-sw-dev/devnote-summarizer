import os
from dotenv import load_dotenv
from langchain_classic.chains.llm import LLMChain
from langchain_classic.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm_api_key= os.getenv("GOOGLE_API_KEY")

prompt_template= PromptTemplate(
    input_variables=["note"],
    template='''
You are an helpful assistant for developers.
Summarize the following note and extract any TODOs or action items.
Note:
{note}
Summary:
'''
)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
summarize_chain=prompt_template | llm #LLMChain(llm,prompt=prompt_template)