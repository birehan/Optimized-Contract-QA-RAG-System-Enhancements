from dotenv import load_dotenv,find_dotenv







from logger import logger
from langchain.retrievers.multi_query import MultiQueryRetriever

from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import OpenAI
from langchain.retrievers import ParentDocumentRetriever
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.storage import InMemoryStore
from langchain_openai import ChatOpenAI

# from langchain_community.embeddings import Embeddings
# from langchain.retrievers import BM25Retriever, EnsembleRetriever

from enum import Enum

class RetrieverType(Enum):
    VECTOR_STORE_BACKED = "vector_store_backed"
    MULTIQUERY = "multiquery"
    CONTEXTUAL_COMPRESSION = "contextual_compression"
    ENSEMBLE_RETRIEVER = "ensemble_retriever"
    PARENT_DOCUMENT = "parent_document"
    

class RetrieverFactory:
    
    def __init__(self):
        # Load OpenAI API key from .env file
        load_dotenv(find_dotenv())
        
    def create_retriver(self, vector_store,  retrieve_type:RetrieverType=RetrieverType.VECTOR_STORE_BACKED):
        try:
            if retrieve_type == retrieve_type.VECTOR_STORE_BACKED:
                return self._create_vectorstore_backend_retriver(vector_store)
            elif retrieve_type == retrieve_type.MULTIQUERY:
                return self._create_multiquery_retriver(vector_store)
            elif retrieve_type == retrieve_type.CONTEXTUAL_COMPRESSION:
                return self._create_compression_retriver(vector_store),
            elif retrieve_type == retrieve_type.PARENT_DOCUMENT:
                return self._create_parent_document_retriver(vector_store)
            # elif vector_store == retriever.ENSEMBLE:
            #     return self._create_ensemble_retriver(chunks, vector_store)
            else:
                logger.error("Invalid vector store type provided.")
                return None
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None

    def _create_vectorstore_backend_retriver(self, vector_store):
        retriver = vector_store.as_retriever()
        logger.info("vectorstore_backend_retriver created successfully.")
        return retriver
    
    def _create_multiquery_retriver(self, vector_store):
        llm = ChatOpenAI(temperature=0)
        retriever = MultiQueryRetriever.from_llm(
            retriever = self._create_vectorstore_backend_retriver(vector_store), 
            llm=llm
        )
        logger.info("multiquery retriever created successfully.")
        return retriever 
    
    def _create_compression_retriver(self, vector_store):
        llm = OpenAI(temperature=0)
        compressor = LLMChainExtractor.from_llm(llm)
        retriever = ContextualCompressionRetriever(
            base_compressor=compressor, 
            base_retriever=self._create_vectorstore_backend_retriver(vector_store)
        )
       
        logger.info("contextual compression retriever created successfully.")
        return retriever
    
    def _create_parent_document_retriver(self, vector_store):
        child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)

        store = InMemoryStore()
        retriever = ParentDocumentRetriever(
        vectorstore=vector_store,
        docstore=store,
        child_splitter=child_splitter,
        )
       
        logger.info("parent document retriever created successfully.")
        return retriever
    
    # The storage layer for the parent documents

    # def _create_ensemble_retriver(self, chunks, vector_store):
    #     # Assuming you have a ChromaDB client instance already created
    #     bm25_retriever = BM25Retriever.from_documents(chunks)
    #     retriever = EnsembleRetriever(
    #     retrievers=[
    #             bm25_retriever,
    #             self._create_vectorstore_backend_retriver(vector_store)],
    #             weights=[0.5, 0.5]
    #         )
    #     logger.info("ensemble retriever created successfully.")
    #     return retriever