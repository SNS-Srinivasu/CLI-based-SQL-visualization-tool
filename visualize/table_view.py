from rich.console import Console
from rich.table import Table

def show_table(columns, rows):
    table = Table(title="SQL Query Results")
    for col in columns:
        table.add_column(col)

    for row in rows:
        table.add_row(*[str(x) for x in row])

    Console().print(table)

