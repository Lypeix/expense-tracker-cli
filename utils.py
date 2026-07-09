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


def choose_category():
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
