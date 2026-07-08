from models import Expense
import json

def save_expenses(expenses):
    data = []

    for expense in expenses:
        data.append({
            "name": expense.name,
            "amount": expense.amount,
            "category": expense.category,
            "date": expense.date
            })
        
    with open("expenses.json", "w") as file:
        json.dump(data, file, indent=4)

def load_expenses():
    
    try:
        with open("expenses.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError, json.JSONDecodeError:
        return []
    
    expenses = []

    for item in data:
        expense = Expense(
            item['name'],
            item['amount'],
            item['category'],
            item['date']
        )

        expenses.append(expense)

    return expenses
