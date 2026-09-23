import csv
import logging
from pathlib import Path
from models import Student

logger = logging.getLogger(__name__)

def load_students(filepath:str = "students.csv")-> list[Student]:
    students= []
    path = Path(filepath)

    if not path.exists():
        logger.error(f"File not found:{filepath}")
        return []

    with open(path,"r")as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                student = Student(**row)
                students.append(student)
            except Exception as e:
                logger.warning(f"Skipping bad row {row}:{e}")

    logger.info(f"Loaded {len(students)} students from {filepath}")
    return students 
