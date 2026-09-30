from datetime import date

from database import get_connection
from validation import validate_amount, validate_category


def add_income(student_id, amount, source, description="", transaction_date=None):
    amount = validate_amount(amount)
    source = validate_category(source)

    # default to today if no date was given
    if transaction_date is None:
        transaction_date = str(date.today())

    con = get_connection()
    try:
        con.execute(
            """
            INSERT INTO transactions
                (student_id, transaction_type, amount, category, description, transaction_date)
            VALUES (?, 'income', ?, ?, ?, ?)
            """,
            (student_id, amount, source, description, transaction_date),
        )
        con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()


def get_income(student_id):
    """Return all income records for a student, newest first."""
    con = get_connection()
    try:
        return con.execute(
            """
            SELECT id, student_id, amount, category, description, transaction_date
            FROM transactions
            WHERE student_id = ? AND transaction_type = 'income'
            ORDER BY transaction_date DESC
            """,
            (student_id,),
        ).fetchall()
    finally:
        con.close()


def get_income_record(income_id, student_id):
    """Return a single income record, or None if it doesn't exist."""
    con = get_connection()
    try:
        return con.execute(
            """
            SELECT id, student_id, amount, category, description, transaction_date
            FROM transactions
            WHERE id = ? AND student_id = ? AND transaction_type = 'income'
            """,
            (income_id, student_id),
        ).fetchone()
    finally:
        con.close()


def update_income(income_id, amount, source, description=""):
    amount = validate_amount(amount)
    source = validate_category(source)

    con = get_connection()
    try:
        cursor = con.execute(
            """
            UPDATE transactions
            SET amount = ?, category = ?, description = ?
            WHERE id = ? AND transaction_type = 'income'
            """,
            (amount, source, description, income_id),
        )

        if cursor.rowcount == 0:
            raise ValueError("Income record not found.")

        con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()


def delete_income(income_id):
    con = get_connection()
    try:
        cursor = con.execute(
            "DELETE FROM transactions WHERE id = ? AND transaction_type = 'income'",
            (income_id,),
        )

        if cursor.rowcount == 0:
            raise ValueError("Income record not found.")

        con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()


def get_total_income(student_id):
    con = get_connection()
    try:
        row = con.execute(
            """
            SELECT SUM(amount)
            FROM transactions
            WHERE student_id = ? AND transaction_type = 'income'
            """,
            (student_id,),
        ).fetchone()
    finally:
        con.close()

    # SUM returns NULL when there are no rows
    return row[0] or 0


def get_income_by_source(student_id, source):
    source = validate_category(source)

    con = get_connection()
    try:
        return con.execute(
            """
            SELECT id, amount, category, description, transaction_date
            FROM transactions
            WHERE student_id = ? AND transaction_type = 'income' AND category = ?
            ORDER BY transaction_date DESC
            """,
            (student_id, source),
        ).fetchall()
    finally:
        con.close()
        