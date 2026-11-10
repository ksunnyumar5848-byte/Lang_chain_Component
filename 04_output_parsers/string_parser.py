import sys
import os
from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage


def main():

    parser = StrOutputParser()
    sample = AIMessage(content="A variable stores a value.")

    load_dotenv()

    api_key=os.getenv("GEMINI_API_KEY","")
    modal_name=os.getenv("GEMINI_API_MODAL","gemini-2.5-flash")
    
    if not api_key:
            sys.exit("you have not api key in your the .env file please add the api key bro .....")
    
    if not modal_name:
            sys.exit("you have not modal name in your .env file please add the modal name  bro .....")
    
    model=ChatGoogleGenerativeAI(model=modal_name, api_key=api_key)

    prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a patient Python tutor. Answer in one sentence."),
            ("human", "{question}"),
        ])

    chain = prompt | model | parser

    print("Chain result:", chain.invoke({"question": "What is a variable?"}))

if __name__ == "__main__":
    main() 


    

