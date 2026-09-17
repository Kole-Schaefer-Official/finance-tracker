# Personal Finance Tracker and Budget System

from datetime import datetime
import sqlite3

connection = sqlite3.connect("finance_tracker.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY,
        merchant TEXT,
        amount REAL,
        category TEXT,
        spending_income TEXT,
        date_time TEXT
    )
""")

connection.commit()

class Transaction:
    def __init__(self, merchant, amount, category, spending_income, date_time, transaction_id=None):
        self.merchant = merchant
        self.amount = amount
        self.category = category
        self.spending_income = spending_income
        self.date_time = datetime.strptime(date_time, "%m/%d/%Y %I:%M %p")
        self.id = transaction_id

def add_transaction(transaction):
    if transaction.amount <= 0:
        print("Error. The amount must be greater than $0.")
    elif transaction.spending_income != "Income" and transaction.spending_income != "Spending":
        print("Error. Must be Income or Spending.")
    else:
        connection = sqlite3.connect("finance_tracker.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO transactions (merchant, amount, category, spending_income, date_time)
            VALUES (?, ?, ?, ?, ?) 
        """, (
            transaction.merchant,
            transaction.amount,
            transaction.category, 
            transaction.spending_income,
            transaction.date_time.strftime("%m/%d/%Y %I:%M %p")
        ))

        transaction.id = cursor.lastrowid

        connection.commit()
        connection.close()
        transactions.append(transaction)

def load_transactions():
    connection = sqlite3.connect("finance_tracker.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()

    connection.close()

    loaded_transactions = []

    for row in rows:
        transaction = Transaction(
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[0]
        )

        loaded_transactions.append(transaction)
    
    return loaded_transactions

def view_transactions():
    for transaction in transactions:
        print(f"{transaction.merchant} {transaction.amount} {transaction.spending_income} {transaction.category} {transaction.date_time}")

def delete_transaction(transaction_id):
    connection = sqlite3.connect("finance_tracker.db")
    cursor = connection.cursor()
    

    cursor.execute("""
        DELETE FROM transactions
        WHERE id = ?
    """, (
        transaction_id,
    ))

    connection.commit()
    connection.close()

def edit_transaction(transaction, new_amount):
    if new_amount <= 0:
        print("Error. The amount must be greater than $0.")
    else:
        cursor.execute("""
            UPDATE transactions
            SET amount = ?
            WHERE id = ?
        """, (
            new_amount,
            transaction.id,    
        ))

        connection.commit()
        transaction.amount = new_amount

def calculate_income():
    total_income = 0
    for transaction in transactions:
        if transaction.spending_income == "Income":
            total_income += transaction.amount
    return total_income

def calculate_spending():
    total_spending = 0
    for transaction in transactions:
        if transaction.spending_income == "Spending":
            total_spending += transaction.amount
    return total_spending

def calculate_balance():
    return calculate_income() - calculate_spending()

def calculate_category_totals():
    category_totals = {}
    for transaction in transactions:
        if transaction.spending_income == "Spending":
            category = transaction.category
            if category in category_totals:
                category_totals[category] += transaction.amount
            else:
                category_totals[category] = transaction.amount
    return category_totals

def filter_transactions_by_month(month, year):
    filtered_transactions = []

    for transaction in transactions:
        if transaction.date_time.month == month and transaction.date_time.year == year:
            filtered_transactions.append(transaction)
    return filtered_transactions

def calculate_monthly_spending(month, year):
    monthly_transactions = filter_transactions_by_month(month, year)
    month_total = 0

    for transaction in monthly_transactions:
        if transaction.spending_income == "Spending":
            month_total += transaction.amount
    return month_total

transactions = load_transactions()

