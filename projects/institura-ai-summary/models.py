from pydantic import BaseModel,field_validator
from typing import Optional

class Student(BaseModel):
    name: str
    marks: float
    batch: str
    fee_status: str

    @field_validator("name")
    @classmethod
    def clean_name(cls, v:str)->str:
        return v.strip().title()

    @field_validator("marks", mode="before")
    @classmethod
    def clean_marks(cls,v)-> float:
        try:
            return float(v)
        except (ValueError, TypeError):
            return 0.0

    @field_validator("fee_status")
    @classmethod
    def clean_fee(cls,v:str)->str:
        return v.strip().lower()

    @field_validator("batch")
    @classmethod
    def clean_batch(cls,v:str)->str:
        return v.strip()

class ParentMessage(BaseModel):
    student_name: str
    message: str
    tone: str
    fee_reminder: bool

    