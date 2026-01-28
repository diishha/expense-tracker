# Expense Tracker Web App

A simple **Expense Tracker** built with **Python Flask**.  
Track your expenses, edit, delete, and view monthly summaries — all in a clean, interactive web interface.

---

## **Features**

- Add new expenses (Date, Amount, Category, Note)  
- Edit existing expenses  
- Delete expenses  
- View all expenses in a table with alternating row colors and hover effects  
- Monthly summary showing total expenses per month  
- Fully styled with CSS (modern buttons, hover effects, responsive table)  

---

## **Tech Stack**

- Python 3  
- Flask  
- HTML / CSS (basic styling)  
- CSV file for local data storage  

---

## **Project Structure**

expense-tracker/
│
├─ app.py # Main Flask application
├─ expense_tracker.py # CSV read/write utility
├─ expenses.csv # Expense data storage
├─ templates/ # HTML templates
│ ├─ index.html
│ ├─ add.html
│ ├─ edit.html
│ └─ summary.html
└─ static/
└─ style.css # CSS styling


---

## **How to Run Locally**

1. Clone the repository:
git clone <your-repo-link>
cd expense-tracker

2. Install Flask (if not installed):
pip install flask

3. Run the app:
python app.py

4. Open your browser:
http://127.0.0.1:5000