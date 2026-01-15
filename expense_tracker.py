import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
FIELDNAMES = ["id", "date", "amount", "category", "note"]

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

def read_expenses():
    with open(FILE_NAME, "r") as file:
        return list(csv.DictReader(file))

def write_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense():
    expenses = read_expenses()
    expense_id = len(expenses) + 1
    date = input("Date (YYYY-MM-DD): ")
    amount = float(input("Amount: "))
    category = input("Category: ")
    note = input("Note: ")

    expenses.append({
        "id": expense_id,
        "date": date,
        "amount": amount,
        "category": category,
        "note": note
    })

    write_expenses(expenses)
    print("✅ Expense added!")

def edit_expense():
    expenses = read_expenses()
    eid = input("Enter expense ID to edit: ")

    for expense in expenses:
        if expense["id"] == eid:
            expense["amount"] = input("New amount: ")
            expense["category"] = input("New category: ")
            expense["note"] = input("New note: ")
            write_expenses(expenses)
            print("✏️ Expense updated!")
            return

    print("❌ Expense not found")

def delete_expense():
    expenses = read_expenses()
    eid = input("Enter expense ID to delete: ")

    expenses = [e for e in expenses if e["id"] != eid]
    write_expenses(expenses)
    print("🗑️ Expense deleted!")

def category_summary():
    expenses = read_expenses()
    summary = {}

    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + float(e["amount"])

    print("\n📊 Category-wise Summary")
    for cat, total in summary.items():
        print(f"{cat}: ₹{total}")

def monthly_summary():
    expenses = read_expenses()

    if not expenses:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:
        date = expense["date"]      # YYYY-MM-DD
        month = date[:7]            # YYYY-MM
        amount = float(expense["amount"])

        if month in summary:
            summary[month] += amount
        else:
            summary[month] = amount

    print("\n📅 Monthly Expense Summary")
    print("-" * 30)
    for month, total in sorted(summary.items()):
        print(f"{month} : ₹{total:.2f}")


def menu():
    print("""
==== Expense Tracker ====
1. Add Expense
2. Edit Expense
3. Delete Expense
4. Category Summary
5. Monthly Summary
6. Exit
""")

def main():
    initialize_file()
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            edit_expense()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
