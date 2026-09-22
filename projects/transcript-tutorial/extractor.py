import os
from anthropic import Anthropic
from pathlib import Path
from dotenv import load_dotenv
from models import Tutorial, TutorialSection

# loading environment variables 
load_dotenv(Path(__file__).parent/".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def extract_structure(transcript:str)-> Tutorial:
    # defining the tool
    tools = [{
        "name": "save_tutorial_structure",
        "description":"save the structured output to the tutorial",
        "input_schema":{
            "type":"object",
            "properties":{
                "title":{"type":"string"},
                "introduction":{"type":"string"},
                "sections":{
                    "type":"array",
                    "items":{
                        "type":"object",
                        "properties":{
                            "heading":{"type": "string"},
                            "content":{"type": "string"},
                            "code_example": {"type": "string"}
                        },
                        "required": ["heading","content"]
                    }
                    },
                "key_takeaways":{
                        "type":"array",
                        "items":{"type":"string"}
                    },
                "thumbnail_prompt":{"type":"string"}
            },
            "required":["title","introduction","sections","key_takeaways","thumbnail_prompt"]
        }
    }]
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        tools=tools,
        tool_choice={"type":"any"},
        system=[
            {
                "type":"text",
                                "text": f"""You are a YouTube tutorial writer. 
                Analyze the transcript below and extract a structured tutorial.

                For the thumbnail_prompt — write a detailed image description 
                for a YouTube thumbnail. Include: topic, visual style, 
                text overlay suggestion, color scheme.

                TRANSCRIPT:
                {transcript}""",
                "cache_control":{"type":"ephemeral"}
                #ephemeral = chache lasts 5 mins
            }
        ],
        messages=[{
                "role":"user",
                "content": "Extract the tutorial structure from the transcript above."

                }]
    )
    tool_use_block = next(
        b for b in response.content if b.type == "tool_use"
    )
    return Tutorial(**tool_use_block.input)

