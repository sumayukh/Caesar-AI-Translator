from dotenv import load_dotenv
import os

#load env variables
load_dotenv()

LANGCHAIN_PROJECT = os.getenv('LANGCHAIN_PROJECT')
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
LANGCHAIN_ENDPOINT = os.getenv('LANGCHAIN_ENDPOINT')
LANGCHAIN_TRACING_V2 = os.getenv('LANGCHAIN_TRACING_V2', 'False').lower() in ('true', '1')
