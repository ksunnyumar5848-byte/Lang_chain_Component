import os
import sys

from dotenv import load_dotenv

from langchain_core.messages import HumanMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

def main():
    load_dotenv()
    api_key=os.getenv("GEMINI_API_KEY","")
    modal_name=os.getenv("GEMINI_API_MODAL","gemini-3.7-flash")

    if not api_key:
        sys.exit("you have not api key please ..... add the api key  in your .env file")

    if not modal_name:
        sys.exit("you have not modal name please ... add the api modal in your .env file")

    modal=ChatGoogleGenerativeAI(model=modal_name,api_key=api_key,temperature=0)

    msg=[
        SystemMessage(content="You are a patient Python tutor answer in one sort "),
        HumanMessage(content="what are the python variable ")
    ]

    response=modal.invoke(msg)

    print(f"modal:{modal_name}")
    print(f"response {response.text()}")

if __name__=="__main__":
    main()