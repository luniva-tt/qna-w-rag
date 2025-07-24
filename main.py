from src.data_ingestion import load_documents
from src.preprocessing import chunk_documents
from src.embedding import generate_embeddings
from src.retriever import Retriever
from src.generator import generate_answer
from src.evaluation import evaluate_answer
from src.utils import load_yaml, save_results

def main():
    # Load configuration
    config = load_yaml('config.yaml')

    # Data ingestion
    documents = load_documents(config['data_path'])

    # Preprocessing
    chunks = chunk_documents(documents, config['chunk_size'])

    # Embedding generation
    embeddings = generate_embeddings(chunks)

    # Initialize retriever and index embeddings
    retriever = Retriever()
    retriever.index_embeddings(embeddings)

    # User query
    user_question = input("Enter your question: ")

    # Retrieve relevant chunks
    relevant_chunks = retriever.retrieve(user_question, top_k=config['top_k'])

    # Generate answer
    answer = generate_answer(user_question, relevant_chunks)

    # Evaluate answer (optional)
    if 'ground_truth' in config:
        evaluation_result = evaluate_answer(answer, config['ground_truth'])
        save_results(evaluation_result, 'evaluation_results.json')

    # Output the answer
    print("Generated Answer:", answer)

if __name__ == "__main__":
    main()