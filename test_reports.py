from models import Expense
from reports import get_total_spent, filter_by_category, filter_by_month


def test_get_total_spent():
    expenses = [
        Expense("Manga", 55, "entertainment", "11-07-2026"),
        Expense("Pizza", 30, "food", "11-07-2026")
    ]

    assert get_total_spent(expenses) == 85

def test_filter_by_category():
    expenses = [
        Expense("Manga", 55, "entertainment", "11-07-2026"),
        Expense("Pizza", 30, "food", "11-07-2026")
    ]

    result = filter_by_category(expenses, "food")
    
    assert len(result) == 1
    assert result[0].name == "Pizza"

def test_filter_by_month():
    expenses = [
        Expense("Manga", 55, "entertainment", "11-07-2026"),
        Expense("Pizza", 30, "food", "11-08-2026")
    ]

    result = filter_by_month(expenses, "07")
    
    assert len(result) == 1
    assert result[0].name == "Manga"
