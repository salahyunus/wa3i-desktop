# DATABASE
# connect to sql
import mysql.connector

# create connection
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
    else:
        print('error')

conn = create_connection()

if conn != None:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
  userId INT PRIMARY KEY,
  username VARCHAR(250) NOT NULL,
  password VARCHAR(250) NOT NULL,
  fullName VARCHAR(250) NOT NULL,
  role VARCHAR(6) NOT NULL,
  Image LONGBLOB
);
    ''')
    conn.commit()
    conn.close()