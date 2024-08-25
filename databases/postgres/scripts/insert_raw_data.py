import pandas as pd
from commons.database_connections import database_connection
from commons.log import setup_logging
from pathlib import Path

logger= setup_logging()


if __name__ == "__main__":
    logger= setup_logging()
    conn, cur = database_connection()

    logger.info("Inserting data to DB...")

    mapping_tables = {
        "example_dbt_core_customers.csv": "example_dbt_core.customers",
        "example_dbt_core_orders.csv": "example_dbt_core.orders",
        "stripe_payments.csv": "stripe.payment",
    }

    for file in mapping_tables.keys():
        tablename = mapping_tables[file]
        data = pd.read_csv(Path(__file__).resolve().parent.parent / "data/{}".format(file))

        try:
            logger.info(
                "Uploading {} records to the table {}...".format(len(data), tablename)
            )
            args_str = b",".join(
                cur.mogrify("(" + "%s," * (len(data.columns) - 1) + "%s)", x)
                for x in tuple(map(tuple, data.values))
            )
            cur.execute(
                "INSERT INTO {} VALUES ".format(tablename) + args_str.decode("utf-8")
            )
            conn.commit()

            logger.info("{} uploaded to the Database".format(tablename))
        except Exception as e:
            logger.error("{}: {}".format(tablename, e))

    cur.close()
    conn.close()
