# Retrieval-Augmented Generation (RAG) Pipeline

This project implements a complete Retrieval-Augmented Generation (RAG) pipeline, which combines information retrieval and natural language generation to provide accurate and contextually relevant answers to user queries.

## Project Structure

```
rag-pipeline-project
├── src
│   ├── data_ingestion       # Module for loading documents from various formats
│   ├── preprocessing         # Module for preprocessing documents into manageable chunks
│   ├── embedding             # Module for generating embeddings from document chunks
│   ├── retriever             # Module for retrieving relevant chunks using FAISS
│   ├── generator             # Module for generating answers using a language model
│   ├── evaluation            # Module for evaluating the quality of generated answers
│   └── utils                 # Utility functions used across the project
├── requirements.txt          # List of project dependencies
├── config.yaml               # Configuration settings for the project
├── main.py                   # Entry point for the RAG pipeline
└── README.md                 # Project documentation
```

## Components

1. **Data Ingestion**: 
   - Responsible for reading documents from the `data/` folder in .txt and .pdf formats.
   - Exports the function `load_documents`.

2. **Preprocessing**: 
   - Handles chunking of documents into 500-token pieces with slight overlaps.
   - Exports the function `chunk_documents`.

3. **Embedding**: 
   - Generates embeddings for document chunks using models from `sentence_transformers`.
   - Exports the function `generate_embeddings`.

4. **Retriever**: 
   - Implements a FAISS vector store for indexing and retrieving relevant document chunks.
   - Exports the class `Retriever` with methods for indexing and retrieval.

5. **Generator**: 
   - Generates answers to user questions using a language model.
   - Exports the function `generate_answer`.

6. **Evaluation**: 
   - Evaluates the quality of generated answers against ground truth.
   - Exports the function `evaluate_answer`.

7. **Utils**: 
   - Contains utility functions for loading configuration files and saving results.
   - Exports functions like `load_yaml` and `save_results`.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd rag-pipeline-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the settings in `config.yaml` as per your requirements.

## Running the Pipeline

To run the RAG pipeline, execute the following command:
```
python main.py
```

This will initiate the process of data ingestion, preprocessing, embedding generation, retrieval, and answer generation.

## Examples

- Provide a sample query to see how the pipeline retrieves and generates answers based on the ingested documents.

For further details on each module, please refer to the respective files in the `src` directory.