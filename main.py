expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        expenses.append(amount)
        print("Expense added!")

    elif choice == "2":
        print("Expenses:", expenses)
        print("Total:", sum(expenses))

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")