# Project Statement: Student Expense Manager

## 1. Project Title

**Student Expense Manager**

## 2. Problem Statement

Students often receive money from sources such as pocket money, scholarships, and part-time jobs. They also spend money on food, travel, education, accommodation, and other personal needs.

Managing these transactions manually can make it difficult to track total spending, understand spending patterns, and stay within a budget.

The Student Expense Manager aims to provide a simple software solution that allows students to record their income and expenses, maintain a monthly budget, and review their financial position.

## 3. Objectives

* To provide a structured system for recording income and expenses.
* To allow students to organize expenses by category.
* To help students set and monitor a monthly budget.
* To calculate income, expenses, and available balance.
* To generate financial summaries and category-wise reports.
* To store financial records persistently using a database.

## 4. Scope of the Project

The project focuses on basic personal finance management for students.

The system supports:

* Student profile creation
* Adding, viewing, updating, and deleting expense records
* Recording and viewing income
* Setting and updating a monthly budget
* Generating financial reports
* Category-wise expense and income summaries
* Storing records in an SQLite database

The current application is a command-line program developed using Python. Advanced features such as online banking integration, cloud synchronization, and automated bank transactions are outside the current scope.

## 5. Target Users

The primary target users are:

* College and university students
* School students who manage personal allowances
* Students receiving scholarships or pocket money
* Students who want to monitor their personal spending

## 6. High-Level Features

| Feature             | Description                            |
| ------------------- | -------------------------------------- |
| Student Profile     | Stores basic student information       |
| Expense Management  | Records and manages expenses           |
| Income Management   | Records income and its source          |
| Budget Management   | Sets and updates the monthly budget    |
| Financial Reporting | Displays income, expenses, and balance |
| Expense Analysis    | Groups expenses by category            |
| Database Storage    | Saves records using SQLite             |
| Input Validation    | Helps prevent invalid input            |

## 7. Functional Requirements

1. The system shall allow a student profile to be created.
2. The system shall allow expenses to be added, viewed, updated, and deleted.
3. The system shall allow income records to be added and viewed.
4. The system shall allow the monthly budget to be set or updated.
5. The system shall calculate total income and total expenses.
6. The system shall calculate the current balance.
7. The system shall display a financial report.
8. The system shall store records in an SQLite database.

## 8. Non-Functional Requirements

* **Usability:** The menu-driven interface should be simple to understand.
* **Reliability:** Financial records should be stored persistently.
* **Maintainability:** The application should use separate modules for different responsibilities.
* **Error Handling:** Invalid inputs should be handled with appropriate error messages.
* **Performance:** Basic database operations and reports should execute efficiently for typical student records.
* **Data Integrity:** Database constraints and parameterized SQL queries should help protect stored data.

## 9. Technologies Used

* Python
* SQLite
* Python standard libraries

## 10. Expected Outcome

The expected outcome is a working application that enables students to maintain financial records, monitor spending against a budget, and review their overall financial position through reports.

The project demonstrates modular Python programming, database operations, input validation, CRUD operations, and basic data analysis.
