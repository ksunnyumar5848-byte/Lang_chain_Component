import sys
import os

from typing import Literal
from dotenv import load_dotenv
from pydantic import BaseModel ,Field ,ValidationError
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


class StudyNotes(BaseModel):
    topic:str=Field(description="Topic name in few words ")
    summary:str=Field(description="One sentance for biggner can undestand ")
    diffculity:Literal["biginner","entermidate","Advance"]=Field(description="how hard for this new programming languange ")


def main():

    load_dotenv()

    api_key=os.getenv("GEMINI_API_KEY","")
    modal_name=os.getenv("GEMINI_API_MODAL","gemini-2.5-flash")

    if not api_key:
        sys.exit("you have not api key in your the .env file please add the api key bro .....")

    if not modal_name:
        sys.exit("you have not modal name in your .env file please add the modal name  bro .....")

    modal=ChatGoogleGenerativeAI(model=modal_name, api_key=api_key)

    structure_modal=modal.with_structured_output(StudyNotes)
    result=structure_modal.invoke("explain a varible for python ")


    print("Topic ",result.topic)
    print("summary",result.summary)
    print("difficulty",result.diffculity)


if __name__=="__main__":
    main()


