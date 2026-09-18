import os
from anthropic import Anthropic
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent/".env")

client  = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# ============================================
# TOOLS DEFINITION
# ============================================

tools = [
    {
        "name":"calculate",
        "description":"Performs math calculations. Use when asked to calculate, compute, or solve math.",
        "input_schema": {
            "type": "object",
            "properties":{
                "operation": {
                    "type":"string",
                    "enum":["add","subtract","multiply","divide"]
                },
                "a":{"type": "number"},
                "b":{"type": "number"}
            },
            "required": ["operation","a","b"]
        }
    },
    {
        "name":"get_student_info",
        "description":"Gets student information from database. Use when asked about a specific student.",
        "input_schema":{
            "type":"object",
            "properties":{
                "name":{"type":"string"}
            },
            "required": ["name"]
        }
    }
]

# ============================================
# PYTHON FUNCTIONS
# ============================================
students_db = {
    "rahul": {"name": "Rahul Sharma", "marks": 85, "fee_status": "paid"},
    "priya": {"name": "Priya Patel",  "marks": 92, "fee_status": "paid"},
    "amit":  {"name": "Amit Kumar",   "marks": 0,  "fee_status": "pending"}
}

def calculate(operation:str, a:float, b:float)->float:
    if operation =="add":
        return a+b
    elif operation =="subtract":
        return a-b
    elif operation =="multiply":
        return a*b
    elif operation =="divide":
        if b==0: 
            raise ValueError("Cannot divide by zero")
        return a/b

def get_student_info(name:str)->str:
    student = students_db.get(name.lower())
    if student:
        return f"Name: {student['name']}, Marks: {student['marks']}, Fee: {student['fee_status']}"
    return f"Student '{name}' not found"

def execute_tool(tool_name:str, tool_input: dict):
    if tool_name =="calculate":
        return calculate(**tool_input)
    elif tool_name == "get_student_info":
        return get_student_info(**tool_input)


# ============================================
# LAYER 1 — Agent loop
# ============================================


def run_agent(question:str)->str:
    messages =[{"role":"user", "content": question}]

    print(f"\nQuestion: {question}")
    print("-"*40)

    # Agent loop — keeps running until Claude says end_turn
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )

        print(f"Stop reason : {response.stop_reason}")

        # Claude finished - return final answer
        if response.stop_reason == "end_turn":
            return response.content[0].text

        # Claude want a tool
        if response.stop_reason == "tool_use":
            tool_use_block = next(
                b for b in response.content if b.type =="tool_use"
            )

            tool_name = tool_use_block.name
            tool_input = tool_use_block.input

            print(f"Tool: {tool_name} | Args: {tool_input}")

            result = execute_tool(tool_name, tool_input)
            print(f"Result: {result}")

            # Add to history
            messages.append({"role": "assistant", "content":response.content})
            messages.append({
                "role": "user",
                "content":[{
                    "type": "tool_result",
                    "tool_use_id": tool_use_block.id,
                    "content": str(result)
                }]
            })

            # Loop continues - Claude gets result, decite next step

# if __name__ == "__main__":
#     # Single tool call
#     print(run_agent("What are Rahul's marks?"))

#     # Multiple tool calls in one question
#     print(run_agent(
#         "Get Rahul's marks, then calculate what percentage "
#         "he scored out of 100, and tell me if he passed or failed."
#     ))


# ============================================
# LAYER 2 — Agent loop with streaming
# ============================================

def run_agent_streaming(question:str)-> str:
    messages = [{"role": "user", "content": question}]

    print(f"\nQuestion : {question}")
    print("-"*40)

    while True:
        # Collect full response for tool use detection
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )

        if response.stop_reason == "end_turn":
            #stream the final answer

            print("Claude: ", end="", flush=True )
            final =client.messages.stream(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                tools=tools,
                messages=messages
            )
            full_text = ""
            with final as stream:
                for text in stream.text_stream:
                    print(text, end="", flush=True)
                    full_text += text
            print()
            return full_text
        if response.stop_reason =="tool_use":
            tool_use_block = next(
                b for b in response.content if b.type == "tool_use"
            )

            tool_name = tool_use_block.name
            tool_input = tool_use_block.input

            print(f"Using Tool: {tool_name}")
            print(f"Args: {tool_input}")

            result = execute_tool(tool_name,tool_input)
            print(f"Result: {result}")


            messages.append({"role": "assistant", "content": response.content})
            messages.append({
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": tool_use_block.id,
                    "content": str(result)
                }]
            })

if __name__ == "__main__":
    
    run_agent_streaming(
        "Get Rahul's marks, calculate his percentage out of 100, "
        "and tell me if he passed or failed."
    )


        