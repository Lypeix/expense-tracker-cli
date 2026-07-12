from models import Expense
from reports import get_total_spent


def test_get_total_spent():
    expenses = [
        Expense("Manga", 55, "entertainment", "11-07-2026"),
        Expense("Food", 30, "food", "11-07-2026")
    ]

    assert get_total_spent(expenses) == 85