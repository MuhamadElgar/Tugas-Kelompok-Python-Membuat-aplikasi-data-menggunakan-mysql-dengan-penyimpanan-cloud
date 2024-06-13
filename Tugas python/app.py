import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",  # Localhost address
        user="admin",  # MySQL username
        passwd="1234567890",  # MySQL password
        database="pythonsql"  # Replace with your database name
    )

def insert_data():
    mydb = connect()
    cursor = mydb.cursor()
    nis = input("Enter NIS: ")
    nama = input("Enter Name: ")
    kelas = input("Enter Class: ")
    sql = "INSERT INTO tb_siswa (nis, nama_siswa, kelas) VALUES (%s, %s, %s)"
    val = (nis, nama, kelas)
    cursor.execute(sql, val)
    mydb.commit()
    print("Data added successfully!")

def display_data():
    mydb = connect()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM tb_siswa")
    results = cursor.fetchall()
    for row in results:
        print(row)

def update_data():
    mydb = connect()
    cursor = mydb.cursor()
    nis = input("Enter NIS of the student to update: ")
    nama = input("Enter new name: ")
    kelas = input("Enter new class: ")
    sql = "UPDATE tb_siswa SET nama_siswa=%s, kelas=%s WHERE nis=%s"
    val = (nama, kelas, nis)
    cursor.execute(sql, val)
    mydb.commit()
    print("Data updated successfully!")

def delete_data():
    mydb = connect()
    cursor = mydb.cursor()
    nis = input("Enter NIS of the student to delete: ")
    sql = "DELETE FROM tb_siswa WHERE nis=%s"
    val = (nis,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Data deleted successfully!")

def search_data():
    mydb = connect()
    cursor = mydb.cursor()
    nis = input("Enter NIS of the student to search: ")
    sql = "SELECT * FROM tb_siswa WHERE nis=%s"
    val = (nis,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result:
        print(result)
    else:
        print("No data found")

def main_menu():
    while True:
        print("=== APLIKASI DATABASE PYTHON ===")
        print("1. Insert Data")
        print("2. Display Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Search Data")
        print("0. Exit")
        choice = input("Choose menu: ")
        
        if choice == '1':
            insert_data()
        elif choice == '2':
            display_data()
        elif choice == '3':
            update_data()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            search_data()
        elif choice == '0':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()