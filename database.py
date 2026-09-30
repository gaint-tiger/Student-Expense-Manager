import sqlite3
from pathlib import Path


# Database file ka path
DB_PATH = Path(__file__).parent / "data" / "expense_manager.db"


def get_connection():
    """
    SQLite database se connection create karta hai.
    """

    # Agar data folder exist nahi karta hai
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)

    # Database rows ko dictionary-like format mein access karne ke liye
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Required database tables create karta hai.
    """

    connection = get_connection()
    cursor = connection.cursor()

    # Student table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            monthly_budget REAL NOT NULL DEFAULT 0
        )
    """)

    # Income aur Expense dono ke liye transactions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            transaction_type TEXT NOT NULL
                CHECK(transaction_type IN ('income', 'expense')),
            amount REAL NOT NULL
                CHECK(amount > 0),
            category TEXT NOT NULL,
            description TEXT,
            transaction_date TEXT NOT NULL,

            FOREIGN KEY(student_id)
                REFERENCES students(id)
        )
    """)

    connection.commit()
    connection.close()


def close_connection(connection):
    """
    Database connection close karta hai.
    """

    if connection:
        connection.close()


# Directly file run karne par database initialize hoga
if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")