from rich.table import Table
from rich.console import Console
import plotext as plt
from graphviz import Digraph
import os

console = Console()

def run_query(cursor, query, chart=False):
    """Run SQL query, print table, optionally plot chart"""
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    # Print table
    table = Table(show_header=True, header_style="bold magenta")
    for col in columns:
        table.add_column(col)
    for row in rows:
        table.add_row(*[str(r) for r in row])
    console.print(table)

    # Plot chart if requested (only for 2-column numeric)
    if chart:
        if len(columns) != 2:
            console.print("❌ Chart requires exactly 2 columns")
            return
        x = [str(r[0]) for r in rows]
        y = [float(r[1]) for r in rows]
        plt.clear_data()
        plt.bar(x, y)
        plt.show()

def generate_er_diagram(cursor, db_name):
    """Generate ER diagram for all tables in a DB"""
    cursor.execute(f"SHOW TABLES FROM {db_name}")
    tables = [t[0] for t in cursor.fetchall()]

    dot = Digraph(comment=f"ER Diagram - {db_name}")

    for table in tables:
        cursor.execute(f"DESCRIBE {db_name}.{table}")
        fields = cursor.fetchall()
        label = f"{table}|\n" + "\n".join([f"{f[0]} ({f[1]})" for f in fields])
        dot.node(table, label=label, shape="record")

    # Save diagram
    output_file = f"{db_name}_er_diagram"
    dot.render(output_file, format="png", cleanup=True)
    console.print(f"✅ ER Diagram saved: {output_file}.png")

