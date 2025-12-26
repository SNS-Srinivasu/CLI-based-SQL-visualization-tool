from utils.table_print import print_table

def show_databases(cursor):
    cursor.execute("SHOW DATABASES")
    rows = cursor.fetchall()
    print_table(["Databases"], rows)

def show_tables(cursor):
    cursor.execute("SHOW TABLES")
    rows = cursor.fetchall()
    print_table(["Tables"], rows)

