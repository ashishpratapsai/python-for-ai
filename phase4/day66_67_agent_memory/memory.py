import json
import os
from pathlib import Path
from datetime import datetime
import chromadb

#============
# Type 1 - file basd conversation
#===========

class ConversationMemory:
    def __init__(self, filepath:str = "conversation_history.json"):
        self.filepath = filepath
        self.messages = self._load()

    def _load(self)-> list:
        if Path(self.filepath).exists():
            with open(self.filepath,"r") as f:
                return json.load(f)

        return[]

    def save(self,role:str,content: str):
        entry = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()

        }
        self.messages.append(entry)
        self._persist()

    def _persist(self):
        with open(self.filepath, "w") as f:
            json.dump(self.messages,f, indent=2)


    def get_recent(self, n:int=10)-> list:
        # Return n last messagges
        recent = self.messages[-n:]
        return [
            {"role":m["role"],"content":m["content"]}
            for m in recent
        ]

    def clear(self):
        self.messages =[]
        if Path(self.filepath).exists():
            os.remove(self.filepath)

# ==========================
# TYPE 2 — Vector-based semantic memory
# ==========================

class VectorMemory:
    def __init__(self,collection_name:str ="agent_memory"):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def save(self,text:str,metadata:dict={}):
        # Generate unique ID using timestamp
        doc_id = f"mem_{datetime.now().timestamp()}" 
        self.collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[doc_id]
        )
        return doc_id

    def search(self, query:str, n_result:int =3):
        results = self.collection.query(
            query_texts=[query],
            n_results=n_result
        )
        if not results["distances"][0]:
            return []
        return [
            {
                "text":doc,
                "metadata":meta,
                "distance": dist
            }
            for doc,meta,dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0]
            )
        ]

    def count(self)->int:
        return self.collection.count()


if __name__ == "__main__":
    # Test ConversationMemory
    print("=== Testing ConversationMemory ===")
    mem = ConversationMemory()
    mem.save("user", "What are Rahul's marks?")
    mem.save("assistant", "Rahul scored 85/100")
    print(f"Saved {len(mem.messages)} messages")
    print(f"Recent: {mem.get_recent(2)}")
    print()

    # Test VectorMemory
    print("=== Testing VectorMemory ===")
    vec = VectorMemory()
    vec.save("Rahul Sharma struggles with calculus", {"student": "Rahul"})
    vec.save("Priya Patel is excellent at biology", {"student": "Priya"})
    vec.save("Amit Kumar needs help with physics", {"student": "Amit"})
    print(f"Saved {vec.count()} memories")
    
    results = vec.search("who needs academic help?")
    print(f"Search results for 'who needs academic help?':")
    for r in results:
        print(f"  → {r['text']} (distance: {r['distance']:.3f})")