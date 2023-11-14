from functions.create_db import create_db
from functions.create_table import create_table
from functions.insert_rows import insert_one_row
from functions.insert_rows import insert_many_rows
insert_one_row(database_name="database.db",
               table_name="tabela_amada",
               columns_name="id,nome_flor,qtd_petala_flor",
               values="2,'copo_de_leite',3")
#############
#import sqlite3
#
#conn = sqlite3.connect("database.db")
#cursor = conn.cursor()
#lista = [(6,'flor do deserto',4),
#    (7,'flor do deserto',5),
#    (8,'flor do deserto',6)]
#cursor.executemany("INSERT INTO tabela_amada (id,nome_flor,qtd_petala_flor) VALUES (?,?,?)",lista)
#conn.commit()
#conn.close()
insert_many_rows(database_name="database.db",
               table_name="tabela_amada",
               columns_name="id,nome_flor,qtd_petala_flor",
               list_values=[(9,'flor do deserto',4),(10,'flor do deserto',5),(11,'flor do deserto',6)])
