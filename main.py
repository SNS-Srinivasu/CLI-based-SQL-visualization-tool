import argparse
import os
from db.connector import get_connection

from features.explorer import show_databases, show_tables
from features.schema import describe_table
from features.join_helper import suggest_joins
from features.visualizer import run_query, generate_er_diagram


# ---------------- Interactive DB selection (READ ONLY) ----------------
def choose_database():
    """
    Let user pick an existing database.
    No database will be created or modified.
    """
    conn = get_connection(database=None)
    cursor = conn.cursor()

    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor.fetchall()]

    if not databases:
        print("No databases found.")
        exit(1)

    print("\n📂 Available Databases:")
    for i, db in enumerate(databases, start=1):
        print(f"{i}. {db}")

    choice = input("\nSelect database number: ")

    try:
        selected_db = databases[int(choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice. Exiting.")
        exit(1)

    cursor.close()
    conn.close()

    print(f"\n Using database: {selected_db}\n")
    return selected_db


# ---------------- Parse CLI arguments ----------------
parser = argparse.ArgumentParser(
    description="SQL Read-Only Visualization Tool"
)

parser.add_argument("--cmd", choices=["dbs", "tables", "desc", "join"])
parser.add_argument("--table", help="Table name")
parser.add_argument("--query", help="Run READ-ONLY SQL query (SELECT only)")
parser.add_argument("--chart", action="store_true", help="Visualize query output")
parser.add_argument("--er", action="store_true", help="Generate ER diagram")

args = parser.parse_args()


# ---------------- Determine database ----------------
db_name = os.getenv("MYSQL_DB")
if not db_name:
    db_name = choose_database()


# ---------------- Connect to database ----------------
conn = get_connection(database=db_name)
cursor = conn.cursor()


# ---------------- SAFETY CHECK FOR READ-ONLY QUERIES ----------------
def is_read_only(query: str) -> bool:
    forbidden = ["insert", "update", "delete", "drop", "alter", "create", "truncate"]
    return not any(word in query.lower() for word in forbidden)


# ---------------- Execute commands ----------------
if args.query:
    if not is_read_only(args.query):
        print("Write operations are not allowed. READ-ONLY MODE.")
    else:
        run_query(cursor, args.query, chart=args.chart)

elif args.er:
    generate_er_diagram(cursor, db_name)

elif args.cmd == "dbs":
    show_databases(cursor)

elif args.cmd == "tables":
    show_tables(cursor)

elif args.cmd == "desc":
    if args.table:
        describe_table(cursor, args.table)
    else:
        print("Please provide --table")

elif args.cmd == "join":
    if args.table:
        suggest_joins(cursor, args.table)
    else:
        print("Please provide --table")

else:
    print("Invalid usage")
    print("Available:")
    print("  --cmd dbs")
    print("  --cmd tables")
    print("  --cmd desc --table <name>")
    print("  --cmd join --table <name>")
    print("  --query \"SELECT ...\" [--chart]")
    print("  --er")


# ---------------- Close connection ----------------
cursor.close()
conn.close()

