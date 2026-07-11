from datetime import datetime
from storage import save_expenses


def user_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().lower()
        
        if choice in valid_choices:
            return choice
        else:
            print(f"Invalid choice! Choose from: {', '.join(valid_choices)}")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Value must be greater than zero!")
            else:
                return value

        except ValueError:
            print("Invalid number")


def choose_category(categories):
    categories = [
        "Bills",
        "Entertainment",
        "Food",
        "Transport",
        "Health",
        "Other"
    ]

    while True:
        print("Choose category")

        for idx, category in enumerate(categories, start=1):
            print(f"{idx}. {category}")

        choice = input("> ")
        
        if choice.isdigit():
            choice = int(choice)
        
            if 1 <= choice <= len(categories):
                return categories[choice - 1]

        print(f"Invalid number")

def get_date():

    while True:
        date = input("Date: (DD-MM-YYYY)")

        try:
            valid_date = datetime.strptime(date, "%d-%m-%Y")
            return valid_date.strftime("%d-%m-%Y")
        
        except ValueError:
            print("Invalid date format")

def get_month():
    while True:
        try:
            month = user_choice("Choose a month from from 1 to 12\n> ",
                                ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
                                )

                                
            return month.zfill(2)

            

        except ValueError:
            print("Invalid month! Choose from 1 to 12")

def get_name():
    while True:
        
        value = input("Name: ").strip()

        if value:
            return value
        
        else: 
            print("This field cannot be empty!") 


def del_expense(tracker):
    if len(tracker.expenses) == 0:
        print("You have no expenses to delete!")
        return

    else:

        for idx, expense in enumerate(tracker.expenses, start=1):
            print(f"{idx}. {expense.name} - {expense.amount} PLN - {expense.category} - {expense.date}")
        
        try:
            choice = int(input("Which expense would you like to delete? (Select the corresponding number)\n> "))

            if 1 <= choice <= len(tracker.expenses):
                
                deleted_expense = tracker.expenses[choice - 1]
                del tracker.expenses[choice - 1]

                save_expenses(tracker.expenses)

                print(f"{deleted_expense.name} has been successfuly removed!")
            else:
                print("Invalid number!")
                return
            
            

        except ValueError:
            print("Invalid number")
