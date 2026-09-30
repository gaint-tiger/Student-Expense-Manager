```python
from database import initialize_database
from student import create_student, get_student, update_budget
from expense import add_expense, get_expenses, update_expense, delete_expense
from income import add_income, get_income
from reports import print_report


def setup_student():
    """Create a student profile or load the existing one."""

    student = get_student(1)

    # If student already exists, use the same profile
    if student:
        print(f"\nWelcome back, {student['name']}!")
        return student["id"]

    print("\n" + "=" * 45)
    print("        CREATE STUDENT PROFILE")
    print("=" * 45)

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    budget = input("Enter your monthly budget (₹): ")

    try:
        student_id = create_student(name, email, budget)

        print("\nProfile created successfully!")
        print("Welcome to Student Expense Manager.")

        return student_id

    except Exception as error:
        print(f"\nUnable to create profile: {error}")
        return None


def show_expenses(student_id):
    """Show all expenses added by the student."""

    expenses = get_expenses(student_id)

    print("\n" + "=" * 70)
    print("                         MY EXPENSES")
    print("=" * 70)

    if not expenses:
        print("No expenses have been added yet.")
        return

    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"{expense['transaction_date']}"
        )


def show_income(student_id):
    """Show all income records."""

    income_records = get_income(student_id)

    print("\n" + "=" * 70)
    print("                         MY INCOME")
    print("=" * 70)

    if not income_records:
        print("No income records have been added yet.")
        return

    for record in income_records:
        print(
            f"ID: {record['id']} | "
            f"₹{record['amount']:.2f} | "
            f"{record['category']} | "
            f"{record['description']} | "
            f"{record['transaction_date']}"
        )


def add_new_expense(student_id):
    """Take expense details from the user."""

    print("\n" + "=" * 45)
    print("             ADD NEW EXPENSE")
    print("=" * 45)

    amount = input("Enter amount (₹): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        add_expense(
            student_id,
            amount,
            category,
            description
        )

        print("\nExpense added successfully!")

    except Exception as error:
        print(f"\nCould not add expense: {error}")


def update_existing_expense(student_id):
    """Update an expense already stored in the database."""

    show_expenses(student_id)

    try:
        expense_id = int(
            input("\nEnter the Expense ID you want to update: ")
        )

        amount = input("Enter new amount (₹): ")
        category = input("Enter new category: ")
        description = input("Enter new description: ")

        update_expense(
            expense_id,
            amount,
            category,
            description
        )

        print("\nExpense updated successfully!")

    except ValueError as error:
        print(f"\nInvalid input: {error}")

    except Exception as error:
        print(f"\nCould not update expense: {error}")


def delete_existing_expense(student_id):
    """Delete an expense after asking for confirmation."""

    show_expenses(student_id)

    try:
        expense_id = int(
            input("\nEnter the Expense ID you want to delete: ")
        )

        confirm = input(
            "Are you sure you want to delete this expense? (y/n): "
        ).strip().lower()

        if confirm == "y":
            delete_expense(expense_id)
            print("\nExpense deleted successfully!")

        else:
            print("\nDelete operation cancelled.")

    except ValueError:
        print("\nPlease enter a valid Expense ID.")

    except Exception as error:
        print(f"\nCould not delete expense: {error}")


def add_new_income(student_id):
    """Take income details from the user."""

    print("\n" + "=" * 45)
    print("              ADD NEW INCOME")
    print("=" * 45)

    amount = input("Enter income amount (₹): ")

    source = input(
        "Enter income source "
        "(Pocket Money/Scholarship/Part-time/etc.): "
    )

    description = input("Enter description: ")

    try:
        add_income(
            student_id,
            amount,
            source,
            description
        )

        print("\nIncome added successfully!")

    except Exception as error:
        print(f"\nCould not add income: {error}")


def change_budget(student_id):
    """Change the monthly spending budget."""

    print("\n" + "=" * 45)
    print("          UPDATE MONTHLY BUDGET")
    print("=" * 45)

    budget = input("Enter your new monthly budget (₹): ")

    try:
        update_budget(student_id, budget)
        print("\nMonthly budget updated successfully!")

    except Exception as error:
        print(f"\nCould not update budget: {error}")


def display_menu():
    """Display the options available to the user."""

    print("""
================================================
          STUDENT EXPENSE MANAGER
================================================

1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Add Income
6. View Income
7. Set / Update Monthly Budget
8. View Financial Report
9. Exit

================================================
""")


def main():
    """Start and run the Student Expense Manager."""

    # Create the database and required tables if needed
    initialize_database()

    # Load existing student or create a new profile
    student_id = setup_student()

    if student_id is None:
        print("\nApplication could not be started.")
        return

    while True:

        display_menu()

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_new_expense(student_id)

        elif choice == "2":
            show_expenses(student_id)

        elif choice == "3":
            update_existing_expense(student_id)

        elif choice == "4":
            delete_existing_expense(student_id)

        elif choice == "5":
            add_new_income(student_id)

        elif choice == "6":
            show_income(student_id)

        elif choice == "7":
            change_budget(student_id)

        elif choice == "8":
            try:
                print_report(student_id)
            except Exception as error:
                print(f"\nUnable to generate report: {error}")

        elif choice == "9":
            print("\nThank you for using Student Expense Manager!")
            print("Have a great day. Goodbye!")
            break

        else:
            print(
                "\nInvalid choice. "
                "Please select a number between 1 and 9."
            )


# Program starts from here
if __name__ == "__main__":
    main()
```
