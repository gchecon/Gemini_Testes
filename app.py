from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.llm import Gemini
from sqlalchemy.engine import URL
import config as cf

connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": cf.STR_CONN})
gemini = Gemini()

db = SQLDatabase.from_uri(
    str(connection_url),
    schema="public",
    include_tables=['Tributos'],
)

db_chain = SQLDatabaseChain.from_llm(llm=gemini, db=db, prompt=cf.PROMPT_ROLE)

