import json

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter  
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate

from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.tools.render import format_tool_to_openai_function

from logger import logger
from datasets import Dataset
import random
import docx

import weaviate
from dotenv import load_dotenv,find_dotenv
from weaviate.embedded import EmbeddedOptions

from ragas import evaluate
from ragas.metrics import ( faithfulness, answer_relevancy, context_recall, context_precision)

from chunking import ChunkingStrategy, Chunking

 
# Load OpenAI API key from .env file
load_dotenv(find_dotenv())


class LangchainPipeline:
    def __init__(self, database, embedding_type):
        self.retriver = None
        self.chunking_strategy = Chunking(ChunkingStrategy.NAIVE)
        self.knowledge_sources = []
    
        pass


    

def read_questions_answers(file_path: str) -> tuple[list[str], list[str]]:
    """
    Read questions and answers from a text file and return them as two separate lists.

    Args:
        file_path (str): The file path of the input text file.

    Returns:
        tuple[list[str], list[str]]: A tuple containing two lists - one for questions and one for answers.
    """
    questions = []
    answers = []

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].startswith("Q"):
                    question = lines[i].split(": ", 1)[-1].strip()  # Remove initials
                    answer = lines[i+1].split(": ", 1)[-1].strip()  # Remove initials
                    questions.append(question)
                    answers.append(answer)
                    i += 2
                else:
                    i += 1

    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'")
        return [], []

    return questions, answers


def convert_docx_to_txt(docx_file_path: str) -> str:
    """
    Convert a DOCX file to a TXT file.

    Args:
        docx_file_path (str): The file path of the input DOCX file.

    Returns:
        str: The file path of the output TXT file.

    Raises:
        Exception: If an error occurs during the conversion process.
    """
    try:
        # Read content from DOCX file
        doc = docx.Document(docx_file_path)
        text_content = ""
        for paragraph in doc.paragraphs:
            text_content += paragraph.text + "\n"

        # Extract the file name and directory path
        file_name = docx_file_path.split("/")[-1].split(".")[0]
        directory_path = "/".join(docx_file_path.split("/")[:-1])

        # Write content to TXT file
        txt_file_path = f"{directory_path}/{file_name}.txt"
        with open(txt_file_path, "w") as txt_file:
            txt_file.write(text_content)

        logger.info(f"Successfully converted {docx_file_path} to TXT format.")
        return txt_file_path

    except Exception as e:
        logger.error(f"Error occurred while converting {docx_file_path} to TXT: {e}")
        return ""



def create_langchain_pipeline(retriever, template, temperature=0):
    try:

        tool_functions = list(map(format_tool_to_openai_function, []))

        # Define LLM
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temperature)

        llm = ChatOpenAI(temperature=0.1, model = 'gpt-4-1106-preview')\
            .bind(functions = tool_functions)


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
        chunks = create_chunks()
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
