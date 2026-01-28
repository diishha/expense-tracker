from flask import Flask, render_template, request, redirect
from expense_tracker import read_expenses, write_expenses

app = Flask(__name__)

# Home page – show all expenses
@app.route("/")
def home():
    expenses = read_expenses()
    return render_template("index.html", expenses=expenses)


# Add expense page
@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        expenses = read_expenses()

        new_expense = {
            "id": len(expenses) + 1,
            "date": request.form["date"],
            "amount": request.form["amount"],
            "category": request.form["category"],
            "note": request.form["note"]
        }

        expenses.append(new_expense)
        write_expenses(expenses)

        return redirect("/")

    return render_template("add.html")


# Delete expense
@app.route("/delete/<int:expense_id>")
def delete_expense(expense_id):
    expenses = read_expenses()

    updated_expenses = []
    for expense in expenses:
        if int(expense["id"]) != expense_id:
            updated_expenses.append(expense)

    write_expenses(updated_expenses)
    return redirect("/")

# Edit expense
@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit_expense(expense_id):
    expenses = read_expenses()

    # Find the expense to edit
    expense_to_edit = None
    for expense in expenses:
        if int(expense["id"]) == expense_id:
            expense_to_edit = expense
            break

    if not expense_to_edit:
        return redirect("/")  # if ID not found

    if request.method == "POST":
        # Update values
        expense_to_edit["date"] = request.form["date"]
        expense_to_edit["amount"] = request.form["amount"]
        expense_to_edit["category"] = request.form["category"]
        expense_to_edit["note"] = request.form["note"]

        write_expenses(expenses)  # save updated list
        return redirect("/")

    return render_template("edit.html", expense=expense_to_edit)

from collections import defaultdict
from datetime import datetime

# Monthly summary
@app.route("/summary")
def monthly_summary():
    expenses = read_expenses()

    summary = defaultdict(float)  # month → total

    for expense in expenses:
        # Convert date string to month name e.g., '2026-01-28' → 'Jan 2026'
        date_obj = datetime.strptime(expense["date"], "%Y-%m-%d")
        month_str = date_obj.strftime("%b %Y")
        summary[month_str] += float(expense["amount"])

    # Sort summary by month
    summary = dict(sorted(summary.items(), key=lambda x: datetime.strptime(x[0], "%b %Y")))

    return render_template("summary.html", summary=summary)


if __name__ == "__main__":
    app.run(debug=True)
