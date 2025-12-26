from graphviz import Digraph

def generate_er(cursor):
    dot = Digraph(comment="ER Diagram", format="png")

    cursor.execute("SHOW TABLES")
    tables = [t[0] for t in cursor.fetchall()]

    for table in tables:
        cursor.execute(f"DESCRIBE {table}")
        cols = cursor.fetchall()
        label = f"{table}|"
        for c in cols:
            label += f"{c[0]}\\l"
        dot.node(table, shape="record", label=label)

    dot.render("er_diagram")
    print("✅ ER diagram generated: er_diagram.png")

