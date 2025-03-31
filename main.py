from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent, AgentExecutor  # 更新导入
from dotenv import load_dotenv

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

# 使用新的创建方法
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

# 使用 invoke 替代 run
agent_executer.invoke({"input": "How many users are in the database?"})