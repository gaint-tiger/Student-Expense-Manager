from database import get_connection
from validation import validate_name, validate_amount


def create_student(name, email, monthly_budget):
    """
    Naya student profile create karta hai.
    """

    # Student name validate karo
    name = validate_name(name)

    # Budget ko number mein convert karo
    budget = float(monthly_budget)

    # Budget negative nahi hona chahiye
    if budget < 0:
        raise ValueError("Monthly budget cannot be negative.")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO students
            (name, email, monthly_budget)
            VALUES (?, ?, ?)
        """, (
            name,
            email.strip(),
            budget
        ))

        student_id = cursor.lastrowid

        connection.commit()

        return student_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def get_student(student_id=1):
    """
    Student ID ke basis par student profile return karta hai.
    """

    connection = get_connection()

    student = connection.execute("""
        SELECT
            id,
            name,
            email,
            monthly_budget
        FROM students
        WHERE id = ?
    """, (student_id,)).fetchone()

    connection.close()

    return student


def update_budget(student_id, monthly_budget):
    """
    Student ka monthly budget update karta hai.
    """

    budget = validate_amount(monthly_budget)

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE students
        SET monthly_budget = ?
        WHERE id = ?
    """, (
        budget,
        student_id
    ))

    # Check karo student mila ya nahi
    if cursor.rowcount == 0:
        connection.close()
        raise ValueError("Student not found.")

    connection.commit()
    connection.close()


def update_student_profile(student_id, name, email):
    """
    Student ka name aur email update karta hai.
    """

    name = validate_name(name)

    connection = get_connection()

    try:
        connection.execute("""
            UPDATE students
            SET name = ?, email = ?
            WHERE id = ?
        """, (
            name,
            email.strip(),
            student_id
        ))

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def delete_student(student_id):
    """
    Student profile delete karta hai.
    """

    connection = get_connection()

    try:
        # Student ke transactions pehle delete karo
        connection.execute("""
            DELETE FROM transactions
            WHERE student_id = ?
        """, (student_id,))

        # Student profile delete karo
        cursor = connection.execute("""
            DELETE FROM students
            WHERE id = ?
        """, (student_id,))

        if cursor.rowcount == 0:
            raise ValueError("Student not found.")

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def get_all_students():
    """
    Database mein stored saare students return karta hai.
    """

    connection = get_connection()

    students = connection.execute("""
        SELECT
            id,
            name,
            email,
            monthly_budget
        FROM students
        ORDER BY id
    """).fetchall()

    connection.close()

    return students