import sys
import os

# Add src/ to system path to allow imports
sys.path.append(os.path.abspath("src"))

from src.data_ingestion.loader import load_json_txt_chapters
from src.preprocessing import chunk_documents_json 
if __name__ == "__main__":
    documents = load_json_txt_chapters("data")  # or your exact path
    print(f"✅ Loaded {len(documents)} chapter files")

    for doc in documents[:1]:  # Print a sample document
        print("🔍 Sample document:")
        print("Subject:", doc["subject"])
        print("Chapter:", doc["chapter"])
        print("Top-level keys in content:", list(doc["content"].keys()))
        break

    chunks = chunk_documents_json(documents, max_tokens=100, overlap=20)
    print(f"\n✅ Generated {len(chunks)} chunks total")

    print("\n🔍 Sample chunk:")
    print(chunks[0])
    import json

with open("data/chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

print("\n💾 chunks.json saved to data/")
