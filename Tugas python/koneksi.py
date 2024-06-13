import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",  # Localhost address
        user="admin",  # MySQL username
        passwd="1234567890",  # MySQL password
        database="pythonsql"  # Replace with your database name
    )

    if mydb.is_connected():
        print("Database connected successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    if (mydb.is_connected()):
        mydb.close()
        print("MySQL connection is closed")
