import os
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent/".env")
client = Anthropic(api_key=os.getenv("ANTHROPI_API_KEY"))

#==========
# Bad tools - vague, in complete
#=========

bad_tools= [
    {
        "name": "search",
        "description": "Search for stuff",
        "input_schema": {
            "type": "object",
            "properties":{
                "q": {"type":"string"}
            },
            "required": ["q"]
            
        }
    },
    {
        "name":"calc",
        "description":"do math",
        "input_schema":{
            "type":"object",
            "properties":{
                "x":{"type":"number"},
                "y":{"type":"number"},
                "op":{"type":"string"}
            },
            "required":["x","y","z"]
        }
    }
]



#===========
# good tools - specific, clear, with example
#=============

good_tools = [
    {
        "name":"search_student",
        "description":"""Search for studetnt by their full name in institura database,
Returns: student name, marks out of 100, batch name, fee status (paid/pending).
Returns error message if student not found.
Use exact full name — 'Rahul Sharma' not just 'Rahul'.
Use this when asked about a specific student's performance or details.""",
        "input_schema":{
            "type":"object",
            "properties":{
                "name":{
                    "type":"string",
                    "description": "Full name of the student. Example: Rahul Sharma"
                }
            },
            "required":["name"]
        }
    },
    {
        "name": "calculate",
        "description": """Perform arithmetic calculations.
Use for: percentage difference, averages, score comparisons.
Returns the numeric result as a string.
Example: to find percentage, use divide then multiply by 100.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "operation": {
                    "type": "string",
                    "enum": ["add", "subtract", "multiply", "divide"],
                    "description": "The arithmetic operation to perform"
                },
                "a": {
                    "type": "number",
                    "description": "First number"
                },
                "b": {
                    "type": "number",
                    "description": "Second number. For divide — cannot be zero."
                }
            },
            "required": ["operation", "a", "b"]
        }
    },
    {
        "name": "get_batch_stats",
        "description": """Get performance statistics for an entire batch.
Returns: average marks, pass rate percentage, name of top student.
Use when comparing batches or understanding overall batch performance.
Batch names: 'IIT-JEE-2026' or 'NEET-2026'""",
        "input_schema": {
            "type": "object",
            "properties": {
                "batch_name": {
                    "type": "string",
                    "enum": ["IIT-JEE-2026", "NEET-2026"],
                    "description": "Name of the batch to get statistics for"
                }
            },
            "required": ["batch_name"]
        }
    }
]

# ============================================
# DATABASE + EXECUTE TOOL 
# ============================================
students_db = {
    "rahul sharma": {"name": "Rahul Sharma", "marks": 85, "batch": "IIT-JEE-2026", "fee_status": "paid"},
    "priya patel":  {"name": "Priya Patel",  "marks": 92, "batch": "NEET-2026",    "fee_status": "paid"},
    "amit kumar":   {"name": "Amit Kumar",   "marks": 35, "batch": "IIT-JEE-2026", "fee_status": "pending"},
    "sneha singh":  {"name": "Sneha Singh",  "marks": 96, "batch": "NEET-2026",    "fee_status": "paid"},
}

batch_stats_db = {
    "IIT-JEE-2026": {"average": 66, "pass_rate": "67%", "top_student": "Rahul Sharma"},
    "NEET-2026":    {"average": 94, "pass_rate": "100%", "top_student": "Sneha Singh"},
}

def execute_tool(tool_name: str, tool_input: dict) -> str:
    # handles both bad and good tool names
    if tool_name in ["search_student", "search"]:
        name_key = "name" if "name" in tool_input else "q"
        name = tool_input[name_key].lower()
        student = students_db.get(name)
        if student:
            return f"Found: {student['name']}, Marks: {student['marks']}/100, Batch: {student['batch']}, Fee: {student['fee_status']}"
        return f"Student not found. Available: {list(students_db.keys())}"

    elif tool_name in ["calculate", "calc"]:
        a_key = "a" if "a" in tool_input else "x"
        b_key = "b" if "b" in tool_input else "y"
        op_key = "operation" if "operation" in tool_input else "op"
        a = tool_input[a_key]
        b = tool_input[b_key]
        op = tool_input[op_key]
        if op in ["add", "+"]:      return str(a + b)
        if op in ["subtract", "-"]: return str(a - b)
        if op in ["multiply", "*"]: return str(a * b)
        if op in ["divide", "/"]:   return str(a / b) if b != 0 else "Error: division by zero"

    elif tool_name == "get_batch_stats":
        batch = tool_input["batch_name"]
        stats = batch_stats_db.get(batch)
        if stats:
            return f"Batch {batch}: Average={stats['average']}, Pass Rate={stats['pass_rate']}, Top Student={stats['top_student']}"
        return f"Batch not found. Available: {list(batch_stats_db.keys())}"

    return f"Unknown tool: {tool_name}"


def run_agent(question: str, tools: list, label: str) -> str:
    messages = [{"role": "user", "content": question}]
    print(f"\n{'='*50}")
    print(f"{label}")
    print(f"Question: {question}")
    print('='*50)

    step = 1
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )

        for block in response.content:
            if hasattr(block, "text") and block.text.strip():
                print(f"[THINKING] {block.text[:150]}...")
            elif block.type == "tool_use":
                print(f"[ACTION] {block.name}({block.input})")

        if response.stop_reason == "end_turn":
            final = next(b.text for b in response.content if hasattr(b, "text"))
            return final

        elif response.stop_reason == "tool_use":
            tool_use_blocks = [b for b in response.content if b.type == "tool_use"]
            tool_results = []
            for tool_block in tool_use_blocks:
                result = execute_tool(tool_block.name, tool_block.input)
                print(f"[RESULT] {result}")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tool_block.id,
                    "content": result
                })
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})
            step += 1


if __name__ == "__main__":
    question = "What are Rahul Sharma's marks and is he above batch average?"

    # Run with bad tools
    result1 = run_agent(question, bad_tools, "=== BAD TOOLS ===")
    print(f"\nFINAL: {result1}\n")

    # Run with good tools
    result2 = run_agent(question, good_tools, "=== GOOD TOOLS ===")
    print(f"\nFINAL: {result2}\n")