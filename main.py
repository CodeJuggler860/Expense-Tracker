import datetime

class Expense:
    def __init__(self, category, amount, date, description=""):
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description

    def __str__(self):
        return f"[{self.date}] {self.category}: ${self.amount:.2f} ({self.description})"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, date, description=""):
        new_expense = Expense(category, amount, date, description)
        self.expenses.append(new_expense)

    def view_expenses(self):
        return self.expenses

    def view_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]

    def calculate_total(self, start_date=None, end_date=None):
        total = 0
        for expense in self.expenses:
            if start_date and expense.date < start_date:
                continue
            if end_date and expense.date > end_date:
                continue
            total += expense.amount
        return total


def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Calculate Total Expenses")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            description = input("Enter description (optional): ")
            tracker.add_expense(category, amount, date, description)
            print("Expense added successfully!")
        elif choice == "2":
            expenses = tracker.view_expenses()
            if not expenses:
                print("No expenses recorded.")
            else:
                for expense in expenses:
                    print(expense)
        elif choice == "3":
            category = input("Enter category to view: ")
            expenses = tracker.view_expenses_by_category(category)
            if not expenses:
                print(f"No expenses found for category: {category}")
            else:
                for expense in expenses:
                    print(expense)
        elif choice == "4":
            start_date_str = input("Enter start date (YYYY-MM-DD) or press Enter to skip: ")
            end_date_str = input("Enter end date (YYYY-MM-DD) or press Enter to skip: ")
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date() if start_date_str else None
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date() if end_date_str else None
            total = tracker.calculate_total(start_date, end_date)
            print(f"Total expenses: ${total:.2f}")
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
