import sqlite3

def insert_one_row(
    database_name: str,
    table_name:str,
    columns_name:str,
    values: str) -> None:
    """ Create
       Args:
        database_name (str): created database name 
        table_name (str): table name 
        columns_name (str): A query specifying the columns
        values (str): Values to insert
    """
    conn=sqlite3.connect(database_name)
    cursor=conn.cursor()
    cursor.execute(
        f"""
        INSERT INTO {table_name} ({columns_name}) VALUES ({values})
        """
    )
    conn.commit()
    conn.close()
