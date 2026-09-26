import os
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent/".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

#============
# Tools 
#=============

tools=[
    {
        "name":"search_student",
        "description": "search for a student by name and return their detail including marks, batch and fee status.",
        "input_schema":{
            "type":"object",
            "properties": {
                "name":{"type": "string","description":"Student name to search for"}
            },
            "required":["name"]
        }
    },
    {
        "name":"calculate",
        "description":"perform math calculation. use for percentage, average, or any arthmetic.",
        "input_schema": {
            "type":"object",
            "properties":{
                "operation": {"type":"string","enum": ["add","subtract","multiply","divide"]},
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required":["operation","a","b"]
        }
    },
    {
        "name": "get_batch_stats",
        "description":" Get statistics for a batch - average marks, pass rate, top student",
        "input_schema":{
            "type": "object",
            "properties":{
                "batch_name": {"type": "string","description":"Name of the batch"}
            },
            "required":["batch_name"]
        }
        
    }
]

#=======
#fake data
#=======

students_db = {
    "rahul sharma": {"name": "Rahul Sharma", "marks": 85, "batch": "IIT-JEE-2026", "fee_status": "paid"},
    "priya patel":  {"name": "Priya Patel",  "marks": 92, "batch": "NEET-2026",    "fee_status": "paid"},
    "amit kumar":   {"name": "Amit Kumar",   "marks": 35, "batch": "IIT-JEE-2026", "fee_status": "pending"},
    "sneha singh":  {"name": "Sneha Singh",  "marks": 96, "batch": "NEET-2026",    "fee_status": "paid"},
    "rohan verma":  {"name": "Rohan Verma",  "marks": 78, "batch": "IIT-JEE-2026", "fee_status": "pending"},
}

batch_stats_db = {
    "IIT-JEE-2026": {"average": 66, "pass_rate": "67%", "top_student": "Rahul Sharma"},
    "NEET-2026":    {"average": 94, "pass_rate": "100%", "top_student": "Sneha Singh"},
}


#===========
# Tool execution
#==============

def execute_tool(tool_name:str,tool_input:dict)-> str:
    if tool_name == "search_student":
        name = tool_input["name"].lower()
        student = students_db.get(name)
        if student:
            return f"Found:{student['name']}, Marks:{student['marks']}/100,Batch: {student['batch']}, Fee: {student['fee_status']}"
        return f"student {tool_input['name']} not found"

    elif tool_name =="calculate":
        a,b = tool_input["a"], tool_input["b"]
        op = tool_input["operation"]
        if op == "add":
            return str(a+b)
        if op == "subtract":
            return str(a-b)
        if op == "multiply":
            return str(a*b)
        if op == "divide":
            return str(a/b) if b !=0 else "Error: division by zero"

    elif tool_name == "get_batch_stats":
        batch = tool_input["batch_name"]
        stats = batch_stats_db.get(batch)
        if stats:
            return f"Batch {batch}: Average={stats['average']}, Pass Rate={stats['pass_rate']}, Top Student={stats['top_student']}"
        return f"Batch '{batch}' not found"

    return "Unkown tool"

#=============
# ReAct with conversation History
#=============

class ReactAgent:
    def __init__(self):
        self.messages= []
        self.system = """You are an intelligent agent for Institura.
You have access to tools to look up student information and calculations.
Before using any tool, explain your reasoning:
- What do you need to find out?
- Which tool will help?
- Why are you choosing this tool?
Think step by step."""

    def chat(self, question:str)-> str:
        # Add new question to the exixting history
        self.messages.append({ "role": "user","content":question})

        print(f"\nYou: {question}")
        print("-"*40)

        step =1
        while True:
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=2048,
                system=self.system,
                tools=tools,
                messages=self.messages
            )

            for block in response.content:
                if hasattr(block,"text") and block.text.strip():
                    print(f"[THINKING] {block.text[:100]}....")
                elif block.type == "tool_use":
                    print(f"[ACTION] {block.name} {block.input}")


            if response.stop_reason == "end_turn":
                final = next( 
                    b.text for b in response.content
                    if hasattr(b, "text")
                )
                #Save Claude's response to history
                self.messages.append(
                    {
                        "role":"assistant",
                        "content": final
                    }
                )
                return final

            elif response.stop_reason =="tool_use":
                tool_use_blocks =[
                    b for b in response.content
                    if b.type == "tool_use"
                ]

                tool_results = []
                for tool_block in tool_use_blocks:
                    result = execute_tool(tool_block.name, tool_block.input)
                    print(f"[RESULT] {result}")
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": tool_block.id,
                        "content": result
                    })

                self.messages.append({
                    "role":"assistant",
                    "content": response.content
                })

                self.messages.append({
                    "role":"user",
                    "content": tool_results
                })
                step+=1

if __name__ == "__main__":
    agent = ReactAgent()

    # Multi-turn conversation — agent remembers context
    print(agent.chat("What are Rahul Sharma's marks?"))
    print()
    print(agent.chat("Is that a good score for his batch?"))
    print()
    print(agent.chat("How does he compare to the topper?"))               