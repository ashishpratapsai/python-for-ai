import os
import base64
import httpx
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent/".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# ============================================
# LAYER 1 — Analyze image from URL
# ============================================

def analyze_image_url(image_url: str, question:str)-> str:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{
            "role":"user",
            "content":[
                {
                    "type":"image",
                    "source":{
                        "type":"url",
                        "url": image_url
                    }
                },
                {
                    "type":"text",
                    "text": question
                }
            ]
        }]
    )
    return response.content[0].text

# if __name__=="__main__":
#     print("=== IMAGE FROM URL ===")
#     result = analyze_image_url(
#     image_url="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png",
#     question="What is in this image? Describe it briefly."
#     )
#     print(result)
#     print()


# ============================================
# LAYER 2 — Analyze image from local file
# ============================================

def analyze_image_file(image_path:str, question:str)->str:
    with open(image_path,"rb") as f:
        image_data = base64.standard_b64encode(f.read()).decode("utf-8")

    extention = Path(image_path).suffix.lower()
    media_types={
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp"
    }
    media_type =media_types.get(extention,"image/jpeg")

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{
            "role":"user",
            "content":[
                {
                    "type": "image",
                    "source":{
                        "type": "base64",
                        "media_type": media_type,
                        "data": image_data
                    }
                },
                {
                    "type":"text",
                    "text": question
                }
            ]
        }]
    )
    return response.content[0].text

# if __name__=="__main__":
#         # Layer 2
#     print("=== IMAGE FROM LOCAL FILE ===")
#     result = analyze_image_file(
#         "test_image.png",
#         "What do you see in this image? Describe it."
#     )
#     print(result)

# ============================================
# LAYER 3 — Analyze PDF
# ============================================

def analyze_pdf(pdf_path:str, question:str)->str:
    with open(pdf_path,"rb") as f:
        pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens= 2048,
        messages=[{
            "role":"user",
            "content":[
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_data
                    }
                },
                {
                    "type": "text",
                    "text": question
                }
            ]
        }]
    )
    return response.content[0].text

if __name__=="__main__":
    #layer 3
    print("=== PDF FROM LOCAL FILE ===")
    result = analyze_pdf(
        "test.pdf",
        "What do you see in this pdf? Describe it."
    )
    print(result)