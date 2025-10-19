import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update with your credentials if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # left empty intentionally (no password prompt)
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
