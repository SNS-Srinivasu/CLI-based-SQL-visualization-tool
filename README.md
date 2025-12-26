# SQL CLI Visualizer Project

## Overview:

The SQL CLI Visualizer is a Python-based command-line tool for MySQL databases. It allows you to explore databases, tables, and schemas, suggest joins, run queries, visualize query results as tables and charts, and generate ER diagrams. This tool is lightweight, CLI-friendly, and suitable for personal and shared usage.

## Features:

* Show available databases (`--cmd dbs`)
* Show tables in a selected database (`--cmd tables`)
* Describe a table (`--cmd desc --table <table_name>`)
* Suggest possible joins for a table (`--cmd join --table <table_name>`)
* Run arbitrary SQL queries and display results (`--query "SELECT ..."`)
* Generate charts for query results (`--query "SELECT ..." --chart`)
* Generate ER diagram (`--er`)
* Interactive database selection if environment variable `MYSQL_DB` is not set
* Dockerized deployment for easy sharing and usage

## Requirements:

* Python 3.14+
* MySQL server installed
* Python packages (inside virtual environment recommended):

  * mysql-connector-python
  * rich
  * plotext
  * graphviz
  * pyyaml

## Installation:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sql-cli-visualizer.git
   cd sql-cli-visualizer
   ```

2. Create and activate virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration:

Set MySQL credentials in environment variables or in `db/connector.py`:

```python
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DB=Awesome_Chocolates  # Optional, can be chosen interactively
```

## Usage:

Show databases:

```bash
python main.py --cmd dbs
```

Show tables:

```bash
python main.py --cmd tables
```

Describe a table:

```bash
python main.py --cmd desc --table products
```

Join suggestions for a table:

```bash
python main.py --cmd join --table products
```

Run a query and display as table:

```bash
python main.py --query "SELECT Product, CostPerBox FROM products"
```

Run a query and display as chart:

```bash
python main.py --query "SELECT Product, CostPerBox FROM products" --chart
```

Generate ER diagram:

```bash
python main.py --er
```

## Docker Usage:

1. Build the Docker image:

```bash
docker build -t sql-cli-visualizer .
```

2. Run the container (interactive mode for commands):

```bash
docker run -it --env MYSQL_HOST=host --env MYSQL_USER=user --env MYSQL_PASSWORD=password sql-cli-visualizer python main.py --cmd dbs
```

3. Mount local project (optional) to persist changes:

```bash
docker run -it -v $(pwd):/app --env MYSQL_HOST=host --env MYSQL_USER=user --env MYSQL_PASSWORD=password sql-cli-visualizer python main.py --cmd tables
```

## Project Structure:

```
sql-cli-visualizer/
├── config/             # Configuration files (optional env settings)
├── db/                 # Database connection utilities
│   └── connector.py
├── features/           # Core CLI features: explorer, schema, join helper
├── utils/              # Utility functions
├── visualize/          # Charting, ER diagram generation
├── Dockerfile
├── README.md / Steps.txt
├── Project_Files/      # Sample SQL scripts or data files
├── main.py             # CLI entry point
└── requirements.txt

```

## Future Enhancements:

* Support multiple database types (PostgreSQL, SQLite, etc.)
* Add interactive CLI menu for queries
* Export query results to CSV, JSON, or Excel
* Improve chart types and formatting
* Add user authentication for shared usage

## License:

MIT License
