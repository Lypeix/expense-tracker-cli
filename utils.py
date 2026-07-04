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
            
