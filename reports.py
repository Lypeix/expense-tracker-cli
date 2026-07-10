from datetime import datetime

def spending_by_category(expenses):

    result = {}

    for expense in expenses:

        category = expense.category

        if category not in result:
            result[category] = 0

        result[category] += expense.amount

    return result 

def expenses_by_month(expenses, month):
    result = []

    for expense in expenses:
        date = datetime.strptime(expense.date, "%d-%m-%Y")

        if date.month == month:
            result.append(expense)

    return result
