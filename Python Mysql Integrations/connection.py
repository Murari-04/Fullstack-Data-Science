import mysql.connector
conn = mysql.connector.connect(host = 'localhost', user = 'root', password = '2004')

if conn.is_connected():
    print("Connection established")
print(conn)
print(conn.is_connected())