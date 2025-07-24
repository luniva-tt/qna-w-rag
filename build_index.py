import os
import json
from src.retriever.retriever import Retriever
from src.embedding.embed import generate_embeddings  # assuming your embedding file is named embed.py
import torch

if __name__ == "__main__":
    chunks_path = "data/chunks.json"

    if not os.path.exists(chunks_path):
        raise FileNotFoundError(f"{chunks_path} not found. Run the chunking pipeline first.")

    # 🔹 Load chunked documents
    with open(chunks_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    texts = [chunk["text"] for chunk in chunks]

    print(f"📦 Loaded {len(texts)} texts for embedding...")

    # 🔹 Generate embeddings
    embeddings = generate_embeddings(texts)
    embeddings_tensor = torch.tensor(embeddings)

    print(f"✅ Generated {len(embeddings_tensor)} embeddings.")

    # 🔹 Create and save FAISS index
    retriever = Retriever(dim=384, index_path="data/faiss_index.idx")
    retriever.index_embeddings(embeddings_tensor)

    print(f"✅ FAISS index saved to data/faiss_index.idx")
