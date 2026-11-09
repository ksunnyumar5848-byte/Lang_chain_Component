import os
import sys

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

def main():
    load_dotenv()
    api_key=os.getenv("GEMINI_API_KEY","")
    model_name=os.getenv("GEMINI_API_MODAL","gemini-2.5-flash")


    if not api_key:
        sys.exit("you have not api please ..... add api key in your .env file")

    if not model_name:
        sys.exit("you have not model please... add the model in your .env file ")


    question=[
        HumanMessage(content="explain a list in the python in one line ")
    ]

    focused=ChatGoogleGenerativeAI(model=model_name,api_key=api_key,temperature=0,max_tokens=50)
    Creative=ChatGoogleGenerativeAI(model=model_name,api_key=api_key,temperature=0.9,max_tokens=50)

    print(f"temperature :0 , max_tokens=50")
    print(focused.invoke(question).content)

    print("temperature : 0.9, max_tokens=50")
    print(Creative.invoke(question).content)




if __name__=="__main__":
    main()



