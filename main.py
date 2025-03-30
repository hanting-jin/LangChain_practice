from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from dotenv import load_dotenv  # Fixed import

from tools.sql import run_query_tool
load_dotenv()

chat = ChatOpenAI(temperature=0)

prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad") 
    ]
)

tools = [run_query_tool]

agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executer = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools,
)