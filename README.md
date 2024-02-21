# Optimized-Contract-QA-RAG-System-Enhancements

This repository contains the codebase for building, evaluating, and improving a Retrieval Augmented Generation (RAG) system for Contract Q&A. The objective is to develop a powerful contract assistant and eventually a fully autonomous contract bot.

## Project Overview

The project aims to leverage RAG technology to create an AI-powered contract advisor capable of answering questions related to legal contracts. By combining large language models with external data sources, the system aims to provide accurate and context-rich responses to user queries. The development process involves:

1. Researching ways to improve RAG systems, including efficiency, scalability, personalization, contextualization, and bias reduction.
2. Building a simple Q&A pipeline with RAG using Langchain, a leading LLM application framework.
3. Creating a RAG evaluation pipeline with RAGAS to assess the performance of the system.
4. Ideating and implementing enhancements to optimize the system for Contract Q&A.
5. Interpretation & Reporting: Presenting the outcomes of the project with a short deck and providing performance metrics to quantify incremental improvements.

## Folder Structure

- **backend/**: Contains the Flask backend for serving the RAG model and handling API requests.
- **frontend/**: Houses the React frontend for user interaction and displaying contract Q&A results.
- **logs/**: Stores log files for backend and frontend activities.
- **notebooks/**: Includes Jupyter notebooks for data exploration, model training, and performance evaluation.
- **prompts/**: Stores prompt templates and examples for RAG model input.
- **scripts/**: Contains utility scripts for data preprocessing, model training, and evaluation.
- **tests/**: Holds unit tests and integration tests for backend and frontend functionalities.
- **workflows/**: Contains GitHub Actions workflows for automated testing, linting, and deployment.
- **.env_example**: Example environment variables file for configuring the Flask backend.
- **.gitignore**: Specifies intentionally untracked files to ignore in version control.
- **Makefile**: Provides convenient commands for setting up, running tests, and other project tasks.
- **README.md**: Main repository documentation providing an overview of the project and instructions for setup.

## Setup Instructions

1. **Backend Setup**:
   - Navigate to the `backend/` directory.
   - Create a virtual environment: `python -m venv venv`.
   - Activate the virtual environment: `source venv/bin/activate`.
   - Install dependencies: `pip install -r requirements.txt`.
   - Copy `.env_example` to `.env` and configure environment variables.
   - Run the Flask app: `flask run`.

2. **Frontend Setup**:
   - Navigate to the `frontend/` directory.
   - Install dependencies: `npm install`.
   - Start the React app: `npm start`.

3. **Testing**:
   - Run backend tests: `pytest backend/tests`.
   - Run frontend tests: `npm test`.

4. **Deployment**:
   - Utilize GitHub Actions workflows for CI/CD pipeline setup.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.