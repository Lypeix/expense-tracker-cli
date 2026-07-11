from models import Expense, ExpenseTracker
from utils import user_choice, get_float, choose_category, get_date, get_month, get_name, del_expense
from storage import save_expenses, load_expenses, load_categories
from reports import get_total_spent, filter_by_category, filter_by_month


def create_expense_from_input(categories):

    name = get_name()

    if name is None:
        return None

    amount = get_float("Amount: ")
    category = choose_category(categories)
    date = get_date()

    return Expense(name, amount, category, date)


def show_total_spent_menu(tracker, categories):
    answer = user_choice("Show total: "
        "\n1. All expenses"
        "\n2. Filter by category"
        "\n3. Filter by month"
        "\n4. Exit"
        "\n> ",
        ["1", "2", "3", "4"]
        )
                
    if answer == "1":
        total = get_total_spent(tracker.expenses)
        print(f"Total spent: {total} PLN")
                
    elif answer == "2":
        category = choose_category(categories)
        filtered_expenses = filter_by_category(tracker.expenses, category)  
        total = get_total_spent(filtered_expenses)
        print(f"Total spent in {category}: {total} PLN")

    elif answer == "3":
        month = get_month()
        filtered_expenses = filter_by_month(tracker.expenses, month)
        total = get_total_spent(filtered_expenses)
        print(f"Total spent in {month}: {total} PLN")



    elif answer == "4":
        return

def action_loop():
    tracker = ExpenseTracker()
    
    tracker.expenses = load_expenses()
    
    categories = load_categories()


    while True:
        action = user_choice("What would you like to do?"
                    "\n1. Add expense"
                    "\n2. Show expenses"
                    "\n3. Show total spent amount"
                    "\n4. Delete expense"
                    "\n5. Quit"
                    "\n> ",
                    ["1", "2", "3", "4", "5"]
                    )
        
        if action == "1":
            expense = create_expense_from_input(categories)

            if expense == None:
                print("Process cancelled")
            else:
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
                show_total_spent_menu(tracker, categories)

        elif action == "4":
            del_expense(tracker)

        elif action == "5":
            break


def main():
    action_loop()

if __name__ == "__main__":
    main()

