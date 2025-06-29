import mysql.connector

try:
    mydb = mysql.connector.connect(host = "localhost". user = "root", passwd = "")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error:
    print("Error creating database")
finally:
    mycursor.close()
    mydb.close()
