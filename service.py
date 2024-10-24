from fastapi import FastAPI

from chain import chain

app = FastAPI()

@app.get("/generate")
def generate(text: str) -> dict:
    try:
        return {"responce": chain.invoke({"input": text})}
    except ValueError as error:
        return {"error": str(error)}
