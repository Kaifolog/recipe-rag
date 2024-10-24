from langchain_community.document_loaders import JSONLoader
from langchain_community.retrievers import BM25Retriever

def metadata_func(record: dict, metadata: dict) -> dict:
    metadata["key"] = record.get("key")
    metadata["recommendation"] = record.get("recommendation")
    return metadata

loader = JSONLoader(
    file_path='./data/replacements.json',
    jq_schema='.[]',
    content_key='.key',
    text_content=False,
    is_content_key_jq_parsable=True,
    metadata_func=metadata_func,
    )

documents = loader.load()

recommendations_retriever = BM25Retriever.from_documents(documents, k=5)
