# Python Banking system Program

def show_balance():
    print(f"Your balance is BDT {balance:.2f}")
def deposit():
    amount = float(input("Enter your amount here: "))
    if amount < 0:
        print("That's not valid amount ")
    else:
        return amount

def withdraw():
    amount = float(input("Enter the withdraw amount: "))
    if amount > balance:
        print("Insufficient Founds")
    elif amount < 0:
        print("amount should be more than Zero")
    else:
        return amount

balance = 0
is_running = True
while is_running:
    print("........ Welcome to the Banking System .........")
    print("1.show_balance ")
    print("2. deposit")
    print("3. withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1 to 4): ")
    if choice == "1":
        show_balance()
    elif choice == "2":
        balance +=deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("That is invalid choice. please try valid choice")
        
print("Thank you visit our system")

