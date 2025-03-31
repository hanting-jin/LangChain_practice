from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent, AgentExecutor 
from langchain.schema import SystemMessage

from dotenv import load_dotenv

from tools.sql import run_query_tool, list_table
load_dotenv()

chat = ChatOpenAI(temperature=0)

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content="You are an AI that has access to a SQlite database."),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad") 
    ]
)

tools = [run_query_tool]
tables = list_table()

print(tables)
import pydantic
print(pydantic.__version__)


agent = create_openai_functions_agent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executer = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools,
)

agent_executer.invoke({"input": "How many users are in the database?"})