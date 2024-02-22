import json

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter  
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate


from langchain.llms import AutoChain
from langchain.llms import AutoModelForSeq2SeqLM
from langchain.llms import SentenceSplitter
from langchain.llms import SemanticChunker



from logger import logger
from datasets import Dataset
import random
import docx

import weaviate
from dotenv import load_dotenv,find_dotenv
from weaviate.embedded import EmbeddedOptions

from ragas import evaluate
from ragas.metrics import ( faithfulness, answer_relevancy, context_recall, context_precision)

 
# Load OpenAI API key from .env file
load_dotenv(find_dotenv())


class ChunkingStrategy:
    def __init__(self, chunking_strategy):
        self.chunking_strategy = chunking_strategy
        self.chunking_pairs  = {
            "Naive": self.naive_chuncking
        }
        pass
    
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
    
    def semantic_chunking(file_path, chunk_size=1000, chunk_overlap=200, model_name="allenai/longformer-base-4k"):
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

            # Load the language model
            model = AutoChain.from_pretrained(model_name)

            # Load the sentence splitter
            sentence_splitter = SentenceSplitter()

            # Load the semantic chunker
            chunker = SemanticChunker(
                model=model,
                sentence_splitter=sentence_splitter,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )

            # Chunk the text
            chunks = chunker(text)

            return chunks
    
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None






class LangchainPipeline:
    def __init__(self, database, embedding_type):
        self.retriver = None
        self.chunking_strategy = ChunkingStrategy("Naive")
        self.knowledge_source = []
    
        pass


    def create_chunks(file_path: str, chunk_size:int=500, chunk_overlap:int=50):
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
