# Write a program to remove an entry from the MySQL table on the basis of table
import mysql.connector
connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='random'
)
cursor=connection.cursor()
roll = int(input("Enter a roll no.: "))
sql='''DELETE FROM student WHERE ROLL_NO={}'''.format(roll)
cursor.execute(sql)
connection.commit()
print(cursor.rowcount,'details modified')
connection.close()