from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter  
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain.text_splitter import RecursiveCharacterTextSplitter

from logger import logger
from dotenv import load_dotenv,find_dotenv

 
# Load OpenAI API key from .env file
load_dotenv(find_dotenv())


class ChunkingStrategy:
    def __init__(self, chunking_strategy):
        self.chunking_strategy = chunking_strategy
        self.chunking_pairs  = {
            "NAIVE": self.naive_chuncking,
            "SEMANTIC": self.semantic_chunking,
            "RECURSIVE": self.recursive_chuncking
        }
        pass

    def chunk_data(self, file_path):
        return self.chunking_pairs[self.chunking_strategy](file_path)

    def change_chunking_strategy(self, chunking_strategy):
        self.chunking_strategy = chunking_strategy

    
    def naive_chuncking(self, file_path: str, chunk_size:int=500, chunk_overlap:int=50):
        try:
            loader = TextLoader(file_path)
            documents = loader.load()

            # Chunk the data
            text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            chunks = text_splitter.split_documents(documents)
            
            logger.info("data loaded to vector database successfully")
            return chunks
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None
    
    def recursive_chuncking(self, file_path: str, chunk_size:int=500, chunk_overlap:int=50):
        try:


            with open(file_path) as f:
                text = f.read()
         

            # Chunk the data
            text_splitter = RecursiveCharacterTextSplitter(
                # Set a really small chunk size, just to show.
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                length_function=len,
                is_separator_regex=False,
            )
            chunks = text_splitter.create_documents([text])

            
            logger.info("data loaded to vector database successfully")
            return chunks
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None
    
    def semantic_chunking(self, file_path, chunk_size=1000, chunk_overlap=200, model_name="allenai/longformer-base-4k"):
        """
        Performs semantic chunking on a given text using Langchain.

        Args:
        file_path: the path of file to be chuncked.
        chunk_size: The maximum size of each chunk (in characters).
        chunk_overlap: The amount of overlap between chunks (in characters).
        model_name: The name of the pre-trained language model to use for
            semantic similarity calculations.

        Returns:
        A list of semantically meaningful chunks.
        """

        try:
            with open(file_path) as f:
                text = f.read()

            text_splitter = SemanticChunker(OpenAIEmbeddings())
            chunks = text_splitter.create_documents([text])

            return chunks
    
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None

