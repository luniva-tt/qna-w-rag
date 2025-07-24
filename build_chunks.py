# build_chunks.py
from src.data_ingestion.loader import load_json_txt_chapters
from src.preprocessing.preprocessor import chunk_documents_json
import json
import os

if __name__ == "__main__":
    docs = load_json_txt_chapters("data")
    chunks = chunk_documents_json(docs, max_tokens=100, overlap=20)

    os.makedirs("data", exist_ok=True)
    with open("data/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved {len(chunks)} chunks to data/chunks.json")
