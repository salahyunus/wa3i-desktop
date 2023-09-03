# DATABASE

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

if conn != None:
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Post (
     postId INT PRIMARY KEY,
     postName VARCHAR(250) NOT NULL,
     postContent TEXT,
     userId INT NOT NULL,
     -- Foreign Key:
     FOREIGN KEY (userId) REFERENCES User(userId),
     comments VARCHAR(250) NOT NULL
    );    
    ''')
    conn.commit()
    conn.close()