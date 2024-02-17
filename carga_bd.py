import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import config as cf

excel_file = './Dados/20230922.xls'
df = pd.read_excel(excel_file)

conn = psycopg2.connect(
    dbname=cf.BD_NOME,
    user=cf.BD_USER,
    password=cf.BD_SENHA,
    host="localhost"
)

str_conn = "postgresql://" + cf.BD_USER + ":" + cf.BD_SENHA + '@localhost:5432/' + cf.BD_NOME
engine = create_engine(str_conn)

table_name = 'Tributos'
df.to_sql(table_name, engine, if_exists='replace', index=False)
