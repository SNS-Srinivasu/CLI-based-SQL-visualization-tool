def suggest_joins(cursor, table):
    query = """
    SELECT TABLE_NAME, COLUMN_NAME
    FROM information_schema.COLUMNS
    WHERE COLUMN_NAME LIKE '%id%'
      AND TABLE_SCHEMA = DATABASE()
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print(f"\n🔗 Possible JOIN columns for `{table}`:\n")
    for table_name, column in rows:
        print(f"{table_name}.{column}")

