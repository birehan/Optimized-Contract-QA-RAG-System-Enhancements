

from databases import VectorStore, VectorStoreFactory
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from langchain.memory import ConversationTokenBufferMemory
from logger import logger
from dotenv import load_dotenv,find_dotenv

from chunking import ChunkingStrategy, Chunking
from data_extractor import DataExtractor
from retrivers import RetrieverFactory, RetrieverType

# Load OpenAI API key from .env file
load_dotenv(find_dotenv())

class RagPipeline:
    def __init__(self, 
                 template_file_path="../prompts/system_message.txt",
                 vector_store:VectorStore=VectorStore.CHROMA,
                 retrieve_type:RetrieverType=RetrieverType.VECTOR_STORE_BACKED,
                 chunking_strategy:ChunkingStrategy=ChunkingStrategy.SEMANTIC
                 ):
        
        self.template = DataExtractor.extract_data(template_file_path)
        self.vectorstore_factory = VectorStoreFactory()
        self.vectorstore = self.vectorstore_factory.create_vectorstore(chunks=[], vector_store=vector_store)
        self.retriver_factory = RetrieverFactory()
        self.retriever = self.retriver_factory.create_retriver(vector_store= self.vectorstore, retrieve_type=retrieve_type)
        self.chunking_tool = Chunking(chunking_strategy=chunking_strategy)
        self.data_sources = {}
        self.executor = self.get_rag_chain()
    

    def add_datasource(self, file_path):
        try:
            chunks = self.chunking_tool.chunk_data(file_path)

            if chunks:
                ids = self.retriever.add_documents(chunks)
                self.data_sources[file_path] = ids
                logger.info("Data source added to the system successfully")
            else:
                logger.info("do data to add")
        
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None 
        
    def remove_datasource(self, file_path):
        try:
            if file_path in self.chunks: 
                ids = self.chunks[file_path]
                self.vectorstore.delete(ids)
                del self.data_sources[file_path]
                logger.info("Data source removed from the system successfully")
            else:
                logger.info("no data with the given path to remove")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None 
        
    def get_rag_chain(self):
        try:

            # tool_functions = list(map(format_tool_to_openai_function, []))

            # Define LLM
            llm = ChatOpenAI(temperature=0.1, model = 'gpt-4-1106-preview')
            
                # \
                # .bind(functions = tool_functions)
            
            memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=50)
            memory.load_memory_variables({})
            
            # Define prompt template
            
            system_message_prompt = SystemMessagePromptTemplate.from_template(self.template)
            human_message_prompt = HumanMessagePromptTemplate.from_template("{question}")


         

            memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
            conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=self.retriever,
            memory=memory,
            combine_docs_chain_kwargs={
                "prompt": ChatPromptTemplate.from_messages(
                    [
                        system_message_prompt,
                        human_message_prompt,
                    ]
                ),
            },
            )

            logger.info("langchain with rag pipeline created successfully.")
            return conversation_chain

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None 
