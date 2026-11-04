from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_anthropic  import ChatAnthropic
from langchain_core.messages import HumanMessage

"""
# 1. Define the state  - the shared Note book

class AgentState(TypedDict):
    question: str
    answer: str


# 2. Initialize the LLM

llm = ChatAnthropic(model="claude-haiku-4-5")

# 3. Define Node 1 - call the llm 
def call_llm(state: AgentState)-> AgentState:
    response = llm.invoke([HumanMessage(content=state["question"])])
    return {"answer": response.content}


# 4. Build the graph
graph = StateGraph(AgentState)

# 5 Add the Node

graph.add_node("call_llm", call_llm)

# 6. Set entry point and edge to END
graph.set_entry_point("call_llm")
graph.add_edge("call_llm", END)

#7. compile - this locks the graph and make it runnable
app = graph.compile()

# 8. Run it

result = app.invoke({"question": " What is state machine in one sentence?"})
print("Answer",result["answer"])
"""

"""
#=============
# Level 2

# 1. Define the state  - the shared Note book

class AgentState(TypedDict):
    question: str
    answer: str


# 2. Initialize the LLM

llm = ChatAnthropic(model="claude-haiku-4-5")

# 3. Define Node 1 - call the llm 
def call_llm(state: AgentState)-> AgentState:
    response = llm.invoke([HumanMessage(content=state["question"])])
    return {"answer": response.content}

# Node 2 decide if answer is long enough
def check_answer(state: AgentState)-> str:
    if len(state["answer"]) > 100:
        return "done"
    else:
        return "retry"

# 4. Build the graph
graph = StateGraph(AgentState)

# 5 Add the Node

graph.add_node("call_llm", call_llm)

# 6. Set entry point and edge to END
graph.set_entry_point("call_llm")


# conditional edge - check_answer decides where to go 

graph.add_conditional_edges(
    "call_llm",
    check_answer,
    {
        "done": END,
        "retry": "call_llm"
    }
)



#7. compile - this locks the graph and make it runnable
app = graph.compile()

# 8. Run it

result = app.invoke({"question": "Say only the word yes"}) # this will stuck in the infinte loop 
print("Answer",result["answer"])

"""

#============
#Level 3 - define the exit condition


class AgentState(TypedDict):
    question: str
    answer: str
    retries: int

llm = ChatAnthropic(model="claude-haiku-4-5")

def call_llm(state:AgentState)-> AgentState:
    response = llm.invoke([HumanMessage(content=state["question"])])
    return{
        "answer": response.content,
        "retries": state.get("retries",0)+1
    }

def check_answer(state: AgentState)-> str:
    if state["retries"]>=3:
        return "done"
    if len(state["answer"])> 100:
        return "done"
    return "retry"


graph = StateGraph(AgentState)
graph.add_node("call_llm", call_llm)
graph.set_entry_point("call_llm")

graph.add_conditional_edges(
    "call_llm",
    check_answer,
    {
        "done": END,
        "retry": "call_llm"

    }
)


app = graph.compile()
result = app.invoke({"question": "Say only the word yes", "retries": 0})
print("Answer:", result["answer"])
print("Retries:", result["retries"])