import os
import json
from anthropic import Anthropic
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv(Path(__file__).parent/".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# ============================================
# LAYER 1 — Pydantic models for output
# ============================================

class StudentAnalysis(BaseModel):
    name: str
    marks: int
    grade: str
    status: str
    feedback: str


class BatchReport(BaseModel):
    total_students: int
    average_marks: float
    top_student: str
    pass_count: int
    fail_count: int
    summary: str


# ============================================
# LAYER 2 — JSON mode structured output
# ============================================

def analyse_student_json(name: str, marks:int)-> StudentAnalysis:
    prompt = f"""Analyse this student ans respond in JSON only.
    student: {name}, Marks: {marks} out of 100

    Respond with this exact JSON Structure
    {{
       "name": "student name",
        "marks": marks as integer,
        "grade": "A/B/C/F based on marks",
        "status": "Pass or Fail",
        "feedback": "one sentence feedback" 
    }}
    Grade rules: 90+ = A, 75+ = B, 40+ = C, below 40 = F
    Pass if marks >= 40, Fail otherwise.
    
    """

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role":"user","content": prompt}]
    )

    raw_text = response.content[0].text
    print(f"Raw response: {raw_text}\n")

    # Strip markdown code blocks if present
    if "```json" in raw_text:
        raw_text = raw_text.split("```json")[1].split("```")[0].strip()
    elif "```" in raw_text:
        raw_text = raw_text.split("```")[1].split("```")[0].strip()

    # parse JSON and validate with Pydantic 
    data = json.loads(raw_text)
    return StudentAnalysis(**data)


# ============================================
# LAYER 3 — Tool use for structured output
# ============================================


def analyse_student_tool(name:str, marks: int)-> StudentAnalysis:
    # Define tool that accepts structured data
    tools = [{
        "name": "save_student_analysis",
        "description": "Save the structured analysis of a student",
        "input_schema": {
            "type": "object",
            "properties": {
                "name":     {"type": "string"},
                "marks":    {"type": "integer"},
                "grade":    {"type": "string", "enum": ["A", "B", "C", "F"]},
                "status":   {"type": "string", "enum": ["Pass", "Fail"]},
                "feedback": {"type": "string"}
            },
            "required": ["name", "marks", "grade", "status", "feedback"]
        }
    }]

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=tools,
        tool_choice={"type":"any"}, # forces Claude to use a tool
        messages=[{
        "role": "user",
        "content": f"Analyse student {name} who scored {marks}/100. "
               f"Grade rules: 90+ = A, 75+ = B, 40+ = C, below 40 = F. "
               f"Pass if marks >= 40, Fail otherwise."
            }]
    )
    # Extract tool input — this IS the structured data
    tool_use_block = next(
        b for b in response.content if b.type =="tool_use"
    )

    print(f"Tool input: {tool_use_block.input}\n")

    # validate with Pydantic directly
    return StudentAnalysis(**tool_use_block.input)

if __name__ == "__main__":
    # JSON mode
    print("=== JSON MODE ===")
    result = analyse_student_json("Rahul Sharma", 85)
    print(f"Name:     {result.name}")
    print(f"Grade:    {result.grade}")
    print(f"Status:   {result.status}")
    print(f"Feedback: {result.feedback}")

    print()

    # Tool use mode
    print("=== TOOL USE MODE ===")
    result = analyse_student_tool("Priya Patel", 92)
    print(f"Name:     {result.name}")
    print(f"Grade:    {result.grade}")
    print(f"Status:   {result.status}")
    print(f"Feedback: {result.feedback}")