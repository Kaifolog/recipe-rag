from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import (
    RunnableLambda, 
    RunnableParallel, 
    RunnablePassthrough, 
)

from subchains.classifier import classifier_subchain
from subchains.parser import parser_subchain
from subchains.recommendations import recommendations_subchain
from subchains.cook import recipe_cooking_subchain

def classifier_route(data):
    if "модифікація" == data["topic"] or "генерація" == data["topic"]:
        return data
    else:
        raise ValueError("Stopping chain execution")

chain = {
    "topic": classifier_subchain, 
    "recipe": lambda x: x["input"]
    } | RunnableLambda(classifier_route) \
    | RunnablePassthrough.assign(parser=parser_subchain) \
    | RunnablePassthrough.assign(recommendations=recommendations_subchain) \
    | recipe_cooking_subchain
