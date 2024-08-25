DROP SCHEMA IF EXISTS example_dbt_core CASCADE;

CREATE SCHEMA IF NOT EXISTS example_dbt_core;

DROP SCHEMA IF EXISTS stripe CASCADE;

CREATE SCHEMA IF NOT EXISTS stripe;

CREATE TABLE IF NOT EXISTS example_dbt_core.customers (
    id int PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255)
);

CREATE TABLE IF NOT EXISTS example_dbt_core.orders (
    id int PRIMARY KEY,
    user_id int,
    order_date date,
    status varchar(255),
    _etl_loaded_at timestamp NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS stripe.payment (
    id int PRIMARY KEY,
    orderid int,
    paymentmethod varchar(255),
    status varchar(255),
    amount integer,
    created date,
    _batched_at timestamp NOT NULL DEFAULT NOW()
);
