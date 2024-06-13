import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # Localhost address
    user="admin",  # MySQL username
    passwd="1234567890",  # MySQL password
    database="pythonsql"  # Replace with your database name
)

cursor = mydb.cursor()
sql = "INSERT INTO tb_siswa (nis, nama_siswa, kelas) VALUES (%s, %s, %s)"
val = ("A001", "Rangga Saputra", "X RPL 2")

cursor.execute(sql, val)
mydb.commit()
print("Data added successfully!")
