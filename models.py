class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_spent(self):
        total = 0 

        for expense in self.expenses:
            total += expense.amount

        return total
    

