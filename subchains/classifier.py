from configs.llm import classifier_llm

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts.classifier import classifier_prompt

classifier_subchain = (
    ChatPromptTemplate.from_messages(
        [("system", classifier_prompt), ("user", """Текст запиту: "{input}" """)]
    )
    | classifier_llm
    | StrOutputParser()
)
