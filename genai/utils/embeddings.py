
from haystack.nodes import EmbeddingRetriever
from haystack.document_stores import InMemoryDocumentStore

def setup_embedding_retriever(text):
    ds = InMemoryDocumentStore()
    retr = EmbeddingRetriever(document_store=ds, embedding_model="sentence-transformers/all-MiniLM-L6-v2")
    docs = [{"content":para} for para in text.split("\n\n") if para.strip()]
    ds.write_documents(docs)
    ds.update_embeddings(retr)
    return ds, retr
