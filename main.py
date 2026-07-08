from models import Expense, ExpenseTracker
from utils import user_choice, get_float
from storage import save_expenses, load_expenses

def create_expense_from_input():
    name = input("Name: ")
    amount = get_float("Amount: ")
    category = input("Category: ")
    date = input("Date: ")

    return Expense(name, amount, category, date)

def main():
    tracker = ExpenseTracker()
    tracker.expenses = load_expenses()
    


    while True:
        action = user_choice("What would you like to do?"
                    "\n1. Add expense"
                    "\n2. Show expenses"
                    "\n3. Show total spent amount"
                    "\n4. Quit"
                    "\n> ",
                    ["1", "2", "3", "4"]
                    )
        
        if action == "1":
            expense = create_expense_from_input()
            tracker.add_expense(expense)
            save_expenses(tracker.expenses)

        elif action == "2":
            if len(tracker.expenses) == 0:
                print("You have no expenses!")
            else:
                for expense in tracker.expenses:
                    print(f"{expense.name} - {expense.amount} PLN - {expense.category} - {expense.date}")

        elif action == "3":
            print(f"Total spent: {tracker.get_total_spent()} PLN")

        elif action == "4":
            break

if __name__ == "__main__":
    main()

    
