from ragas import evaluate
from logger import logger
import matplotlib.pyplot as plt
from embedding import EmbeddingFactory, EmbeddingType
from memory import MemoryType, MemoryFactory
from datasets import Dataset
from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    context_recall,
    context_precision,
    context_relevancy,
    answer_correctness,
    answer_similarity
)
from chunking import ChunkingStrategy
from databases import VectorStore
from retrivers import RetrieverType
from rag_pipeline import RagPipeline
from data_extractor import DataExtractor

class RagEvaluation:
    def __init__(self, 
                 context_path:str, 
                 question_ans_path:str,
                 template_file_path="../prompts/system_message.txt",
              

                vector_store:VectorStore=VectorStore.CHROMA,
                 retrieve_type:RetrieverType=RetrieverType.VECTOR_STORE_BACKED,
                 chunking_strategy:ChunkingStrategy=ChunkingStrategy.SEMANTIC,
                 embedding_model: EmbeddingType=EmbeddingType.OPENAI_EMBEDDING,
                 memory_type: MemoryType=MemoryType.CONVERSATION_BUFFER_WINDOW
                 
                 ):
        
        self.rag_chain = RagPipeline(
            template_file_path=template_file_path,
            vector_store=vector_store,
            retrieve_type=retrieve_type,
            chunking_strategy=chunking_strategy,
            embedding_model=embedding_model,
            memory_type=memory_type
        )
        
        self.rag_chain.add_datasource(context_path)
        self.questions, self.ground_truth = self.extract_qa_dataset(question_ans_path)
    

    def extract_qa_dataset(self, question_ans_path):
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
  
     

    def create_ragas_dataset(self):

        try:
            contexts = []
            answers = []

            for question in self.questions:
                contexts.append([docs.page_content for docs in self.rag_chain.retriever.get_relevant_documents(question)])
                answers.append(self.rag_chain.executor.invoke(question)["answer"])
                
            data = {
                "question": self.questions, # list 
                "answer": answers, # list
                "contexts": contexts, # list list
                "ground_truth": self.ground_truth # list Lists
            }

            dataset = Dataset.from_dict(data)
            return dataset
          
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
  

    def evaluate_dataset(self, ragas_dataset):
        result = evaluate(
            ragas_dataset,
            metrics=[
                context_precision,
                faithfulness,
                answer_relevancy,
                context_recall,
                context_relevancy,
                answer_correctness,
                answer_similarity
            ],
        )
        return result
    
    def plot_evaluation(self, metrics_dict, title='RAG Metrics'):
        try:
            """
            Plots a bar chart for metrics contained in a dictionary and annotates the values on the bars.
            Args:
            metrics_dict (dict): A dictionary with metric names as keys and values as metric scores.
            title (str): The title of the plot.
            """
            names = list(metrics_dict.keys())
            values = list(metrics_dict.values())
            plt.figure(figsize=(10, 6))
            bars = plt.barh(names, values, color='skyblue')
            # Adding the values on top of the bars
            for bar in bars:
                width = bar.get_width()
                plt.text(width + 0.01,  # x-position
                        bar.get_y() + bar.get_height() / 2,  # y-position
                        f'{width:.4f}',  # value
                        va='center')
            plt.xlabel('Score')
            plt.title(title)
            plt.xlim(0, 1)  # Setting the x-axis limit to be from 0 to 1
            plt.show()

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")