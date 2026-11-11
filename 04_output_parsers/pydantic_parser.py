import sys
import os

from typing import Literal
from dotenv import load_dotenv
from pydantic import BaseModel ,Field ,ValidationError
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv