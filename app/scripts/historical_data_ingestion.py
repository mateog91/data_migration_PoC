#!/usr/bin/env python3
import os
import psycopg2


table_names = ["jobs", "departments", "hired_employees"]

conn = psycopg2.connect(database="postgres",
                        user='postgres',
                        password='pswd12345',
                        host='127.0.0.1',
                        port='5432'
                        )
for table_name in table_names:

    cursor = conn.cursor()
    print(table_name)
    # read file and store to postgres databese

    csv_file_path = f'./file_storage/landing_zone/{table_name}.csv'
    postgres_file_path = f'/file_storage/landing_zone/{table_name}.csv'

    copy_sql = f"""
    COPY {table_name}
    FROM '{postgres_file_path}'
    DELIMITER ',' CSV
"""
    # Execute the COPY command
    print(copy_sql)
    with open(csv_file_path, 'r') as f:
        cursor.copy_expert(sql=copy_sql, file=f)
    # cursor.execute(copy_sql)
    conn.commit()

    #move file to processed
    os.mv(csv_file_path, f'./file_storage/processed/{table_name}.csv')

conn.close()
