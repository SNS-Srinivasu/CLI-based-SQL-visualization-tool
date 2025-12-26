import mysql.connector
import yaml

def get_connection():
    with open("config/db_config.yaml") as f:
        cfg = yaml.safe_load(f)

    return mysql.connector.connect(
        host=cfg["host"],
        user=cfg["user"],
        password=cfg["password"],
        database=cfg["database"]
    )

