import os
import voyageai
from pathlib import Path
from dotenv import load_dotenv
import chromadb

load_dotenv(Path(__file__).parent/".env")

voyage = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))


# ============================================
# SETUP — Embed and store with rich metadata
# ============================================


def setup_knowledge_base()-> chromadb.Collection:
    client = chromadb.PersistentClient(path="./chroma_db")

    try:
        client.delete_collection("institura_kb")
    except:
        pass

    collection = client.create_collection(
        name="institura_kb",
        metadata={"hnsw:space":"cosine"}
    )

    # Documents with rich metadata
    documents = [
        {
            "text": "Rahul Sharma scored 85 out of 100 in IIT-JEE 2026. Fee status: paid. Strong performance.",
            "metadata": {"student": "Rahul Sharma", "batch": "IIT-JEE-2026", "doc_type": "student_record", "marks": 85}
        },
        {
            "text": "Amit Kumar scored 35 out of 100 in IIT-JEE 2026. At serious risk of failing. Fee: pending.",
            "metadata": {"student": "Amit Kumar", "batch": "IIT-JEE-2026", "doc_type": "student_record", "marks": 35}
        },
        {
            "text": "Priya Patel scored 92 out of 100 in NEET 2026. Excellent performance. Fee: paid.",
            "metadata": {"student": "Priya Patel", "batch": "NEET-2026", "doc_type": "student_record", "marks": 92}
        },
        {
            "text": "Sneha Singh scored 96 out of 100 in NEET 2026. Top student. Fee: paid.",
            "metadata": {"student": "Sneha Singh", "batch": "NEET-2026", "doc_type": "student_record", "marks": 96}
        },
        {
            "text": "Rohan Verma scored 78 out of 100 in IIT-JEE 2026. Fee payment pending.",
            "metadata": {"student": "Rohan Verma", "batch": "IIT-JEE-2026", "doc_type": "student_record", "marks": 78}
        },
        {
            "text": "IIT-JEE 2026 batch: average marks 66, pass rate 67%, top student Rahul Sharma.",
            "metadata": {"batch": "IIT-JEE-2026", "doc_type": "batch_stats"}
        },
        {
            "text": "NEET 2026 batch: average marks 94, pass rate 100%, top student Sneha Singh.",
            "metadata": {"batch": "NEET-2026", "doc_type": "batch_stats"}
        },
        {
            "text": "Fee pending students: Amit Kumar (IIT-JEE-2026) and Rohan Verma (IIT-JEE-2026). Contact parents.",
            "metadata": {"doc_type": "fee_report", "batch": "IIT-JEE-2026"}
        },
    ]


    texts = [doc["text"] for doc in documents]
    embeddings = voyage.embed(texts=texts, model="voyage-3").embeddings

    collection.add(
        embeddings=embeddings,
        documents=texts,
        metadatas=[doc["metadata"] for doc in documents],
        ids=[f"doc_{i}" for i in range(len(documents))]
    )

    print(f"Knowledge base ready : {collection.count()} documents")
    return collection

# ===========================
# LAYER 1 — Basic retrieval 
# ===========================


def retrieve_basic(collection, query:str, n_results: int =2) -> list[dict]:
    query_embedding = voyage.embed(texts=[query], model= "voyage-3").embeddings[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results= n_results
    )

    return [
        {"text": doc, "metadata": meta, "distance": dist}
        for doc,meta,dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        )
    ]


# ============================
# LAYER 2 — Filtered retrieval 
# =============================

def retrieve_filtered(collection, query: str, filter: dict, n_results: int =2)-> list[dict]:
    query_embedding = voyage.embed(texts=[query],model="voyage-3").embeddings[0]
    results = collection.query(
         query_embeddings =[query_embedding],
         where =filter,
         n_results=n_results
    )

    return [
        {"text": doc,"metadata": meta, "distance": dist}
        for doc, meta, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        )
    ]

# ============================================
# LAYER 3 — Multi-query retrieval
# ============================================

def retrieve_multi_query(collection, queries: list[str], n_results: int = 2) -> list[dict]:
    all_results ={}

    for query in queries:
        results = retrieve_basic(collection, query,n_results)
        for r in results:
            # Use text as the key to deduplicate
            if r["text"] not in all_results:
                all_results[r["text"]]= r
            else:
                # keep lower distance more relavent
                if r["distance"]< all_results[r["text"]]["distance"]:
                    all_results[r["text"]]= r
                

    # Sort by distance
    sorted_results = sorted(all_results.values(), key=lambda x: x["distance"])
    return sorted_results

if __name__=="__main__":
    collection = setup_knowledge_base()
    print()

    # Layer 1 basic retrieval
    print("=== LAYER 1 - Basic Retrieval ===")
    query = "which student need urgent academic help"
    results = retrieve_basic(collection,query)
    for r in results:
        print(f"[{r['distance']:.4f}] {r['text'][:80]}")
        print(f"      metadata:{r['metadata']}")
        print()


    # Layer 2 - filtered retrival
    print("=== LAYER 2 - Filtered Retrieval ===")
    print("Filter: doc_type = batch_stats only")
    results = retrieve_filtered(
        collection,
        query="What is the average performance of IIT-JEE batch",
        filter={"doc_type":"batch_stats"}
    )
    for r in results:
        print(f"[{r['distance']:.4f}] {r['text'][:80]}")
        print(f"     metadata:{r['metadata']}")
        print()


    # Layer 3 — multi-query
    print("=== LAYER 3 — Multi-Query Retrieval ===")
    queries = [
        "students with low marks at risk",
        "fee payment pending students",
    ]

    print(f"Queries:{queries}")
    results = retrieve_multi_query(collection,queries)
    for r in results:
        print(f"[{r['distance']:.4f}] {r['text'][:80]}")
        print()


    
