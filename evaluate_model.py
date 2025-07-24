import json
import sys
import os

# Add src/ to system path to allow imports
sys.path.append(os.path.abspath("src"))
from src.retriever.retriever import Retriever
from src.data_ingestion.loader import load_json_txt_chapters
from src.generator.generate import generate_answer
from src.evaluation.eval import evaluate_answer
from src.utils import save_results

from sentence_transformers import SentenceTransformer
from transformers import pipeline
# from generator.generate import generate_answer
# from evaluation.eval import evaluate_answer
# from utils import save_results
# Load ground truth evaluation set
with open("data/eval_set.json", "r", encoding="utf-8") as f:
    eval_set = json.load(f)

# Load chunks
with open("data/chunks.json", "r", encoding="utf-8") as f:
    all_chunks = json.load(f)

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize retriever
retriever = Retriever()
retriever.load_index()

# Evaluate
scores = []
for sample in eval_set:
    question = sample["question"]
    true_answer = sample["answer"]

    # 🔍 Embed query
    query_embedding = embed_model.encode([question])

    # 🔍 Retrieve context
    top_indices = retriever.retrieve(query_embedding, k=5)
    retrieved_chunks = [all_chunks[i]["text"] for i in top_indices[0]]
    context = " ".join(retrieved_chunks)

    # 🧠 Generate answer
    pred_answer = generate_answer(question, context)

    # 📏 Evaluate
    score = evaluate_answer(pred_answer, true_answer, embed_model)
    scores.append(score)
    print(f"\nQ: {question}\n✅ True: {true_answer}\n💬 Pred: {pred_answer}\n📊 Score: {score:.4f}")

# Final score
avg_score = sum(scores) / len(scores)
print(f"\n🎯 Average Cosine Similarity Score: {avg_score:.4f}")


results = []
for i, sample in enumerate(eval_set):
    results.append({
        "question": sample["question"],
        "true_answer": sample["answer"],
        "predicted_answer": pred_answer,
        "score": scores[i]
    })

save_results(results, "results/eval_results.json")
