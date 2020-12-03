import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user='root',
    password='12345678',
    database='banking'
)

cursor = connection.cursor()
querystring = 'DELETE FROM users'
cursor.execute(querystring)
connection.commit()
connection.close()