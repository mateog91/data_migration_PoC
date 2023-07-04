#!/usr/bin/env python3
import psycopg2

conn = psycopg2.connect(database="postgres",
                        user='postgres', password='pswd12345',
                        host='127.0.0.1', port='5432'
                        )

conn.autocommit = True
cursor = conn.cursor()

sql1 = '''INSERT INTO departments (id, department) VALUES (2, 'Sales');'''