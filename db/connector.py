import os
import mysql.connector

def get_connection(database=None):
    """
    Connect to MySQL using default credentials, override with environment variables if provided.
    """
    host = os.getenv("MYSQL_HOST", "localhost")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "saipandu")  # default password

    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database  # can be None initially
    )
    return conn

