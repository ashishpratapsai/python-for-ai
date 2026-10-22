import os
import voyageai
import chromadb
import anthropic
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(Path(__file__).parent/".env")

voyage = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))
claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


#=================
# The knowledge base setup
#==================

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

    print(f"Knowledge base ready: {collection.count()} documents")
    return collection


# ======================
# RETRIEVAL
# ======================

def retrieve(collection, query:str, n_results: int =5)-> list[dict]:
    query_embedding = voyage.embed(texts=[query], model="voyage-3").embeddings[0]

    results = collection.query(
        query_embeddings = [query_embedding],
        n_results=n_results
    )

    return [
        {"text": doc, "metadata":meta, "distance": dist}
        for doc, meta, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        )
    ]


# ======================
# GENERATION
# ======================

def generate_answer(question:str, context_chunks: list[dict])-> str:
    # Step 1 - format  retrieved chunks into readable context
    context = "\n\n".join([
        f"[{i+1}] {chunk['text']}"
        for i,chunk in enumerate(context_chunks)
    ])

    # step 2 - call claude with context in the prompt

    response = claude.messages.create(
        model="claude-haiku-4-5",
        max_tokens=500,
        system= "You are a helpful assistant for Institura coaching institute. "
               "Answer questions using ONLY the context provided. "
               "If the answer is not in the context, say 'I don't have that information.'",
        messages=[
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ]
    )

    return response.content[0].text


#========
# Reranking
#==============

def rerank(query:str, chunks:list[dict], top_n:int =2)-> list[dict]:

    result = voyage.rerank(query, [chunk["text"] for chunk in chunks], model="rerank-2", top_k=top_n)

    reranked= []

    for r in result.results:
        original_chunk = chunks[r.index]
        original_chunk["relevance_score"] = r.relevance_score
        reranked.append(original_chunk)

    return reranked








if __name__=="__main__":
    collection = setup_knowledge_base()
    print()

    questions = [
        "Which student needs urgent academic help?",
        "What is the average performance of the IIT-JEE batch?",
        "What is the fee structure for new admissions?",
    ]

    for question in questions:
        print(f"Q: {question}")
        chunks = retrieve(collection, question, n_results=5)

        print("RAW (by distance)")
        for c in chunks:
            print(f"{c['distance']:.3f} - {c['text'][:50]}")


        reranked  = rerank(question, chunks,2)

        print("RERANKED (by relavence)")
        for c in reranked:
            print(f"{c['relevance_score']:.3f} - {c['text'][:50]}")
            
        answer = generate_answer(question, reranked)
        print(f"A: {answer}")
        print("-"*60)
        print()