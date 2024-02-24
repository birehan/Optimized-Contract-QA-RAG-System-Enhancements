from flask import Blueprint, jsonify, request
import json
import logging
from docx import Document
from utils import get_rag_options, create_rag_pipeline
main_bp = Blueprint('main', __name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from werkzeug.utils import secure_filename

import os
import sys

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

sys.path.append(os.path.abspath(os.path.join('../scripts')))

from rag_pipeline import RagPipeline
from rag_evaluation import RagEvaluation

global rag_chain
rag_chain = None

@main_bp.route('/api/v1/rag-options', methods=['GET'])
def rag_options():
    response = {
        "data": None,
        "error": None
    }
    statusCode = 404
    try:
        response["data"] = get_rag_options()
        statusCode = 200

    except Exception as error:
        logging.error(error)
        response['error'] = f"An error occured: {error}"
        statusCode = 404

    return jsonify(response), statusCode


@main_bp.route('/api/v1/create-rag', methods=['POST'])
def create_rag():
    global rag_chain
    data = request.json
    response = {
        "data": None,
        "error": None
    }
    statusCode = 400

    try:
     
        rag_chain = create_rag_pipeline(data)
        response["data"] = "Rag Pipeline created successfully"
        statusCode = 200

    except KeyError as e:
        error_message = f"Missing required field: {str(e)}"
        logging.error(error_message)
        response['error'] = error_message

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        logging.error(error_message)
        response['error'] = error_message

    return jsonify(response), statusCode


@main_bp.route('/api/v1/file-upload', methods=['POST'])
def upload_file():
    response = {
        "data": None,
        "error": None
    }
    statusCode = 404
    try:
        if 'file' not in request.files:
            raise ValueError("No file part")

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
        
            # extracted_data = DataExtractor.extract_data(filepath)
            rag_chain.add_datasource(filepath)

            response["data"] = "File added to vectorstore successfully"
            print("data upload success")
            print("data upload success")
            print("data upload success")

            statusCode = 200
        else:
            response["error"] = "File format not supported"


    except Exception as error:
        logging.error(error)
        response['error'] = f"An error occured: {error}"
        statusCode = 404

    return jsonify(response), statusCode


@main_bp.route('/api/v1/chat', methods=['POST'])
def chat():

    data = request.json
    response = {
        "data" : None,
        "error" : None
    }
    statusCode = 404
    try:
        message = data['message']
        chain_response = rag_chain.executor.invoke(message)

        response["data"] = chain_response["answer"]
        statusCode = 200

    except Exception as error:
        logging.error(error)
        response['error'] = f"An error occured: {error}"
        statusCode = 404
    return jsonify(response), statusCode

    

@main_bp.route('/api/v1/rag-evaluation', methods=['POST'])
def rag_evaluate():
    response = {
        "data": None,
        "error": None
    }
    statusCode = 404
    try:
        if 'context-file' not in request.files:
            raise ValueError("No context file provided")
        
        if 'qa-file' not in request.files:
            raise ValueError("No question answer file provided")

        context_file = request.files['context-file']
        qa_file = request.files['qa-file']

        base_path = os.getcwd()

        if context_file.filename == '' or qa_file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        if context_file and qa_file and allowed_file(context_file.filename) and allowed_file(qa_file.filename):
            context_filename = secure_filename(context_file.filename)
            context_filepath = os.path.join(UPLOAD_FOLDER, context_filename)
            context_file.save(context_filepath)

            qa_filename = secure_filename(qa_file.filename)
            qa_filepath = os.path.join(UPLOAD_FOLDER, qa_filename)
            context_file.save(qa_filepath)
 
            rag_eval = RagEvaluation(context_path=base_path+context_filepath, question_ans_path=base_path+qa_filepath)
            ragas_dataset = rag_eval.create_ragas_dataset()
            rag_eval_metrics_dict = rag_eval.evaluate_dataset(ragas_dataset)

            eval_response = {
                    "evaluation_metrics": list(rag_eval_metrics_dict.keys()),
                    "total_scores": list(rag_eval_metrics_dict.values()),
                    "values": rag_eval_metrics_dict.to_pandas().values.tolist()
                }

            response["data"] = eval_response
            statusCode = 200
        else:
            response["error"] = "File format not supported"

    except Exception as error:
        logging.error(error)
        response['error'] = f"An error occured: {error}"
        statusCode = 404

    return jsonify(response), statusCode



@main_bp.route('/', methods=['GET'])
def base_get():
    response = {
        "data" : "The backend is working...",
        "error" : None
    }

    return jsonify(response), 200