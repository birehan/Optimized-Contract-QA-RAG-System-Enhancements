

from dotenv import load_dotenv,find_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from logger import logger

import weaviate
from weaviate.embedded import EmbeddedOptions

from langchain_community.vectorstores import Weaviate
from langchain_community.vectorstores import Milvus
from langchain_community.vectorstores import Pinecone
from langchain_community.vectorstores import Chroma

from enum import Enum
import os

class VectorStore(Enum):
    CHROMA = "Chroma"
    MILVUS = "Milvus"
    WEAVIATE = "Weaviate"
    PINECONE = "Pinecone"

class VectorStoreFactory:
    def __init__(self):
        # Load OpenAI API key from .env file
        load_dotenv(find_dotenv())
        
    def create_vectorstore(self, chunks=[],  vector_store: VectorStore=VectorStore.MILVUS, embedding=OpenAIEmbeddings()):
        try:
            if vector_store == VectorStore.MILVUS:
                return self._create_milvus_vectorstore(chunks, embedding)
            elif vector_store == VectorStore.WEAVIATE:
                return self._create_weaviate_vectorstore(chunks, embedding)
            elif vector_store == VectorStore.PINECONE:
                return self._create_pinecone_vectorstore(chunks, embedding)
            elif vector_store == VectorStore.CHROMA:
                return self._create_chroma_db_vectorstore(chunks, embedding)
            else:
                logger.error("Invalid vector store type provided.")
                return None
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None

    def _create_milvus_vectorstore(self, chunks, embedding):
        vectorstore = Milvus.from_documents(chunks, embedding)
        logger.info("Milvus vectorstore created successfully.")
        return vectorstore
    
    def _create_weaviate_vectorstore(self, chunks, embedding):
        client = weaviate.Client(embedded_options=EmbeddedOptions())
        vectorstore = Weaviate.from_documents(client=client, documents=chunks, embedding=embedding, by_text=False)
        logger.info("Weaviate vectorstore created successfully.")
        return vectorstore
    
    def _create_pinecone_vectorstore(self, chunks, embedding):
        index_name = os.getenv("PINECONE_INDEX_NAME")
        vectorstore = Pinecone.from_documents(documents=chunks, embedding=embedding, index_name=index_name)
        logger.info("Pinecone vectorstore created successfully.")
        return vectorstore
    
    def _create_chroma_db_vectorstore(self, chunks, embedding):
        # Assuming you have a ChromaDB client instance already created
        vectorstore = Chroma(embedding_function=embedding)
        logger.info("ChromaDB vectorstore created successfully.")
        return vectorstore

    @staticmethod
    def list_supported_vectorStores():
        """
        """
        return {
            "items": [{"key": enum_type.name, "value":enum_type.value } for enum_type in VectorStore],
            "name": "vectorStore",
            "label": "VectorStore Databases"
        }