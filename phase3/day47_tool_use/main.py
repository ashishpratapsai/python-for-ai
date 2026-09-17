import os
from anthropic import Anthropic
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent/".env")

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

#=========
# Layer 1 - Define and execut tool
#=========

# Step 1- Define your tools
# This is what you need to send to Claude so it knows what tool exist

tools = [
    {
        "name":"calculate",
        "description": "Performs basic math calculations. Use this when the user asks to calculate, compute, or solve a math problem.",
        "input_schema":{
            "type":"object",
            "properties":{
                "operation": {
                    "type": "string",
                    "enum":["add","subtract","multiply","divide"],
                    "description": "The math operation to perform"
                },
                "a":{
                    "type": "number",
                    "description": "First Number"
                },
                "b":{
                    "type": "number",
                    "description": "Second Number"
                }
                
            },
            "required": ["operation","a","b"]
        }
    }
]

# Step 2 - The actual python function that run the tool

def calculate(operation:str, a:float, b:float)-> float:
    if operation == "add":
        return a+b
    elif operation == "subtract":
        return a-b
    elif operation =="multiply":
        return a*b
    elif operation =="divide":
        if  b==0:
            raise ValueError("Cannot divide by Zero")
        return a/b

# Step 3- The tool use loop

def ask_with_tools(question: str)-> str:
    messages = [{"role":"user", "content": question}]

    #First API call  - Claude decide if it needs a tool
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=tools,
        messages=messages
    )

    print(f"Stop reason : {response.stop_reason}")

    # If Claude wants to use a tool 
    if response.stop_reason == "tool_use":
        # Finf the tool_use block
        tool_use_block = next(
            block for block in response.content
            if block.type =="tool_use"
        )

        tool_name = tool_use_block.name
        tool_input = tool_use_block.input

        print(f"Claude wants to use: {tool_name}")
        print(f"With argument : {tool_input}")


        # Execute the tool
        result = calculate(**tool_input)
        print(f"Tool result: {result}")

        # send result back to Claude

        messages.append({"role":"assistant","content": response.content})
        messages.append({
            "role":"user",
            "content":[
                {
                    "type":"tool_result",
                    "tool_use_id": tool_use_block.id,
                    "content": str(result)
                }
            ]
        
        
        })

        #Second API call - Claude give final Answer

        final_response =  client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            tools=tools,
            messages=messages

        )

        return final_response.content[0].text

    # Claude answered directly without tool
    return response.content[0].text

# if __name__=="__main__":
#     print(ask_with_tools("What is 1234 multiplied by 5678?"))
#     print()
#     print(ask_with_tools("What is the capital of India?"))


# ==================
# LAYER 2 — Multiple tools
# ==================


tool_v2 = [
    {
        "name": "calculate",
        "description": "Performs basic math. Use when asked to calculate or compute.",
        "input_schema":{
            "type":"object",
            "properties":{
                "operation": {"type":"string","enum": ["add","subtract","multiply","divide"]},
                "a":{"type":"number"},
                "b":{"type":"number"}
            },
            "required": ["operation","a","b"]
        }
    },
    {
        "name": "get_student_info",
        "description": "Get student info. use when asked about student.",
        "input_schema":{
            "type":"object",
            "properties":{
                "name":{"type": "string"}
            },
            "required": ["name"]
        }

    }
]

students_db = {
    "rahul": {"name": "Rahul Sharma", "marks": 85, "fee_status": "paid"},
    "priya": {"name": "Priya Patel", "marks": 92, "fee_status": "paid"},
    "amit":  {"name": "Amit Kumar",  "marks": 0,  "fee_status": "pending"}
}

def get_student_info(name:str)-> str:
    student =students_db.get(name.lower())
    if student:
        return f"Name: {student['name']}, Marks: {student['marks']}, Fee: {student['fee_status']}"
    return f"Student '{name}' not found"

def execute_tool(tool_name:str, tool_input:dict):
    if tool_name == "calculate":
        return calculate(**tool_input)
    elif tool_name == "get_student_info":
        return get_student_info(**tool_input)

def ask_with_multiple_tools(question:str)->str:
    messages = [{"role":"user","content": question}]

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=tool_v2,
        messages=messages
    )

    print(f"Stop reason: {response.stop_reason}")

    if response.stop_reason == "tool_use":
        tool_use_block = next(
            b for b in response.content if b.type == "tool_use"
        )

        print(f"Tool: {tool_use_block.name} | Args: {tool_use_block.input}")

        result = execute_tool(tool_use_block.name,tool_use_block.input)
        print(f"Result: {result}")

        messages.append({"role":"assistant","content": response.content})
        messages.append({
            "role":"user",
            "content":[{
                "type": "tool_result",
                "tool_use_id":tool_use_block.id,
                "content": str(result)
            }]
        })

        final = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            tools=tool_v2,
            messages=messages
        )
        return final.content[0].text

    return response.content[0].text

if __name__=="__main__":
    print(ask_with_multiple_tools("what are Rahul Marks?"))
    print()
    print(ask_with_multiple_tools("What is 999 divided by 3?"))
    print()
    print(ask_with_multiple_tools("Is Priya's fee paid?"))