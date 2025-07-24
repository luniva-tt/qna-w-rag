Retrieval-Augmented Generation (RAG) Pipeline
This project implements a Retrieval-Augmented Generation pipeline to answer questions based on curriculum-aligned textbook content. It combines document retrieval using FAISS with answer generation by a language model.

Project Structure
bash
Copy
Edit
rag-pipeline-project/
├── data/                      # Textbook chapters in JSON format (.txt files)
├── data/chunks.json           # Preprocessed chunks of textbook content
├── data/faiss_index.idx       # FAISS vector index of chunk embeddings
├── results/                   # Evaluation outputs and plots
├── src/
│   ├── data_ingestion/        # Loading and parsing textbook files
│   ├── preprocessing/         # Chunking and flattening JSON content
│   ├── embedding/             # Generating embeddings using sentence-transformers
│   ├── retriever/             # FAISS index wrapper for retrieval
│   ├── generator/             # Language model for answer generation
│   ├── evaluation/            # Scripts for model evaluation and metrics
│   └── utils/                 # Utility functions (YAML loading, saving JSON)
├── build_index.py             # Script to build FAISS index from chunk embeddings
├── test_query.py              # Test query script to demo retrieval + generation
├── evaluate_model.py          # Evaluate model answers with multiple metrics
├── requirements.txt           # Required Python packages
└── README.md                  # This documentation
Setup
Clone the repo:

bash
Copy
Edit
git clone <repository-url>
cd rag-pipeline-project
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Prepare data:

Place your chapters as JSON-structured .txt files under the data/ folder, organized by subject.

Usage
1. Build embeddings and index
Run the script to generate embeddings from chunks and build the FAISS index:

bash
Copy
Edit
python build_index.py
2. Query the model
Run a test query to retrieve relevant chunks and generate answers:

bash
Copy
Edit
python test_query.py
Modify test_query.py to try your own questions.

3. Evaluate the model
Evaluate model answers using multiple metrics (Cosine similarity, BLEU, ROUGE-L):

bash
Copy
Edit
python evaluate_model.py
Evaluation results will be saved in results/eval_results.json and plotted as results/metrics_plot.png.

Customization
Modify chunk size and overlap in src/preprocessing/preprocessor.py.

Change embedding or generation models in src/embedding/embed.py and src/generator/generate.py.

Update retrieval parameters (top_k) in src/retriever/retriever.py or config files.

Add more evaluation metrics or datasets in evaluate_model.py.