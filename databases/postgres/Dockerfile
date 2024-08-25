FROM python:3.12.4-slim

COPY . /app

WORKDIR /app

RUN pip install -r ./requirements.txt

CMD python3 scripts/create_database.py
CMD python3 scripts/insert_raw_data.py