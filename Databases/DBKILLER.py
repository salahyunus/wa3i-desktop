# DATABASE KILLER

import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
            host='localhost',
            database='United_DB',
            user='root',
            password='Yeer2023'
    )
    if connection.is_connected():
        print('Connected to MySQL database')
        return connection
conn = create_connection()
# DROP POST FIRST
if conn != None:
    cursor = conn.cursor()
    cursor.execute('''
    DROP TABLE IF EXISTS User;
    ''')
    conn.commit()
    conn.close()
# AFTER RUNNING THIS CODE MAKE SURE TO RUN Account_DB.py and Content_DB.py