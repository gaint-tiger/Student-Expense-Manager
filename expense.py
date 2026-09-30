from datetime import date

from database import get_connection
from validation import validate_amount, validate_category


def add_expense(
    student_id,
    amount,
    category,
    description="",
    transaction_date=None
):
    """
    New expense database mein add karta hai.
    """

    # Input validation
    amount = validate_amount(amount)
    category = validate_category(category)

    # Agar date nahi di gayi hai to today's date use hogi
    if transaction_date is None:
        transaction_date = str(date.today())

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO transactions
            (
                student_id,
                transaction_type,
                amount,
                category,
                description,
                transaction_date
            )
            VALUES (?, 'expense', ?, ?, ?, ?)
        """, (
            student_id,
            amount,
            category,
            description.strip(),
            transaction_date
        ))

        transaction_id = cursor.lastrowid

        connection.commit()

        return transaction_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def get_expenses(student_id):
    """
    Student ke saare expenses database se fetch karta hai.
    """

    connection = get_connection()

    expenses = connection.execute("""
        SELECT
            id,
            student_id,
            amount,
            category,
            description,
            transaction_date
        FROM transactions
        WHERE student_id = ?
        AND transaction_type = 'expense'
        ORDER BY transaction_date DESC, id DESC
    """, (student_id,)).fetchall()

    connection.close()

    return expenses


def get_expense(transaction_id, student_id):
    """
    Specific expense ki details return karta hai.
    """

    connection = get_connection()

    expense = connection.execute("""
        SELECT
            id,
            student_id,
            amount,
            category,
            description,
            transaction_date
        FROM transactions
        WHERE id = ?
        AND student_id = ?
        AND transaction_type = 'expense'
    """, (
        transaction_id,
        student_id
    )).fetchone()

    connection.close()

    return expense


def update_expense(
    transaction_id,
    amount,
    category,
    description=""
):
    """
    Existing expense ko update karta hai.
    """

    amount = validate_amount(amount)
    category = validate_category(category)

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE transactions
            SET
                amount = ?,
                category = ?,
                description = ?
            WHERE id = ?
            AND transaction_type = 'expense'
        """, (
            amount,
            category,
            description.strip(),
            transaction_id
        ))

        if cursor.rowcount == 0:
            raise ValueError(
                "Expense not found."
            )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def delete_expense(transaction_id):
    """
    Existing expense ko delete karta hai.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM transactions
            WHERE id = ?
            AND transaction_type = 'expense'
        """, (transaction_id,))

        if cursor.rowcount == 0:
            raise ValueError(
                "Expense not found."
            )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def get_total_expense(student_id):
    """
    Student ke total expenses calculate karta hai.
    """

    connection = get_connection()

    result = connection.execute("""
        SELECT
            COALESCE(SUM(amount), 0) AS total_expense
        FROM transactions
        WHERE student_id = ?
        AND transaction_type = 'expense'
    """, (student_id,)).fetchone()

    connection.close()

    return result["total_expense"]


def get_category_expenses(student_id, category):
    """
    Specific category ke expenses fetch karta hai.
    """

    category = validate_category(category)

    connection = get_connection()

    expenses = connection.execute("""
        SELECT
            id,
            amount,
            category,
            description,
            transaction_date
        FROM transactions
        WHERE student_id = ?
        AND transaction_type = 'expense'
        AND category = ?
        ORDER BY transaction_date DESC
    """, (
        student_id,
        category
    )).fetchall()

    connection.close()

    return expenses