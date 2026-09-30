from database import get_connection


def get_summary(student_id):
    """Return complete financial summary for a student."""

    connection = get_connection()

    try:
        income_result = connection.execute("""
            SELECT COALESCE(SUM(amount), 0) AS total_income
            FROM transactions
            WHERE student_id = ?
            AND transaction_type = 'income'
        """, (student_id,)).fetchone()

        expense_result = connection.execute("""
            SELECT COALESCE(SUM(amount), 0) AS total_expense
            FROM transactions
            WHERE student_id = ?
            AND transaction_type = 'expense'
        """, (student_id,)).fetchone()

        student = connection.execute("""
            SELECT monthly_budget
            FROM students
            WHERE id = ?
        """, (student_id,)).fetchone()

        total_income = float(income_result["total_income"] or 0)
        total_expense = float(expense_result["total_expense"] or 0)

        if student:
            monthly_budget = float(student["monthly_budget"] or 0)
        else:
            monthly_budget = 0.0

        balance = total_income - total_expense
        budget_remaining = monthly_budget - total_expense

        return {
            "income": total_income,
            "expense": total_expense,
            "balance": balance,
            "budget": monthly_budget,
            "budget_remaining": budget_remaining
        }

    finally:
        connection.close()


def category_wise_expenses(student_id):
    """Return expenses grouped by category."""

    connection = get_connection()

    try:
        return connection.execute("""
            SELECT
                category,
                COALESCE(SUM(amount), 0) AS total
            FROM transactions
            WHERE student_id = ?
            AND transaction_type = 'expense'
            GROUP BY category
            ORDER BY total DESC
        """, (student_id,)).fetchall()

    finally:
        connection.close()


def category_wise_income(student_id):
    """Return income grouped by source."""

    connection = get_connection()

    try:
        return connection.execute("""
            SELECT
                category,
                COALESCE(SUM(amount), 0) AS total
            FROM transactions
            WHERE student_id = ?
            AND transaction_type = 'income'
            GROUP BY category
            ORDER BY total DESC
        """, (student_id,)).fetchall()

    finally:
        connection.close()


def get_highest_expense_category(student_id):
    """Return category with the highest total expense."""

    connection = get_connection()

    try:
        return connection.execute("""
            SELECT
                category,
                SUM(amount) AS total
            FROM transactions
            WHERE student_id = ?
            AND transaction_type = 'expense'
            GROUP BY category
            ORDER BY total DESC
            LIMIT 1
        """, (student_id,)).fetchone()

    finally:
        connection.close()


def get_transaction_count(student_id):
    """Return total number of transactions."""

    connection = get_connection()

    try:
        result = connection.execute("""
            SELECT COUNT(*) AS total_transactions
            FROM transactions
            WHERE student_id = ?
        """, (student_id,)).fetchone()

        return result["total_transactions"]

    finally:
        connection.close()