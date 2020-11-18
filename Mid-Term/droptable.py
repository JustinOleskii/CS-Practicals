import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123',
    database = 'ananye'
)

cursor = connection.cursor()
colname = input("Enter name of column: ")
sql = '''ALTER TABLE Students DROP COLUMN {}'''.format(colname)
cursor.execute(sql)
connection.commit()
connection.close()