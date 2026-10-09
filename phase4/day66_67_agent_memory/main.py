from memory import ConversationMemory, VectorMemory
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).parent/".env")   

client = Anthropic(api_key= os.getenv("ANTHROPIC_API_KEY"))




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


class MemoryAgent:
    def __init__(self):
        self.conv_memory = ConversationMemory()
        self.vec_memory = VectorMemory()
        self.system = """You are an intelligent agent for institura.
        You have access to tools and memory of past conversation.
        Before using anytool explain your resoning."""

    def chat(self, question:str)-> str:
        #search vector memory for relevant context
        relevant = self.vec_memory.search(question, n_result=2)
        context = ""
        if relevant:
            context ="\n\nRelevant memort:\n"
            for r in relevant:
                context += f"- {r['text']}\n"

        # save user question to conversation memory
        self.conv_memory.save("user", question)

        # Get recent history + add context to last message
        messages = self.conv_memory.get_recent(10)
        messages[-1]["content"] = question + context

        step = 1
        while True:
            response = client.messages.create(
                model ="claude-sonnet-4-6",
                max_tokens=2048,
                system=self.system,
                tools=tools,
                messages=messages

            )

            for block in response.content:
                if hasattr(block,"text") and block.text.strip():
                    print(f"[THINKING] {block.text[:100]}...")
                elif block.type == "tool_use":
                    print(f"[ACTION] {block.name}{block.input}")

            if response.stop_reason == "end_turn":
                final = next(
                    b.text for b in response.content
                    if hasattr(b,"text")
                )
                self.conv_memory.save("assistant", final)
                self.vec_memory.save(
                    f"Q: {question} A: {final}",
                    {"type":"qa"}
                )
                return final

            elif response.stop_reason == "tool_use":
                tool_use_block = [
                    b for b in response.content
                    if b.type == "tool_use"
                ]
                tool_result = []

                for tool_block in tool_use_block:
                    result = execute_tool(tool_block.name,tool_block.input)
                    print(f"[RESULTS]: {result}")
                    tool_result.append({
                        "type":"tool_result",
                        "tool_use_id": tool_block.id,
                        "content": result
                        }
                    )
                messages.append({
                    "role":"assistant",
                    "content": response.content
            
                })

                messages.append({
                    "role":"user",
                    "content": tool_result
                })
                step +=1


if __name__ =="__main__":
    # agent = MemoryAgent()


    # print(agent.chat("What are Rahul Sharma's marks"))
    # print()

    # print(agent.chat("Is Amit kumar is risk of failing"))
    # print()

    agent2 =MemoryAgent()

    print("\n ----SITIMULATING RESTART-----")
    print()
    print(agent2.chat("What did we discussed about Rahual earlier"))

