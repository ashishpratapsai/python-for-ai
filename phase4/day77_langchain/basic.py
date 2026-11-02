from dotenv import load_dotenv

load_dotenv()


from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

llm = ChatAnthropic(model="claude-sonnet-4-5")

messages =[

    SystemMessage(content="You are brutally consise assistant. Answer in one sentense only."),
    HumanMessage(content="Expalin Quantam entaglement")
    

]
response = llm.invoke(messages)
print("Turn 1:", response.content)



# ADD the response to history, then ask a follow-up
messages.append(AIMessage(content=response.content))
messages.append(HumanMessage(content="Give me a real world example"))


response2 = llm.invoke(messages)
print("Turn 2:", response2.content)
