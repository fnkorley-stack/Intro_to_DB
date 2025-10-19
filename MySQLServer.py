#!/usr/bin/python3
"""
A simple Python script to create the 'alx_book_store' database.
"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (no specific database yet)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aigle@2025'  # ← replace with your MySQL root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close cursor and connection properly
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
