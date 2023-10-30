import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='123456789')
if conn.is_connected():
    print("connection successful")