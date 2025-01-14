from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

helsinki_model_family = 'Helsinki-NLP/opus-mt-'
def text_translate_model(lang=[]):
    helsinki_model = f"{helsinki_model_family}{lang[0]}-{lang[1]}"
    translation_model = pipeline('translation', model=helsinki_model)
    return HuggingFacePipeline(pipeline=translation_model)