FROM postgres


COPY /db/create_tables.sql /docker-entrypoint-initdb.d/