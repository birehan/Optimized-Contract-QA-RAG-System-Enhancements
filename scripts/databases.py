from langchain_community.vectorstores import Milvus
from dotenv import load_dotenv,find_dotenv
from langchain_openai import OpenAIEmbeddings
from logger import logger

import weaviate
from weaviate.embedded import EmbeddedOptions
from langchain.vectorstores import Weaviate

# from langchain_community.embeddings import Embeddings
from langchain_community.vectorstores import Milvus
from langchain_community.vectorstores import Pinecone

from enum import Enum
import os


class VectorStore(Enum):
    MILVUS = "milvus"
    WEAVIATE = "weaviate"
    PINECONE = "pinecone"

class RetrieverFactory:
    def __init__(self):
        # Load OpenAI API key from .env file
        load_dotenv(find_dotenv())
        

    def create_retriever(self, chunks,  vector_store: VectorStore=VectorStore.MILVUS, embedding=OpenAIEmbeddings()):
        try:
            if vector_store == VectorStore.MILVUS:
                return self._create_milvus_retriever(chunks, embedding)
            elif vector_store == VectorStore.WEAVIATE:
                return self._create_weaviate_retriever(chunks, embedding)
            elif vector_store == VectorStore.PINECONE:
                return self._create_pinecone_retriever(chunks, embedding)
            else:
                logger.error("Invalid vector store type provided.")
                return None
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None

    def _create_milvus_retriever(self, chunks, embedding):
        vectorstore = Milvus.from_documents(chunks, embedding)
        retriever = vectorstore.as_retriever()
        logger.info("Milvus retriever created successfully.")
        return retriever
    
    def _create_weaviate_retriever(self, chunks, embedding):
        client = weaviate.Client(embedded_options=EmbeddedOptions())
        vectorstore = Weaviate.from_documents(client=client, documents=chunks, embedding=embedding, by_text=False)
        retriever = vectorstore.as_retriever()
        logger.info("Weaviate retriever created successfully.")
        return retriever
    
    def _create_pinecone_retriever(self, chunks, embedding):
        index_name = os.getenv("PINECONE_INDEX_NAME")
        vectorstore = Pinecone.from_documents(documents=chunks, embedding=embedding, index_name=index_name)
        retriever = vectorstore.as_retriever()
        logger.info("Pinecone retriever created successfully.")
        return retriever




def milvus_retriver(chunks, embedding):
    try:
        # Load OpenAI API key from .env file
        load_dotenv(find_dotenv())

        vectorstore = Milvus.from_documents(
            chunks,
            embedding,
            # connection_args={"host": "192.168.137.236", "port": "19530"},
        )
                
        retriever = vectorstore.as_retriever()
        logger.info("retriever create succesfully.")

        return retriever
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

    
def weaviate_retriever(chunks, embedding):
    try:
        # Load OpenAI API key from .env file
        load_dotenv(find_dotenv())

        client = weaviate.Client(
            embedded_options = EmbeddedOptions()
        )
        # Populate vector database
        vectorstore = Weaviate.from_documents(
            client = client,    
            documents = chunks,
            embedding = embedding,
            by_text = False
        )

        retriever = vectorstore.as_retriever()
        logger.info("retriever create succesfully.")

        return retriever
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")


def pinecone_retriever(chunks, embedding):
    try:
        # Load OpenAI API key from .env file
        load_dotenv(find_dotenv())
        index_name = "contract-rag"


        # Populate vector database
        vectorstore = Pinecone.from_documents(
            documents = chunks,
            embedding = embedding,
            index_name = index_name
           
        )

        retriever = vectorstore.as_retriever()
        logger.info("retriever create succesfully.")

        return retriever
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")