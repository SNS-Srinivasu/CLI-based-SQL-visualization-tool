import argparse
import os
from db.connector import get_connection
from features.explorer import show_databases, show_tables
from features.schema import describe_table
from features.join_helper import suggest_joins

# New import for visualization features
from features.visualizer import run_query, generate_er_diagram

# ---------------- Interactive DB selection ----------------
def choose_database():
    """Let user pick a database interactively if MYSQL_DB not set"""
    conn = get_connection(database=None)  # Connect without selecting DB
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor.fetchall()]

    print("\nAvailable Databases:")
    for i, db in enumerate(databases, start=1):
        print(f"{i}. {db}")

    choice = input("\nEnter database number to connect: ")
    try:
        selected_db = databases[int(choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice. Defaulting to first database.")
        selected_db = databases[0]

    print(f"\n✅ Connecting to database: {selected_db}\n")
    cursor.close()
    conn.close()
    return selected_db

# ---------------- Parse CLI arguments ----------------
parser = argparse.ArgumentParser(description="SQL CLI Visualizer")
parser.add_argument("--cmd", help="dbs | tables | desc | join")
parser.add_argument("--table", help="Table name")
parser.add_argument("--query", help="Run SQL query")
parser.add_argument("--chart", action="store_true", help="Show chart for SQL query result")
parser.add_argument("--er", action="store_true", help="Generate ER diagram for current database")
args = parser.parse_args()

# ---------------- Determine database ----------------
db_name = os.getenv("MYSQL_DB")
if not db_name:
    db_name = choose_database()

# ---------------- Connect to chosen database ----------------
conn = get_connection(database=db_name)
cursor = conn.cursor()

# ---------------- Execute commands ----------------
if args.query:
    # Run SQL query and optionally show chart
    run_query(cursor, args.query, chart=args.chart)

elif args.er:
    # Generate ER diagram for current database
    generate_er_diagram(cursor, db_name)

elif args.cmd == "dbs":
    show_databases(cursor)

elif args.cmd == "tables":
    show_tables(cursor)

elif args.cmd == "desc":
    if args.table:
        describe_table(cursor, args.table)
    else:
        print("❌ Please provide a table name with --table")

elif args.cmd == "join":
    if args.table:
        suggest_joins(cursor, args.table)
    else:
        print("❌ Please provide a table name with --table")

else:
    print("❌ Invalid command. Available commands: dbs, tables, desc, join, --query, --er")

# ---------------- Close connection ----------------
cursor.close()
conn.close()

