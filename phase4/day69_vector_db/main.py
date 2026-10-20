import os
import time
import voyageai
import chromadb
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent/".env")

voyage = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))

# ============================================
# EMBEDDING FUNCTION — Voyage AI
# ============================================


def embed_texts(texts: list[str])-> list[list[float]]:
    result = voyage.embed(texts=texts, model="voyage-3")
    return result.embeddings


# ============================================
# LAYER 1 — Setup ChromaDB with Voyage embeddings
# ============================================

def create_vector_store(collection_name: str ="institura_docs"):
    client = chromadb.PersistentClient(path = "./chroma_db")

    # delete if exixts - fresh start for demo

    try:
        client.delete_collection(collection_name)
    except:
        pass

    collection = client.create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"}
    )

    return collection


# ============================================
# LAYER 2 — Add documents with Voyage embeddings
# ============================================

def add_documents(collection, documents: list[dict]):
    texts = [doc["text"] for doc in documents]
    embeddings = embed_texts(texts)

    collection.add(
        embeddings=embeddings,
        documents=texts,
        metadatas=[doc["metadata"] for doc in documents],
        ids=[doc["id"] for doc in documents]
    )

    print(f"Added {len(documents)} documents to vector store")



# ============================================
# LAYER 3 — Search with Voyage embeddings
# ============================================

def search(collection, query:str, n_results: int = 3) -> list:
    query_embedding = embed_texts([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return [
        {
            "text": doc,
            "metadata": meta,
            "distance": dist
        }
        for doc, meta, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        )
    ]


if __name__ == "__main__":
    # Sample Institura documents
    documents = [
        {
            "id": "doc1",
            "text": "Rahul Sharma scored 85 out of 100 in IIT-JEE 2026 batch. Fee status: paid.",
            "metadata": {"student": "Rahul Sharma", "batch": "IIT-JEE-2026"}
        },
        {
            "id": "doc2",
            "text": "Amit Kumar scored 35 out of 100. At serious risk of failing. Fee pending.",
            "metadata": {"student": "Amit Kumar", "batch": "IIT-JEE-2026"}
        },
        {
            "id": "doc3",
            "text": "Priya Patel scored 92 out of 100 in NEET 2026. Excellent performance.",
            "metadata": {"student": "Priya Patel", "batch": "NEET-2026"}
        },
        {
            "id": "doc4",
            "text": "Sneha Singh scored 96 out of 100. Top student in NEET batch.",
            "metadata": {"student": "Sneha Singh", "batch": "NEET-2026"}
        },
        {
            "id": "doc5",
            "text": "Rohan Verma scored 78 out of 100. Fee payment pending for IIT-JEE batch.",
            "metadata": {"student": "Rohan Verma", "batch": "IIT-JEE-2026"}
        },
        {
            "id": "doc6",
            "text": "IIT-JEE 2026 batch average is 66 marks. Pass rate 67 percent.",
            "metadata": {"type": "batch_stats", "batch": "IIT-JEE-2026"}
        },
        {
            "id": "doc7",
            "text": "NEET 2026 batch average is 94 marks. Pass rate 100 percent.",
            "metadata": {"type": "batch_stats", "batch": "NEET-2026"}
        },
    ]

    #Layer 1 -  create vector store
    print("=== LAYER 1 - creating vector store ===")
    collection = create_vector_store()
    print(f"Collection created: {collection.name}")
    print()

    #Layer 2 - add documents
    print("=== LAYER 2 - Adding Documents ===")
    add_documents(collection, documents)
    print(f"Total documents: {collection.count()}")
    print()

    #Layer 3 - search

    print("=== LAYER 3 - Searching ====")
    queries = [
        "which student is failing and needs urgent help?",
        "what is the average marks for IIT-JEE batch?",
        "students with pending fee payments",
    ]

    for query in queries:
        print(f"Query: '{query}'")
        results = search(collection, query, n_results=2)
        for r in results:
            print(f"[{r['distance']:.4f}] {r['text'][:80]}...")

        print()
        time.sleep(20)
        
