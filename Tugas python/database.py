import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # Localhost address
    user="admin",  # MySQL username
    passwd="1234567890",  # MySQL password
    database="pythonsql"  # Replace with your database name
)

cursor = mydb.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_siswa (
    No VARCHAR(10) PRIMARY KEY,
    Nama VARCHAR(255),
    Alamat VARCHAR(10)
)
""")
print("Table created successfully!")