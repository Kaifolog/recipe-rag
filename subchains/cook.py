from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from configs.llm import llm
from prompts.cook import cook_sys_prompt, modification_user_prompt, creation_user_prompt


def prompt_router(data):
    data.update(data["parser"])
    data["ingredients"] = "\n".join(
        ["- " + ingredient for ingredient in data["ingredients"]]
    )
    data["steps"] = "\n".join(["- " + step for step in data["steps"]])
    data["recommendations"] = "\n".join(
        [
            "- " + recommendation.metadata["recommendation"]
            for recommendation in data["recommendations"]
        ]
    )
    if data["topic"] == "модифікація":
        return ChatPromptTemplate.from_messages(
            [("system", cook_sys_prompt), ("user", modification_user_prompt)]
        )
    elif data["topic"] == "генерація":
        return ChatPromptTemplate.from_messages(
            [("system", cook_sys_prompt), ("user", creation_user_prompt)]
        )


recipe_cooking_subchain = RunnableLambda(prompt_router) | llm | StrOutputParser()
