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
# React Agent loop
#=============


def run_react_agent(question:str)-> str:
    #ReAct system Prompt - tell claude to think before acting
    system = """You are an intelligent agent for Institura coaching institute.

You have access to tools to look up student information and perform calculations.

IMPORTANT: Before using any tool, explain your reasoning:
- What do you need to find out?
- Which tool will help?
- Why are you choosing this tool?

Think step by step. Show your reasoning before each action."""
    messages = [{"role":"user","content": question}]

    print(f"\nQuestion: {question}")
    print("="* 50)

    step =1 
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system,
            tools=tools,
            messages=messages
        )

        #Print Claude's thinking and Action
        for block in response.content:
            if hasattr(block,"text"):
                print(f"\n[THINKING - step {step}]")
                print(block.text)
            elif block.type == "tool_use":
                print(f"\n[ACTION- step {step}]")
                print(f"Tool: {block.name}")
                print(f"args: {block.input}")

        if response.stop_reason == "end_turn":
            final = next(b.text for b in response.content if hasattr(b,"text"))
            print(f"\n[FINAL ANSWER]")
            return final

        if response.stop_reason == "tool_use":
            # Get ALL tool_use blocks — not just the first one
            tool_use_blocks = [b for b in response.content if b.type == "tool_use"]
            
            # Execute ALL tools and collect ALL results
            tool_results = []
            for tool_use_block in tool_use_blocks:
                result = execute_tool(tool_use_block.name, tool_use_block.input)
                
                print(f"\n[OBSERVATION - step {step}]")
                print(f"Tool: {tool_use_block.name}")
                print(f"Result: {result}")
                
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tool_use_block.id,
                    "content": result
                })

            # Append assistant message + ALL results together
            messages.append({"role": "assistant", "content": response.content})
            messages.append({
                "role": "user",
                "content": tool_results   # all results in one message
            })
            step += 1


if __name__ =="__main__":
    # simple question - one tool
    # print(run_react_agent("What are Rahul Sharma Marks"))

    # print("\n" + "="*60 + "\n")

    print(run_react_agent(
    "Compare Rahul Sharma and Sneha Singh. "
    "Who scored higher and by what percentage difference? "
    "Also tell me which batch has better average marks."
))


            

