import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mypassword" 
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn’t exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL or creating database: {e}")

    finally:
        # Close cursor and connection safely
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional confirmation message
            # print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
