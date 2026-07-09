def spending_by_category(expenses):

    result = {}

    for expense in expenses:

        category = expense.category

        if category not in result:
            result[category] = 0

        result[category] += expense.amount

    return result 
