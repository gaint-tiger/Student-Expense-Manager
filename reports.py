from analytics import (
    get_summary,
    category_wise_expenses,
    category_wise_income,
    get_highest_expense_category,
    get_transaction_count
)


def print_report(student_id):
    """Display complete financial report."""

    summary = get_summary(student_id)

    print("\n")
    print("=" * 55)
    print("              STUDENT FINANCIAL REPORT")
    print("=" * 55)

    print(f"Total Income        : ₹{summary['income']:.2f}")
    print(f"Total Expenses      : ₹{summary['expense']:.2f}")
    print(f"Current Balance     : ₹{summary['balance']:.2f}")
    print(f"Monthly Budget      : ₹{summary['budget']:.2f}")
    print(f"Budget Remaining    : ₹{summary['budget_remaining']:.2f}")

    print("-" * 55)

    # Category-wise expenses
    print("\nCATEGORY-WISE EXPENSES")
    print("-" * 55)

    expenses = category_wise_expenses(student_id)

    if not expenses:
        print("No expenses recorded.")
    else:
        for row in expenses:
            print(
                f"{row['category']:<25}"
                f"₹{row['total']:>10.2f}"
            )

    # Income sources
    print("\nINCOME SOURCES")
    print("-" * 55)

    income_sources = category_wise_income(student_id)

    if not income_sources:
        print("No income records found.")
    else:
        for row in income_sources:
            print(
                f"{row['category']:<25}"
                f"₹{row['total']:>10.2f}"
            )

    # Highest expense
    print("\nHIGHEST EXPENSE CATEGORY")
    print("-" * 55)

    highest = get_highest_expense_category(student_id)

    if highest:
        print(
            f"{highest['category']} "
            f"→ ₹{highest['total']:.2f}"
        )
    else:
        print("No expense data available.")

    # Transaction count
    total_transactions = get_transaction_count(student_id)

    print("\nTRANSACTION SUMMARY")
    print("-" * 55)
    print(f"Total Transactions : {total_transactions}")

    # Budget status
    print("\nBUDGET STATUS")
    print("-" * 55)

    if summary["budget"] <= 0:
        print("Monthly budget has not been set.")

    elif summary["expense"] > summary["budget"]:
        exceeded = summary["expense"] - summary["budget"]

        print("WARNING: Monthly budget exceeded!")
        print(f"Amount exceeded   : ₹{exceeded:.2f}")

    else:
        remaining = summary["budget"] - summary["expense"]

        print("Budget is within limit.")
        print(f"Amount remaining  : ₹{remaining:.2f}")

    # Balance status
    print("\nBALANCE STATUS")
    print("-" * 55)

    if summary["balance"] > 0:
        print(
            f"Positive balance: "
            f"₹{summary['balance']:.2f}"
        )

    elif summary["balance"] < 0:
        print(
            f"Negative balance: "
            f"₹{abs(summary['balance']):.2f}"
        )

    else:
        print("Balance is zero.")

    print("=" * 55)
    print("              END OF REPORT")
    print("=" * 55)
    print()

    input("Press Enter to return to the main menu...")