from functions.create_db import create_db
from functions.create_table import create_table
from functions.insert_rows import insert_one_row
insert_one_row(database_name="database.db",
               table_name="tabela_amada",
               columns_name="id,nome_flor,qtd_petala_flor",
               values="2,'copo_de_leite',3")
#############