import sys
import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

PROVIDER="gemini"

QUESTION="sey hello  word in one sentence  "

def main():
    load_dotenv()

    provider=PROVIDER.strip().lower()

    print("how use the multiple proivder")
    print(f" hello bro my provider : {provider}")
    print("multiple provider gemini or enthropic ollama  or openAI")


    if provider=="gemini":
        api_key=os.getenv("GEMINI_API_KEY","")
        model_name=os.getenv("GEMINI_API_MODAL","gemini-3.7-flash")

        if not api_key:
            sys.exit("you hav not api key in your .env file please .... add the api key ")
        if not model_name:
            sys.exit("you have not the model name in your .env file please add the model name ....")    


        model=ChatGoogleGenerativeAI(model=model_name,api_key=api_key,temperature=0)    



