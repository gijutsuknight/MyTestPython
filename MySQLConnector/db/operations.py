# db/operations.py
from .connection import get_connection


def create_database(db_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    print(f"Database '{db_name}' created (if not existed).")
    cursor.close()
    conn.close()


def create_table(db_name):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS customers
                   (
                       name
                       VARCHAR
                   (
                       255
                   ),
                       address VARCHAR
                   (
                       255
                   )
                       )
                   """)
    print("Table 'customers' created (if not existed).")
    cursor.close()
    conn.close()


def insert_customer(db_name, name, address):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", (name, address))
    conn.commit()
    print(f"Inserted customer: {name}")
    cursor.close()
    conn.close()


def select_all(db_name):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()


def select_by_name(db_name, name):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE name = %s", (name,))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()


def delete_by_name(db_name, name):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE name = %s", (name,))
    conn.commit()
    print(f"Deleted records with name: {name}")
    cursor.close()
    conn.close()
