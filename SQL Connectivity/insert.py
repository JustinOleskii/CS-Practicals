# Write a program to add a new record in a table.
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    username='root',
    password='12345678',
    database='python'
)

records = int(input("Enter amount of records: "))
cursor = connection.cursor()

for i in range(0, records, 1):
    name = input("Enter name: ")
    roll = int(input("Enter roll no.: "))
    querystring = 'INSERT INTO Student (Name,Roll_no) VALUES (%s,%s)'
    val = (name, roll)
    cursor.execute(querystring, val)
    connection.commit()
connection.close()