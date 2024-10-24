from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.output_parsers import JsonOutputParser

from pydantic import BaseModel, Field
from typing import List

from configs.llm import llm
from prompts.parser import parser_prompt


class Recipe(BaseModel):
    title: str = Field(description="назва рецепту")
    ingredients: List[str] = Field(description="інгредієнти для рецепту")
    steps: List[str] = Field(description="кроки виконання рецепту")


parser = JsonOutputParser(pydantic_object=Recipe)

parser_subchain = (
    ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(
                template=parser_prompt,
                partial_variables={
                    "format_instructions": parser.get_format_instructions()
                },
            ),
            HumanMessagePromptTemplate.from_template(
                template="""Текст рецепта: "{recipe}" """, input_variables=["recipe"]
            ),
        ]
    )
    | llm
    | parser
)
