import unittest
from datetime import date
from main import ExpenseTracker, Expense

class TestExpenseTracker(unittest.TestCase):
    def test_add_expense(self):
        tracker = ExpenseTracker()
        tracker.add_expense("Food", 50.0, date(2024, 12, 25), "Dinner")
        self.assertEqual(len(tracker.expenses), 1)
        self.assertEqual(tracker.expenses[0].category, "Food")
        self.assertEqual(tracker.expenses[0].amount, 50.0)

    def test_calculate_total(self):
        tracker = ExpenseTracker()
        tracker.add_expense("Food", 50.0, date(2024, 12, 25))
        tracker.add_expense("Transport", 20.0, date(2024, 12, 26))
        total = tracker.calculate_total()
        self.assertEqual(total, 70.0)

if __name__ == "__main__":
    unittest.main()
