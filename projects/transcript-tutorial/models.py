from pydantic import BaseModel
from typing import Optional

class TutorialSection(BaseModel):
    heading: str
    content: str
    code_example: Optional[str] = None # optional -  default to None

class Tutorial(BaseModel):
    title: str
    introduction: str
    sections: list[TutorialSection]
    key_takeaways: list[str]
    thumbnail_prompt: str


