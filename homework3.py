import os
import pandas as pd
import sqlite3

def create_dataframe(db_path):
    if not os.path.isfile(db_path):
        raise ValueError("invalid path to database file")
    conn = sqlite3.connect(db_path)
    tables = ["ca", "de", "fr", "gb", "us"]
    sql_query_template = "SELECT video_id, category_id, '{}' AS language FROM {}videos"
    sql_query_by_table = [sql_query_template.format(table, table.upper()) for table in tables]
    sql_query = " UNION ".join(sql_query_by_table) + ";"
    df = pd.read_sql_query(sql_query, conn)
    conn.close()
    return df
