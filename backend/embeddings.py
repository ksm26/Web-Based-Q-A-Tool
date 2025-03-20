import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

# Use a small, fast embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# FAISS Index
dimension = 384  # Embedding size of MiniLM
index = faiss.IndexFlatL2(dimension)
stored_texts = []  # Store text chunks

def add_to_index(url: str, content: str):
    global stored_texts
    chunks = content.split(". ")  # Simple chunking
    
    embeddings = model.encode(chunks)
    index.add(np.array(embeddings, dtype=np.float32))
    
    stored_texts.extend(chunks)

def search_index(query: str):
    query_embedding = model.encode([query])
    _, top_k = index.search(np.array(query_embedding, dtype=np.float32), k=5)
    
    results = [stored_texts[i] for i in top_k[0] if i < len(stored_texts)]
    return " ".join(results)
