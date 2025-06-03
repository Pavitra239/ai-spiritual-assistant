# backend/rag/pipeline.py

from chromadb import Client
from chromadb.utils import embedding_functions
import subprocess
# If using local LLM later (e.g., LLaMA), update this function
def generate_response(query: str, context_chunks: list) -> str:
    context = "\n\n".join([chunk['document'] for chunk in context_chunks])
    prompt = f"""Answer the user's question based only on the context from Swaminarayan scripture below.

Context:
{context}

Question:
{query}

Answer:"""

    # Call Ollama CLI
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        capture_output=True
    )
    output = result.stdout.decode().strip()
    return f"📜 **Context from Vachanamrut**:\n{context}\n\n🤖 **Answer**:\n{output}"

def ask_question(question: str, top_k: int = 3) -> str:
    # 1. Initialize client + embedder
    client = Client()
    embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    collection = client.get_or_create_collection("vachanamrut_english", embedding_function=embed_fn)

    # 2. Query top-k chunks
    results = collection.query(query_texts=[question], n_results=top_k)

    # 3. Extract documents + metadata
    context_chunks = []
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        context_chunks.append({
            "document": doc,
            "reference": meta.get("reference", ""),
            "title": meta.get("title", "")
        })

    # 4. Generate full response
    return generate_response(question, context_chunks)
