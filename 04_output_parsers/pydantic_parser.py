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


