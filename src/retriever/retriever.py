import faiss
import numpy as np
import os
import torch

class Retriever:
    def __init__(self, dim=384, index_path="data/faiss_index.idx"):
        self.index_path = index_path
        self.index = faiss.IndexFlatL2(dim)
        # Load existing index if available
        if os.path.exists(self.index_path):
            self.load_index()

    def index_embeddings(self, embeddings: np.ndarray):
        """
        Add embeddings to FAISS index.
        Accepts torch.Tensor or numpy.ndarray.
        """
        if torch.is_tensor(embeddings):
            embeddings = embeddings.cpu().numpy()
        self.index.add(embeddings)
        faiss.write_index(self.index, self.index_path)

    def load_index(self):
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
        else:
            print(f"⚠️ Index file {self.index_path} not found. Starting fresh.")

    def retrieve(self, query_embedding: np.ndarray, k=5):
        """
        Retrieve top-k nearest neighbors for the query embedding.
        Returns indices of neighbors.
        """
        if self.index.ntotal == 0:
            print("⚠️ FAISS index is empty. Cannot retrieve results.")
            return []

        if torch.is_tensor(query_embedding):
            query_embedding = query_embedding.cpu().numpy()

        distances, indices = self.index.search(query_embedding, k)
        return indices



# import faiss
# import numpy as np

# class Retriever:
#     def __init__(self, dim=384, index_path="data/faiss_index.idx"):
#         self.index_path = index_path
#         self.index = faiss.IndexFlatL2(dim)        

#     def index_embeddings(self, embeddings):
#         self.index.add(embeddings.cpu().numpy())
#         faiss.write_index(self.index, self.index_path)

#     def load_index(self):
#         self.index = faiss.read_index(self.index_path)

#     def retrieve(self, query_embedding, k=5):
#         if self.index.ntotal == 0:
#             self.load_index()
#         distances, indices = self.index.search(query_embedding, k)
#         return indices