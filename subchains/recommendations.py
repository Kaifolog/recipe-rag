from langchain_core.runnables import RunnableLambda

from configs.bm25 import recommendations_retriever


def recomendations_for_itams(data):
    return recommendations_retriever.invoke(
        f"\"{data['parser']['title']}\": {data['recipe']}"
    )


recommendations_subchain = RunnableLambda(recomendations_for_itams)
