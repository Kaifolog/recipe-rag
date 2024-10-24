from langchain_groq import ChatGroq

classifier_llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    )

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0.5,
    max_tokens=None,
    )