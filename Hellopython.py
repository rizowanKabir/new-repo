balance = 1000
while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Enter your choice option:")
    if choice == "1":
        print(f"Check balance : {balance}")
    elif choice == "2":
        amount = int(input("Enter deposit amount:"))
        balance += amount
    elif choice == "3":
        amount = int(input("Enter withdraw: "))
        if amount > balance:
            print("Insufficent balance ")
        else:
            balance -= amount
    elif choice == "4":
        print("Good Bye")
        break
    else:
        print("Invalid Option ")






