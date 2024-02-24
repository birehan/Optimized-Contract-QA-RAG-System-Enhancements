from chunking import Chunking
from databases import VectorStoreFactory
from embedding import EmbeddingFactory
from memory import MemoryFactory
from retrivers import RetrieverFactory
from logger import logger
import docx
from dotenv import load_dotenv,find_dotenv
from chunking import  Chunking
from data_extractor import DataExtractor

# Load OpenAI API key from .env file
load_dotenv(find_dotenv())

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


def get_rag_options():
    return [
        Chunking.list_supported_chunkings(),
        VectorStoreFactory.list_supported_vectorStores(),
        EmbeddingFactory.list_supported_embeddings(),
        MemoryFactory.list_supported_memory_types(),
        RetrieverFactory.list_supported_retrivers()
    ]


def extract_qa_dataset(question_ans_path):
    try:
        extracted_text = DataExtractor.extract_data(question_ans_path)
        
        blocks = extracted_text.split('\n')

        questions = []
        answers = []

        i = 0
        while i < len(blocks):
            blocks[i] = blocks[i].strip()
            if blocks[i].startswith("Q"):
                question = blocks[i].split(": ", 1)[-1].strip()  # Remove initials
                answer = blocks[i+1].split(": ", 1)[-1].strip() # Remove initials
                questions.append(question)
                answers.append(answer)
                i += 2
            else:
                i += 1
    
        return questions, answers
        
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")


def extract_and_optimize_qa_dataset(question_ans_path, optimized_questions):
    try:
        extracted_text = DataExtractor.extract_data(question_ans_path)
        
        blocks = extracted_text.split('\n')

        questions = []
        answers = []

        i = 0
        while i < len(blocks):
            blocks[i] = blocks[i].strip()
            if blocks[i].startswith("Q"):
                question = optimized_questions.pop(0)  # Pop the next optimized question
                answer = blocks[i+1].split(": ", 1)[-1].strip() # Remove initials
                questions.append(question)
                answers.append(answer)
                i += 2
            else:
                i += 1
        
        # Save the optimized dataset
        optimized_file_path = question_ans_path.replace('.docx', '_optimized_questions.txt')
        with open(optimized_file_path, 'w') as f:
            for q, a in zip(questions, answers):
                f.write(f"Q: {q}\n")
                f.write(f"A: {a}\n")
        
        return optimized_file_path
        
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
