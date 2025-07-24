from typing import List
from sentence_transformers import SentenceTransformer
import torch

# Load model once globally to save time if embedding multiple times
MODEL = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(texts: List[str], batch_size: int = 32) -> List[List[float]]:
    """
    Generate embeddings for a list of texts using SentenceTransformer.

    Args:
        texts (List[str]): List of input text strings.
        batch_size (int): Number of texts to encode at once.

    Returns:
        List[List[float]]: List of embeddings as float lists.
    """
    embeddings = []
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i+batch_size]
        batch_emb = MODEL.encode(batch_texts, convert_to_tensor=True)
        embeddings.extend(batch_emb.cpu().tolist())
    return embeddings



#     embeddings = model.encode(document_chunks, convert_to_tensor=True)
    
#     return embeddings.tolist()  # Convert to list for easier handling