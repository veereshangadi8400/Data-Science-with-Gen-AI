import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Vresh@342749'
)

cursor = mydb.cursor()
cursor.execute('SELECT VERSION()')
result = cursor.fetchone()
print(result)

cursor.close()
mydb.close()