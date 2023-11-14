import sqlite3
import pandas as pd

conn=sqlite3.connect("database.db")

df=pd.read_sql_query(
    """
    SELECT nome_flor As nome, qtd_petala_flor as qtd
    """,conn)

df=
