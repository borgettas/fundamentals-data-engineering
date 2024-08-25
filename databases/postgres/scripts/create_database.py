from pathlib import Path
from commons.database_connections import database_connection
from commons.log import setup_logging


if __name__ == "__main__":
    logger= setup_logging()

    conn, cur = database_connection()

    with open(Path(__file__).resolve().parent / "sql/create_tables.sql", "r") as f:
        query = f.read()

    cur.execute(query)
    conn.commit()

    logger.info("📚 Tables created.")