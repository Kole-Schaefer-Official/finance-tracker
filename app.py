from flask import Flask, render_template, request, redirect, url_for

from datetime import datetime

from finance_tracker import load_transactions, Transaction, add_transaction, delete_transaction

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        merchant = request.form["merchant"]
        amount = float(request.form["amount"])
        category = request.form["category"]
        spending_income = request.form["spending_income"]
        
        date_time = request.form["date_time"]
        date_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
        date_time = date_time.strftime("%m/%d/%Y %I:%M %p")

        transaction = Transaction(
            merchant,
            amount,
            category,
            spending_income, 
            date_time
        )

        add_transaction(transaction)

    transactions = load_transactions()
    return render_template("index.html", transactions=transactions)

@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete(transaction_id):
    delete_transaction(transaction_id)
    return redirect(url_for("home"))


@app.route("/about")
def about():
    return "This is my finance tracker."