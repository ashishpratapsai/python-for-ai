from pydantic import BaseModel, field_validator

# Version 1 -  basic model
class Student(BaseModel):
    roll_number: str
    name : str
    batch : str
    academic_year : str
    personal_email: str
    phone: str
    parent_name : str
    parent_phone: str
    marks : int
    fee_status: str

#------------

# version 2 - with validator

class StudentV2(BaseModel):
    roll_number: str
    name: str
    batch: str
    academic_year: str
    personal_email: str
    phone: str
    parent_name: str
    parent_phone: str
    marks: int
    fee_status: str

    @field_validator("marks")
    @classmethod
    def marks_must_be_positve(cls,v):
        if v<0:
            raise ValueError("Marks cannot be Negative")
        if v>100:
            raise ValueError("Marks cannot exceed 100")
        return v

    @field_validator("name")
    @classmethod
    def clean_name(cls, v):
        return v.strip().title()