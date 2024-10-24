from fastapi import FastAPI

from chain import chain

app = FastAPI()

@app.get("/generate")
def generate(text: str) -> str:
    try:
        return chain.invoke({"input": text})
    except ValueError as error:
        return str(error)