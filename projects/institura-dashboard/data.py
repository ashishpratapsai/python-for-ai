import csv
import logging
from pathlib import Path
from pydantic import BaseModel, field_validator

logging.basicConfig(
    level = logging.INFO,
    format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

class Student(BaseModel):
    roll_number :str
    name : str
    batch : str
    marks : int
    fee_status : str


    @field_validator("name")
    @classmethod
    def clean_name(cls,v: str)-> str:
        return v.strip().title()

    @field_validator("marks", mode ="before")
    @classmethod
    def clean_marks(cls,v)-> int:
        try:
            return int(v)
        except(ValueError, TypeError):
            return 0

    @field_validator("fee_status")
    @classmethod
    def clean_fee(cls ,v:str)-> str:
        return v.strip().lower()

def load_students(filepath: str)-> list[Student]:
    students=[]
    path =Path(filepath)

    if not path.exists():
        logger.error(f"File not found: {filepath}")
        return []

    with open(path,"r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                student = Student(**row)
                students.append(student)
            except Exception as e:
                logger.warning(f"Skipping invalid row: {e}")

    logger.info(f"Loaded {len(students)} students")
    return students

if __name__ == "__main__":
    students = load_students("sample_students.csv")
    for s in students[:3]:
        print(s)

