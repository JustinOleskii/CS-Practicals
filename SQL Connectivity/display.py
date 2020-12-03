# Write a program to display all records of a table.
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user='root',
    password='12345678',
    database='banking'
)

cursor = connection.cursor()

querystring = 'SELECT * FROM users'
print(cursor.execute(querystring))