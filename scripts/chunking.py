from langchain.text_splitter import CharacterTextSplitter  
from langchain_experimental.text_splitter import SemanticChunker
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings

from logger import logger
from dotenv import load_dotenv,find_dotenv
from enum import Enum
from data_extractor import DataExtractor
from data_cleaning import DataCleaner

class ChunkingStrategy(Enum):
    SEMANTIC = "Semantic"
    NAIVE = "Naive"
    RECURSIVE = "Recursive"

# Load OpenAI API key from .env file
load_dotenv(find_dotenv())

class Chunking:
    def __init__(self, chunking_strategy=ChunkingStrategy.SEMANTIC):
        if chunking_strategy not in ChunkingStrategy:
            raise ValueError("Invalid chunking strategy. Please use a valid ChunkingStrategy enum value.")
        self.chunking_strategy = chunking_strategy

        self.chunking_methods = {
            ChunkingStrategy.NAIVE: self.naive_chunking,
            ChunkingStrategy.SEMANTIC: self.semantic_chunking,
            ChunkingStrategy.RECURSIVE: self.recursive_chunking
        }
        self.data_extract_tool = DataExtractor()

    def chunk_data(self, file_path):
        try:
            chunking_method = self.chunking_methods[self.chunking_strategy]
            return chunking_method(file_path)
        except KeyError:
            logger.error(f"Chunking strategy '{self.chunking_strategy}' is not implemented.")
            return None
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None
        

    def change_chunking_strategy(self, chunking_strategy):
        if chunking_strategy not in ChunkingStrategy:
            raise ValueError("Invalid chunking strategy. Please use a valid ChunkingStrategy enum value.")
        self.chunking_strategy = chunking_strategy

    
    def naive_chunking(self, file_path: str, chunk_size:int=500, chunk_overlap:int=50):
        try:
            
            text = self.data_extract_tool.extract_data(file_path)
            # cleaned_text = DataCleaner.clean_text(text)

            # Chunk the data
            text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            chunks = text_splitter.create_documents([text])
            
            logger.info("data loaded to vector database successfully")
            return chunks
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None
    
    def recursive_chunking(self, file_path: str, chunk_size:int=500, chunk_overlap:int=50):
        try:


            text = self.data_extract_tool.extract_data(file_path)
            # cleaned_text = DataCleaner.clean_text(text)

            # Chunk the data
            text_splitter = RecursiveCharacterTextSplitter(
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
    
    def semantic_chunking(self, file_path):
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
            text = self.data_extract_tool.extract_data(file_path)
            # cleaned_text = DataCleaner.clean_text(text)


            text_splitter = SemanticChunker(OpenAIEmbeddings())
            chunks = text_splitter.create_documents([text])

            return chunks
    
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None
    

    @staticmethod
    def list_supported_chunkings():
        """
        """

        return {
            "items": [{"key": enum_type.name, "value":enum_type.value } for enum_type in ChunkingStrategy],
            "name": "chunking",
            "label": "Chunking Strategies"
        }



