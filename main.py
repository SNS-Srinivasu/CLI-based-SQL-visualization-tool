import argparse
from db.connector import get_connection
from features.explorer import show_databases, show_tables
from features.schema import describe_table
from features.join_helper import suggest_joins

parser = argparse.ArgumentParser(description="SQL CLI Visualizer")
parser.add_argument("--cmd", help="dbs | tables | desc | join")
parser.add_argument("--table", help="Table name")

args = parser.parse_args()

conn = get_connection()
cursor = conn.cursor()

if args.cmd == "dbs":
    show_databases(cursor)

elif args.cmd == "tables":
    show_tables(cursor)

elif args.cmd == "desc":
    describe_table(cursor, args.table)

elif args.cmd == "join":
    suggest_joins(cursor, args.table)

else:
    print("❌ Invalid command")

cursor.close()
conn.close()

