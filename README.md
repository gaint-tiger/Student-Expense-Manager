# Student Expense Manager

## 1. Project Overview

Student Expense Manager is a Python-based application designed to help students manage their personal finances. It allows students to record their income and expenses, maintain a monthly budget, and view financial summaries.

The application uses Python for its core functionality and SQLite for storing student and transaction data.

## 2. Objectives

* To help students maintain a record of their income and expenses.
* To organize expenses into categories.
* To track monthly budgets.
* To calculate total income, total expenses, and current balance.
* To generate financial reports for better expense tracking.

## 3. Features

* **Student Profile:** Create and manage student information.
* **Expense Management:** Add, view, update, and delete expenses.
* **Income Management:** Record and view income sources.
* **Budget Management:** Set and update a monthly budget.
* **Financial Reports:** View income, expenses, balance, and budget status.
* **Category-wise Analysis:** View expenses grouped by category.
* **Data Persistence:** Store records in an SQLite database.
* **Input Validation:** Validate amounts, names, and categories.

## 4. Technologies Used

* **Programming Language:** Python
* **Database:** SQLite
* **Libraries:** `sqlite3`, `datetime`, `pathlib`, `unittest`

## 5. Project Structure

```text
StudentExpenseManager/
│
├── main.py
├── database.py
├── student.py
├── validation.py
├── expense.py
├── income.py
├── analytics.py
├── reports.py
├── README.md
├── statement.md
│
├── data/
│   └── expense_manager.db
│
└── tests/
    └── test_expense.py
```

## 6. Installation and Setup

### Requirements

* Python 3.8 or later
* No external Python packages are required for the core application.

### Steps

1. Download or clone the project repository.
2. Open a terminal in the project folder.
3. Run the application:

```bash
python main.py
```

The SQLite database is initialized automatically when the application starts. The database is stored in the `data/` directory.

## 7. How to Use

1. Run `main.py`.
2. Create a student profile when prompted.
3. Select an option from the main menu.
4. Add income and expenses as required.
5. Set or update the monthly budget.
6. Select the financial report option to view a summary.
7. Select Exit to close the application.

## 8. Testing

Run the unit tests from the project directory:

```bash
python -m unittest discover tests
```

The tests cover input validation, including valid and invalid amounts, names, categories, email addresses, and transaction types.

## 9. Database Design

The application uses an SQLite database containing two main tables:

### Students

Stores student profile information, including name, email, and monthly budget.

### Transactions

Stores income and expense records, including transaction type, amount, category, description, date, and associated student ID.

## 10. Future Enhancements

* Graphical user interface
* Graphs and charts for expense visualization
* Monthly and yearly filtering
* Export reports to CSV or PDF
* Password-based user authentication
* Savings goals and spending alerts

## 11. Conclusion

Student Expense Manager provides a simple way for students to organize their finances. By combining transaction management, budget tracking, and financial reporting, the application encourages better awareness of personal spending.
