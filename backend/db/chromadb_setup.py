# backend/db/chromadb_setup.py

import chromadb
from chromadb.utils import embedding_functions
from backend.utils.vachanamrut_loader import load_vachanamrut
from backend.utils.chunker import split_into_chunks

# 1. Initialize ChromaDB client
client = chromadb.Client()
collection = client.get_or_create_collection("vachanamrut_english")

# 2. Choose embedding model (use local transformer)
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# 3. Load and process data
entries = load_vachanamrut("data/raw/vachanamrut_combined.json")
all_chunks = []

for entry in entries:
    all_chunks.extend(split_into_chunks(entry))

# 4. Insert into ChromaDB
for idx, chunk in enumerate(all_chunks):
    collection.add(
        ids=[f"chunk-{idx}"],
        documents=[chunk["chunk"]],
        metadatas=[{
            "vach_id": chunk["id"],
            "title": chunk["title"],
            "reference": chunk["reference"]
        }]
    )

print(f"✅ Inserted {len(all_chunks)} chunks into ChromaDB.")
