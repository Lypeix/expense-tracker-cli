from models import Expense, ExpenseTracker
from utils import user_choice, get_float, choose_category, get_date
from storage import save_expenses, load_expenses, load_categories
from reports import spending_by_category


def create_expense_from_input(categories):
    name = input("Name: ")
    amount = get_float("Amount: ")
    category = choose_category(categories)
    date = get_date()

    return Expense(name, amount, category, date)


def main():
    tracker = ExpenseTracker()
    
    tracker.expenses = load_expenses()
    
    categories = load_categories()


    while True:
        action = user_choice("What would you like to do?"
                    "\n1. Add expense"
                    "\n2. Show expenses"
                    "\n3. Show total spent by category"
                    "\n4. Show total spent amount"
                    "\n5. Quit"
                    "\n> ",
                    ["1", "2", "3", "4", "5"]
                    )
        
        if action == "1":
            expense = create_expense_from_input(categories)
            tracker.add_expense(expense)
            save_expenses(tracker.expenses)

        elif action == "2":
            if len(tracker.expenses) == 0:
                print("You have no expenses!")
            else:
                for expense in tracker.expenses:
                    print(f"{expense.name} - {expense.amount} PLN - {expense.category} - {expense.date}")

        elif action == "3":
            if len(tracker.expenses) == 0:
                print("You have no expenses!")
            else:
                
                report = spending_by_category(tracker.expenses)  

                for category, amount in report.items():
                    print(f"Category: {category} |  PLN: {amount}")


        elif action == "4":
            if len(tracker.expenses) == 0:
                print("You have no expenses!")
            else:
                print(f"Total spent: {tracker.get_total_spent()} PLN")

        elif action == "5":
            break

if __name__ == "__main__":
    main()

