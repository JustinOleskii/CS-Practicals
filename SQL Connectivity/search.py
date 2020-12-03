# Write a program to search a record of a table.
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user='root',
    password='12345678',
    database='banking'
)

cursor = connection.cursor()
name = input("Enter name: ")
querystring = 'SELECT * FROM users WHERE NAME = {}'.format(name)
cursor.execute(querystring)
