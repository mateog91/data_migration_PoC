#!/usr/bin/env python3
import os
import shutil
import psycopg2
import time

def connect_to_postgres():
    for i in range(10):
        try:
            conn = psycopg2.connect(database="postgres",
                            user='postgres',
                            password='pswd12345',
                            host='postgres',
                            port='5432'
                            )
            return conn
        except Exception as e:
            print(f"Retrying connection to postgres in 1 second ({i+1}/10)")
            time.sleep(5)
            continue

    print(f"Could not connect to postgres after {i+1} attempts")
    raise Exception("Could not connect to postgres")



def main():
    table_names = ["jobs", "departments", "hired_employees"]
    # Connect to an existing database


    for table_name in table_names:
        conn = connect_to_postgres()

        cursor = conn.cursor()

        # check if file exists in processed folder
        processed_file_path = f'/file_storage/processed/{table_name}.csv'

        if os.path.exists(processed_file_path):
            print(f"File was already processed: {processed_file_path}")
            continue

        # Initialize paths
        csv_file_path = f'/file_storage/landing_zone/{table_name}.csv'
        if not os.path.exists(csv_file_path):
            print(f"Processing file not exists: {csv_file_path}")
            continue

        postgres_file_path = csv_file_path

        # Initialize cursor and query

        copy_sql = f"""
        COPY {table_name}
        FROM '{postgres_file_path}'
        DELIMITER ',' CSV
    """
        print(copy_sql)

        try:
            # Execute the COPY command
            with open(csv_file_path, 'r') as f:
                cursor.copy_expert(sql=copy_sql, file=f)
            conn.commit()
        except psycopg2.Error as e:
            print(e)
            conn.rollback()

        #move file to processed
        shutil.move(csv_file_path, f'/file_storage/processed/{table_name}.csv')
        print(f"Processed file: {csv_file_path}")

    cursor.close()
    conn.close()
    print("Finished processing files")

if __name__ == "__main__":
    main()

