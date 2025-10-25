# main.py
import mysql.connector
from db import operations


def main():
    db_name = None
    while True:
        print("\n=== MySQL CLI App ===")
        print("1. Create Database")
        print("2. Create Table")
        print("3. Insert Data")
        print("4. Select All")
        print("5. Select by Name")
        print("6. Delete by Name")
        print("7. Exit")

        choice = input("Choose an action: ")

        try:
            if choice == "1":
                db_name = input("Enter database name: ")
                operations.create_database(db_name)

            elif choice == "2":
                if not db_name:
                    db_name = input("Enter database name: ")
                operations.create_table(db_name)

            elif choice == "3":
                if not db_name:
                    db_name = input("Enter database name: ")
                name = input("Enter name: ")
                address = input("Enter address: ")
                operations.insert_customer(db_name, name, address)

            elif choice == "4":
                if not db_name:
                    db_name = input("Enter database name: ")
                operations.select_all(db_name)

            elif choice == "5":
                if not db_name:
                    db_name = input("Enter database name: ")
                name = input("Enter name to search: ")
                operations.select_by_name(db_name, name)

            elif choice == "6":
                if not db_name:
                    db_name = input("Enter database name: ")
                name = input("Enter name to delete: ")
                operations.delete_by_name(db_name, name)

            elif choice == "7":
                print("Goodbye!")
                break

            else:
                print("❌ Invalid choice, try again.")

        except mysql.connector.Error as err:
            print(f"⚠️ MySQL Error: {err}")

        except Exception as e:
            print(f"⚠️ Unexpected Error: {e}")


if __name__ == "__main__":
    main()
