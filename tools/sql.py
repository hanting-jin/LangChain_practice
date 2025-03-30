import sqlite3
from langchain.tools import Tool

dataBaseConnection = sqlite3.connect("database.db")

def ruin_sqlite_query(query):
    c = dataBaseConnection.cursor()
    c.execute(query)
    return c.fetchall()

run_query_tool = Tool.from_function(
    name="Run SQLite Query",
    description="Useful for when you need to answer questions about sqlite databases. Input should be a valid sqlite query.",
    func=ruin_sqlite_query
)