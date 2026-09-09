# Personal Finance Tracker and Budget System

class Transaction:
    def __init__(self, merchant, amount, category, spending_income, date_time):
        self.merchant = merchant
        self.amount = amount
        self.category = category
        self.spending_income = spending_income
        self.date_time = date_time

def add_transaction(transaction):
    if transaction.amount <= 0:
        print("Error. The amount must be greater than $0.")
    elif transaction.spending_income != "Income" and transaction.spending_income != "Spending":
        print("Error. Must be Income or Spending.")
    else:
        transactions.append(transaction)

def view_transactions():
    for transaction in transactions:
        print(f"{transaction.merchant} {transaction.amount} {transaction.spending_income} {transaction.category} {transaction.date_time}")

transaction1 = Transaction("Publix", 45.72, "Food", "Spending", "09/08/2026 2:30 PM")
transaction2 = Transaction("Bostons on the Beach", 1500, "Paycheck", "Income", "09/01/2026 3:00 AM")
transaction3 = Transaction("Shell", 40, "Gas", "Spending", "09/09/2026 2:14 AM")
transaction4 = Transaction("Costco", -256.87, "Food", "Spending", "09/09/2026 2:44 AM")
transaction5 = Transaction("Walmart", 105.06, "Shopping", "Banana", "09/09/2026 2:53 AM")

transactions = [transaction1, transaction2]

add_transaction(transaction3)
add_transaction(transaction4)
add_transaction(transaction5)

view_transactions()
