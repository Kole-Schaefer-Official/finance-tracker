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

def delete_transaction(transaction):
    try:
        transactions.remove(transaction)
    except ValueError:
        print("Error. Transaction not found.")

def edit_transaction(transaction, new_amount):
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


transaction1 = Transaction("Publix", 45.72, "Food", "Spending", "09/08/2026 2:30 PM")
transaction2 = Transaction("Bostons on the Beach", 1500, "Paycheck", "Income", "09/01/2026 3:00 AM")
transaction3 = Transaction("Shell", 40, "Gas", "Spending", "09/09/2026 2:14 AM")
transaction4 = Transaction("Costco", -256.87, "Food", "Spending", "09/09/2026 2:44 AM")
transaction5 = Transaction("Walmart", 105.06, "Shopping", "Banana", "09/09/2026 2:53 AM")

transactions = [transaction1, transaction2]

add_transaction(transaction3)
add_transaction(transaction4)
add_transaction(transaction5)

delete_transaction(transaction1)
delete_transaction(transaction1)

edit_transaction(transaction3, 50)

view_transactions()

print(calculate_income())
print(calculate_spending())
print(calculate_balance())

print(calculate_category_totals())