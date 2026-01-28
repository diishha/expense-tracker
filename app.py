from flask import Flask, render_template, request, redirect
from expense_tracker import read_expenses, write_expenses

app = Flask(__name__)

@app.route("/")
def home():
    expenses = read_expenses()
    return render_template("index.html", expenses=expenses)

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

if __name__ == "__main__":
    app.run(debug=True)
