import json

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter  
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate


from logger import logger
from datasets import Dataset
import random

import weaviate
from dotenv import load_dotenv,find_dotenv
from weaviate.embedded import EmbeddedOptions

from ragas import evaluate
from ragas.metrics import ( faithfulness, answer_relevancy, context_recall, context_precision)

 
# Load OpenAI API key from .env file
load_dotenv(find_dotenv())


def data_loader(file_path= '../prompts/context.txt', chunk_size=500, chunk_overlap=50):
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


def create_langchain_pipeline(retriever, template, temperature=0):
    try:
        # Define LLM
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temperature)

        # Define prompt template
        
        prompt = ChatPromptTemplate.from_template(template)

        # Setup RAG pipeline
        rag_chain = (
            {"context": retriever,  "question": RunnablePassthrough()} 
            | prompt 
            | llm
            | StrOutputParser() 
        )

        logger.info("langchain with rag pipeline created successfully.")
        return rag_chain

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 

def create_retriever(chunks):
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
            embedding = OpenAIEmbeddings(),
            by_text = False
        )

        retriever = vectorstore.as_retriever()
        logger.info("retriever create succesfully.")

        return retriever
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
  

def load_file(file_path):
    try:

        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the contents of the file
            file_contents = file.read()   
        
        return file_contents
        
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 
    

    

def ragas_evaulation(response):
    try:
        result = evaluate(
            dataset = response, 
            metrics=[
                context_precision,
                context_recall,
                faithfulness,
                answer_relevancy,
            ],
        )

        df = result.to_pandas()
        return df

      
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 






def get_generated_prompt_with_evaulation(question):
    try:
        chunks = data_loader()
        retriever = create_retriever(chunks)

        prompt_template = load_file('../prompts/prompt-generation-prompt.txt')
        prompt_rag_chain = create_langchain_pipeline(retriever, prompt_template)

        generated_prompts = prompt_rag_chain.invoke(question)
        prompt_list  = json.loads(generated_prompts)

        questions = [item['prompt'] for item in prompt_list]
        questions = [item['question'] for item in prompt_list]
        answers = [item['answer'] for item in prompt_list]
        contexts = [item['context'] for item in prompt_list]



        ground_truths = [[item['ground_truth']] for item in prompt_list]


        # response = generate_testcase_and_context(questions, ground_truths, retriever, evaulation_rag_chain)

              
        data = {
            "question": questions, # list 
            "answer": answers, # list
            "contexts": contexts, # list list
            "ground_truths": ground_truths # list Lists
        }


        # Convert dict to dataset
        dataset = Dataset.from_dict(data)

        df = ragas_evaulation(dataset)

        return df
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 
