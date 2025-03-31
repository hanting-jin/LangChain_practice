import sqlite3
from langchain.tools import Tool

dataBaseConnection = sqlite3.connect("db.sqlite")

def list_table():
      c = dataBaseConnection.cursor()
      c.execute("SELECT name FROM sqlite_master WHERE type='table';")
      rows = c.fetchall()
      return rows

def ruin_sqlite_query(query):
    c = dataBaseConnection.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as error:
        return f"An error occurred: {str(error)}"

run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Useful for when you need to answer questions about sqlite databases. Input should be a valid sqlite query.",
    func=ruin_sqlite_query
)