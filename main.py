import argparse
from db.connector import get_connection
from visualize.table_view import show_table
from visualize.chart_view import bar_chart
from visualize.er_diagram import generate_er

parser = argparse.ArgumentParser(description="CLI SQL Visualizer")
parser.add_argument("--query", help="SQL query")
parser.add_argument("--chart", action="store_true")
parser.add_argument("--er", action="store_true")

args = parser.parse_args()

conn = get_connection()
cursor = conn.cursor()

if args.query:
    cursor.execute(args.query)
    rows = cursor.fetchall()
    columns = [i[0] for i in cursor.description]

    show_table(columns, rows)

    if args.chart:
        x = [r[0] for r in rows]
        y = [r[1] for r in rows]
        bar_chart(x, y, "Query Chart")

if args.er:
    generate_er(cursor)

cursor.close()
conn.close()

