from models import Expense, ExpenseTracker

def main():
    tracker = ExpenseTracker()

    expense_1 = Expense("Pizza", 30, "food", "2026-07-01")
    expense_2 = Expense("Manga", 55, "entertainment", "2026-06-30")

    tracker.add_expense(expense_1)
    tracker.add_expense(expense_2)

    for expense in tracker.expenses:
        print(f"{expense.name} - {expense.amount} PLN - {expense.category} - {expense.date}")

    print(f"Total spent: {tracker.get_total_spent()} PLN")

if __name__ == "__main__":
    main()

    
