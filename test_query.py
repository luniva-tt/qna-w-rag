import sys
import os

# Add src/ to system path to allow imports
sys.path.append(os.path.abspath("src"))
from src.retriever.retriever import Retriever
from src.data_ingestion.loader import load_json_txt_chapters
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import json

# Load all chunks
with open("data/chunks.json", "r", encoding="utf-8") as f:
    all_chunks = json.load(f)

# Query
query = "What are the five kingdoms?"

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
query_embedding = embed_model.encode([query])

# Retrieve top-k
retriever = Retriever()
retriever.load_index()
top_indices = retriever.retrieve(query_embedding, k=5)

# Gather retrieved chunks
retrieved_chunks = [all_chunks[i]["text"] for i in top_indices[0]]
context = " ".join(retrieved_chunks)

# QA model (free and effective)
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(question, context):
    prompt = f"question: {question} context: {context}"
    response = qa_pipeline(prompt, max_new_tokens=100)
    return response[0]["generated_text"].strip()

# Final output
answer = generate_answer(query, context)
print("📘 Question:", query)
print("💬 Answer:", answer)
