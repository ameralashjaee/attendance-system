import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="123456",
    database='stdb',
)
mycursor=myconn.cursor()
mycursor=myconn.cursor(buffered=True)

