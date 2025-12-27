import os
import mysql.connector

def get_connection(database=None):
    """
    Create a MySQL connection.
    - If database is None → connects to MySQL server only
    - If database is provided → connects to that database
    """

    config = {
        "host": os.getenv("MYSQL_HOST", "localhost"),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
    }

    # Attach database ONLY if provided
    if database:
        config["database"] = database

    return mysql.connector.connect(**config)

