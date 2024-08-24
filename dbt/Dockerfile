# Use a imagem base do Ubuntu
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

RUN pip install \
    dbt-core \
    polars \
    --break-system-packages

WORKDIR /app

# RUN chmod +x app/dbt_init.sh

# RUN app/dbt_init.sh
