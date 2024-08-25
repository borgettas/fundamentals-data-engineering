import os
import psycopg2
from commons.log import setup_logging

logger= setup_logging()


def database_connection():
    conn = psycopg2.connect(
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT'),
    )

    cur = conn.cursor()
    logger.info("🎲 Connection to Database stablished.")

    return conn, cur
