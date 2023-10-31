from functions.create_db import create_db
from functions.create_table import create_table

create_db('database.db')
create_table(database_name="database.db",
             table_name="tabela_amada",
             columns="id INTERER PRIMARY KEY, nome_flor TEXT, qtd_petala_flor INTEGER")