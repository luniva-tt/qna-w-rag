# app.py
import sys
import os
import streamlit as st
import json
from sentence_transformers import SentenceTransformer

sys.path.append(os.path.abspath("src"))
from src.retriever.retriever import Retriever
from src.generator.generate import generate_answer

st.title("📘 Curriculum QA Assistant")
st.markdown("Ask a question based on the textbook content.")

@st.cache_resource
def load_components():
    retriever = Retriever()
    retriever.load_index()
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    with open("data/chunks.json", "r", encoding="utf-8") as f:
        all_chunks = json.load(f)
    return retriever, embed_model, all_chunks

retriever, embed_model, all_chunks = load_components()

# Input
question = st.text_input("❓ Enter your question:")

if question:
    query_embedding = embed_model.encode([question])
    top_indices = retriever.retrieve(query_embedding, k=5)
    retrieved_chunks = [all_chunks[i]["text"] for i in top_indices[0]]
    context = " ".join(retrieved_chunks)

    with st.spinner("Generating answer..."):
        answer = generate_answer(question, context)

    st.markdown("### 💬 Answer:")
    st.success(answer)

    with st.expander("📄 Retrieved Context"):
        st.write(context)
