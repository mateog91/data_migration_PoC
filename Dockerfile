FROM postgres


COPY create_tables.sql /docker-entrypoint-initdb.d/
COPY app/file_storage /file_storage