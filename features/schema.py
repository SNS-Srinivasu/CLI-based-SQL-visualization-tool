from utils.table_print import print_table

def describe_table(cursor, table):
    cursor.execute(f"DESCRIBE {table}")
    rows = cursor.fetchall()
    headers = ["Field", "Type", "Null", "Key", "Default", "Extra"]
    print_table(headers, rows)

