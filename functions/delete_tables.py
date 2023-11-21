import sqlite3

def delete_table(database_name:str,
                 table_name:str,
                 ) -> None:
    """Delete table

    Args:
        database_name (str): created database name 
        table_name (str): table name 
    """
    
    conn=sqlite3.connect(database_name)
    cursor=conn.cursor()
    
    cursor.execute(f"""
        DROP TABLE {table_name}
    """)
    conn.commit()
    conn.close()