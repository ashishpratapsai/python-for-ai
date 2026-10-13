import os
import voyageai
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent/".env")

voyage = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))

# ============================================
# LAYER 1 — Create a single embedding
# ============================================

# Single text → single embedding (for Layer 1 and Layer 3)
def embed_text(text: str) -> list[float]:
    result = voyage.embed(
        texts=[text],
        model="voyage-3"
    )
    return result.embeddings[0]

# Multiple texts → multiple embeddings (for Layer 2 batch)
def embed_texts(texts: list[str]) -> list[list[float]]:
    result = voyage.embed(
        texts=texts,
        model="voyage-3"
    )
    return result.embeddings

# ============================================
# LAYER 2 — Compare similarity between texts
# ============================================

def cosine_similarity(vec1:list, vec2: list) -> float:
    dot_product = sum(a*b for a, b in zip(vec1, vec2))
    magnitude1 = sum(a ** 2 for a in vec1) ** 0.5
    magnitude2 = sum(b ** 2 for b in vec2) ** 0.5
    return dot_product / (magnitude1 * magnitude2)


# ============================================
# LAYER 3 — Find most similar text
# ============================================


def find_most_similar(query:str, document: list[str])-> list:
    # Embed query + all documents in ONE call
    all_text = [query] + documents
    all_embeddings = embed_texts(all_text)


    query_embedding = all_embeddings[0]
    doc_embeddings = all_embeddings[1:]

    results = []
    for doc,doc_emb in zip(documents,doc_embeddings):
        similarity = cosine_similarity(query_embedding,doc_emb)
        results.append({
            "text": doc,
            "similarity": similarity
            }
        )

    results.sort(key=lambda x:x["similarity"], reverse=True)
    return results


if __name__ =="__main__":
    # Student facts about Institura students
    documents = [
        "Rahul Sharma scored 85 out of 100 in IIT-JEE preparation",
        "Amit Kumar scored 35 out of 100 and is at risk of failing",
        "Priya Patel scored 92 out of 100 in NEET preparation",
        "Sneha Singh scored 96 out of 100 and is the top student",
        "Rohan Verma scored 78 out of 100 and fee is pending",
    ]


    #Layer 1 - single embedding
    print("===LAYER 1 - Single Embedding===")
    embedding = embed_text("Rahul Sharma scored 85")
    print(f"Text: 'Rahul Sharma scored 85'")
    print(f"Embedding dimentions: {len(embedding)}")
    print(f"First 5 values: {embedding[:5]}")
    print()

    # Layer 2 — similarity comparison
    print("=== LAYER 2 — Similarity Comparison ===")
    text1 = "student failed the exam"
    text2 = "pupil did not pass the test"
    text3 = "the weather is sunny today"

    texts = [text1, text2, text3]
    embedding = embed_texts(texts)

    emb1 = embedding[0]
    emb2 = embedding[1]
    emb3 = embedding[2]
    


    sim_12 = cosine_similarity(emb1,emb2)
    sim_13 = cosine_similarity(emb1,emb3)

    print(f"'{text1}' vs '{text2}'")
    print(f"Similarities: {sim_12:.4f}")
    print()
    print(f"'{text1}' vs '{text3}'")
    print(f"Similarities: {sim_13:.4f}")
    print()


    # Layer 3 - find most similar
    print("=== Layer 3 - Find Most Similar ===")
    query = "Which student needs help and is struggling?"
    print(f"Query: '{query}'")
    print()

    results = find_most_similar(query, documents)
    for r in results:
        print(f"Similarity: {r['similarity']:4f} | {r['text']}")


