FROM python:3

WORKDIR /usr/src/app

COPY data_ingestion/requirements.txt data_ingestion/main.py ./
RUN pip install --no-cache-dir -r requirements.txt

VOLUME /usr/src/app/data_ingestion

CMD ["sh", "-c", "while true; do sleep 1; done"]
