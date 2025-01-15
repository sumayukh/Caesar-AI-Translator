from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from .helsinki import text_translate_model
#from src.models.helsinki.helsinki import text_translate_model

def prompt_template_init():
    return PromptTemplate(template="{input}")

def llmchain_init(lang=[]):
    translator = text_translate_model(lang)
    prompt_template = prompt_template_init()
    return LLMChain(llm=translator, prompt=prompt_template)