
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline
from utils.embeddings import setup_embedding_retriever

def answer_question(query, text):
    doc_store, retriever = setup_embedding_retriever(text)
    reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)
    pipe = ExtractiveQAPipeline(reader, retriever)
    res = pipe.run(query=query, params={"Retriever":{"top_k":5},"Reader":{"top_k":1}})
    if res["answers"]:
        ans = res["answers"][0].answer
        ctx = res["answers"][0].context
        return ans, ctx
    return "No answer found.",""
