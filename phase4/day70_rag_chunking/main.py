import os
import voyageai
import chromadb
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent/".env")

voyage = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))


# ============================================
# LAYER 1 — Chunking strategies
# ============================================


def chunk_by_paragraph(text:str) -> list[str]:
    """Split text by double newlines - natural parageaph breatk"""
    chunks = [p.strip() for p in text.split("\n\n") if p.strip()]
    return chunks

def chunk_by_size(text:str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """Split text into fixed size chunks with overlap"""

    chunks =[]
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  # overlap keeps context between chunks

    return chunks

def chunk_by_sentences(text: str, sentence_per_chunk: int = 3) -> list[str]:
    """Split text into chunk of N sentences"""

    sentences = text.replace(".\n",". ").split(". ")
    chunks =[]

    for i in range(0, len(sentences), sentence_per_chunk):
        chunk = ". ".join(sentences[i:i+sentence_per_chunk])
        if chunk.strip():
            chunks.append(chunk.strip())


    return chunks



# ============================================
# LAYER 2 — Embed and store chunks
# ============================================


def embed_and_store(chunks: list[str], collection_name:str)-> chromadb.Collection:
    client = chromadb.PersistentClient(path = "./chroma_db")

    try:
        client.delete_collection(collection_name)
    except:
        pass

    collection = client.create_collection(
        name= collection_name,
        metadata={"hnsw:space": "cosine"}
    )

    # Embed all chunks in one call

    embeddings = voyage.embed(texts=chunks, model="voyage-3").embeddings

    collection.add(
        embeddings=embeddings,
        documents=chunks,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

    return collection


# ============================================
# LAYER 3 — Retrieve relevant chunks
# ============================================

def retrieve(collection, query:str, n_results: int = 2) -> list[str]:
    query_embedding = voyage.embed(texts=[query], model="voyage-3").embeddings[0]

    results = collection.query(
        query_embeddings =[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]




if __name__=="__main__":

    #Load Document

    doc_path = Path(__file__).parent/"sample_document.txt"
    text = doc_path.read_text()

    print(f"Document length: {len(text)} characters")
    print()

    #Layer 1 - compare chunking strategies
    print("=== LAYER 1 - Chunking Strategies ===")

    para_chunks = chunk_by_paragraph(text)
    size_chunks = chunk_by_size(text, chunk_size=300, overlap=50)
    sent_chunks = chunk_by_sentences(text, sentence_per_chunk=3)

    print(f"Paragraph Chunks: {len(para_chunks)}")
    print(f"Size Chunks: {len(size_chunks)}")
    print(f"Sentence Chunks: {len(sent_chunks)}")
    print()

    print("First pragraph chunk")
    print(para_chunks[0][:200])
    print()

    #Layer 2 - embed and store paragraph chunks 
    print("=== Layer 2 - Embedding and storing ===")
    collection = embed_and_store(para_chunks,"institura_handbook")
    print(f"Stored {collection.count()} chunks")
    print()

    #Layer 3 - retrive relavent chunk
    print("==== LAYER 3 -  Retrieval")
    queries = [
        "What are the fee payment deadlines?",
        "How are students graded?",
        "What support does the institute provide?",
    ]

    for query in queries:
        print(f"Qurey: {query}")
        chunks = retrieve(collection, query, n_results=1)
        print(f"Retrived: {chunks[0][:150]}...")
        print()


