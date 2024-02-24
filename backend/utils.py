import os
import sys

sys.path.append(os.path.abspath(os.path.join('../scripts')))

from chunking import Chunking, ChunkingStrategy
from databases import VectorStoreFactory, VectorStore
from embedding import EmbeddingFactory, EmbeddingType
from memory import MemoryFactory, MemoryType
from retrivers import RetrieverFactory, RetrieverType
from rag_pipeline import RagPipeline

def get_rag_options():
    return [
        Chunking.list_supported_chunkings(),
        VectorStoreFactory.list_supported_vectorStores(),
        EmbeddingFactory.list_supported_embeddings(),
        MemoryFactory.list_supported_memory_types(),
        RetrieverFactory.list_supported_retrivers()
    ]

def create_rag_pipeline(data):

    chunking_strategy = ChunkingStrategy[data['chunking']]
    embedding_model = EmbeddingType[data['embedding']]
    memory_type = MemoryType[data['memoryType']]
    retriever_type = RetrieverType[data['retrieverType']]
    vector_store = VectorStore[data['vectorStore']]

    # Creating RagPipeline object
    rag_pipeline = RagPipeline(
        chunking_strategy=chunking_strategy,
        embedding_model=embedding_model,
        memory_type=memory_type,
        retrieve_type=retriever_type,
        vector_store=vector_store
        )

    print(type(rag_pipeline))
    
    return rag_pipeline




