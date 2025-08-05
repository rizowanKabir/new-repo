import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.txt"):
        self.filename = filename

    def add_expense(self, item, amount):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as file:
            file.write(f"{date} - {item} - BDT{amount}\n")
        print(f"✅ Added: {item} - BDT{amount}")

    def view_expenses(self):
        total = 0
        print("\n📄 Your Expenses:\n----------------------")
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    print(line.strip())
                    parts = line.strip().split(" - ")
                    if len(parts) == 3:
                        amount = float(parts[2].replace("BDT", ""))
                        total += amount
        except FileNotFoundError:
            print("No expense record found.")
            return

        print(f"\n💰 Total Expenses: BDT{total:.2f}")

# ----------------------------
# Main Program
# ----------------------------

tracker = ExpenseTracker()

while True:
    print("\n----- Expense Tracker -----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        item = input("Enter expense item: ").strip()
        amount = float(input("Enter amount (BDT): "))
        tracker.add_expense(item, amount)

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        print("Thank you for using Expense Tracker! 👋")
        break

    else:
        print("❌ Invalid choice. Try again.")
