FROM python:3

WORKDIR /data_ingestion

COPY data_ingestion/requirements.txt /data_ingestion/

RUN pip install --no-cache-dir -r requirements.txt

COPY data_ingestion/main.py /data_ingestion/

CMD [ "python", "main.py"]
