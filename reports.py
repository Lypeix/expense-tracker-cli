def get_total_spent(expenses):
    total = 0

    for expense in expenses:
        total += expense.amount

    return total


def filter_by_category(expenses, category):

    filtered_expenses = []

    for expense in expenses:
        if expense.category == category:
            filtered_expenses.append(expense)

    return filtered_expenses 

def filter_by_month(expenses, month):
    filtered_expenses = []

    for expense in expenses:
        if expense.date[3:5] == month:
            filtered_expenses.append(expense)

    print(expense.date, expense.date[3:5], month)

    return filtered_expenses
    
