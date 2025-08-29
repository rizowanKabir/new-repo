#Add two number
"""num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

add = num1 + num2
print(f"The result is: {add}")"""

#Area of Rectangle
"""length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
Area = length * width

print(f"The result of area is : {Area}")"""

#Area of circle
"""r = float(input("Enter the number: "))
pi = 3.1416

area = pi * r * r
print(f"Total Area of circle: {area}")"""

#Interest Calculater
"""principle = int(input("Enter the principle amount: "))
rate = float(input("Enter the rate: "))
time = int(input("Enter the time(in year): "))

interest = principle * rate * time
print(f"Total amount is: {interest}")"""

#Tempareture Converter
"""celsius = int(input("Enter the celsius: "))
fahrenheit = (celsius * 9/5) +32
print(fahrenheit)"""

#Age in day
"""age = int(input("Enter your age please: "))
day = age * 365
print(f"The age into day: {day}")"""

#Swap two number
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping: a =", a, "b =", b)"""

#Even or odd
"""num = int(input("Enter the number: "))
if (num % 2 == 0):
    print("Even number")
else:
    print("odd number")"""

#Largest number
"""num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the three number: "))

largest = max(num1,num2,num3)
print(f"The largest number is: {largest}")"""

#Grade Calculater
"""mark = int(input("Enter the mark please: "))

if mark >= 80:
    print("you get A+")
elif mark >= 70:
    print("you get A")
elif mark >= 60:
    print("you get A-")
elif mark >= 50:
    print("you get B")
elif mark >= 40:
    print("you get D")
else:
    print("you fail !!! try agin with more harder")"""

#ATM cash withdraw
"""balance = int(input("Enter the total balance pleas: "))
withdraw = float(input("Enter the withdraw amount: "))
if withdraw <= balance:
    balance -= withdraw
    print("successfully you withdraw your amount ")
else:
    print("Insufficient balance ! please try for right amount")"""

#BMI calculater
"""weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)
print("Your BMI:", round(bmi, 2))"""

#Speed Calculater
"""distance = int(input("Enter the distance please: "))
time = int(input("Enter the time please: "))

speed = (distance / time) * 100
print(f"The total speed is: {speed}  km/h")"""

#Discount Calculater
"""price = float(input("Enter product price: "))
discount = float(input("Enter discount %: "))
final_price = price - (price * discount / 100)
print("Final price:", final_price)"""

#
"""units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 5
else:
    bill = (100 * 5) + ((units - 100) * 8)
print("Electricity bill:", bill)"""

#passwor Manager
"""password = input("Enter you password please: ")

if len(password) < 6:
    print("Weak password please try more stronger ")
elif password.isdigit() or password.isalpha():

    print("Medium Password ")
else:
    print("strong password")"""

#Voting eligibility
"""name = input("Enter your name please: ")
age = int(input("Enter your age please: "))
citizen = input("Are you citizen in this country(NO/YES?): ")

if citizen.lower() == "Yes":
    print("You are right path.. ")
elif citizen.lower() == "No":
    print("You are try in wrong path")

elif age >= 18:
    print("You are on process to get voter")
else:
    print("You are not enough age to pay vot or anything.Dont be upset better luck next time")"""

#
"""items = int(input("Enter your number of item: "))
total = 0
for i in range(items):
    price = float(input("Enter your item price: "))
    i += 1
    total += price
print(f"The total amount: {total}")"""

#Student mark
"""num = int(input("Enter your subject number: "))
total = 0

for i in range(num):
    mark = float(input("Enter your mark please: "))
    i += 1
    total += mark
    average = total / num
print(f"The average number: {average:.2f}")"""

#currency Converter

"""usd = float(input("Enter the USD currency: "))
value = 120

BDT = usd * value
print(f"The total money in BDT: {BDT}")"""

# student Management
"""students = int(input("How many students: "))
total = 0
for s in range(students):
    name = input("Enter your name: ")
    subjects = int(input("How many Subject: "))

    for i in range(subjects):
        mark = float(input("Enter your mark: "))
        i += 1
        total += mark
        avg = total / subjects
    if avg >= 80:
        grade = "A+"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "Fail"
    print(f"{name} result")
    print(f"Total: {total},Average: {avg:.2f}, GPA: {grade}")"""

#Banking Management System
"""balance = 0
while True:
    print("\n....Bank Menu.....")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = float(input("Enter Your Deposit please: "))
        balance += amount
        print(f"You have successfully Deposit(New Balance) {balance}")
    elif choice == 2:
        amount = float(input("Enter your withdraw amount : "))
        if amount <= balance:
            balance -= amount
            print(f"You have successfully Withdraw New balance{balance}")
        else:
            print("Insufficient Balance ")
    elif choice == 3:
        print(f"Current Balance is: {balance}")
    elif choice == 4:
        print("Exit....!!")
    else:
        print("Invalid Choice !!! please do right choice")"""
#Employee payroll Management

"""employees = int(input("Enter How many Employees: "))

for e in range(employees):
    name = input("Enter Employee Name: ")
    salary = float(input("Enter your salary Number: "))

    house_rent = salary * 0.20
    allowance = salary * 0.10
    provident_found = salary * 0.5

    gross = house_rent + allowance + provident_found
    Net = gross - provident_found

    print(f"Employee Name: {name}")

    print(f"Total Gross: {gross},& Net: {Net}")"""

#ticket booking system

"""tickets = 50
price = 200

while tickets > 0:
    print(f"\nAvailable Tickets: {tickets}")
    buy = int(input("How many tickets do you want to buy?: "))

    if buy <= tickets:
        cost = buy * price
        print(f"Total cost = {cost} Tk")
        tickets -= buy
    else:
        print("Not enough tickets available!")

    if tickets == 0:
        print("All tickets sold out!")
        break"""

#Tickets Booking

"""tickets = 50
price = 200
while tickets > 0:
    print("\nTickets Available !!!!")
    buy = int(input("Enter How many tickets do you want buy?: "))
    if buy <= tickets:
        cost = buy * price
        print(f"Total cost : {cost} Tk")
        tickets -= buy
    else:
        print("not enough tickets available ")

    if tickets == 0:
        print("All the tickets sold out")
        break"""

#Resturant Billing System

"""menu = {"pizza":150, "burger":100, "clod coffe":120, "pasta":80, "cocke":20}
order = {}
total = 0

print(".......Welcome to the love cafe........")
print(menu)

while True:
    items = input("\nEnter item to order (or Done!!): ").lower()
    if items == "done":
        break
    if items in menu:
        qty = int(input("Enter quantity of order: "))
        cost = menu[items] * qty
        order[items] = order.get(items, 0) + qty
        total += cost
    else:
        print("Item not available ")

print("\n......BILL.......")
for item, qty in order.items():
    print(f"{item.capitalize()} x {qty} = {menu[item] * qty} Tk")
print(f"Total: {total}")"""

#Score Game

"""questions = {
    "What is the capital of France?": "Paris",
    "Who developed Python?": "Guido",
    "2 + 2 * 2 = ?": "6"
}

score = 0
for q, ans in questions.items():
    user = input(q + " ")
    if user.strip().lower() == ans.lower():
        score += 1

print("\nYour Score:", score, "/", len(questions))"""

#Studnets Attendance Report

"""students = ["Rizowan","Kabir","Ovey","Atik","Shagor","Shakil"]
attendance = {}

for student in students:
    status = input(f"{student} Present(Yes or No??): ")
    attendance[student] = status
print("\n.......Student attendance report........")
for s,st in attendance.items():
    print(f"{s}:{st}")"""

#Expence Tracker daily(Budget)

"""budget = float(input("Enter your daily budget: "))
expenses = 0
while True:
    expense = input("Enter your expense (or done): ")
    if expense.lower() == "done":
        break
    expenses += float(expense)
    remain = budget - expenses
print(f"Total Expenses: {expenses}")
print(f"Reaming: {remain}")"""

#Hospital Management

"""patients = []

while True:
    print("\n.....Hospital Menu .........")
    print("1. Admit patients")
    print("2. Show Patients")
    print("3. Discharge Patients")
    print("4. Exit.......")

    choice = input("Enter your Choice: ")

    if choice == "1":
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        disease = input("Enter disease name: ")
        patients.append({"name": name, "age": age, "disease": disease})
        print("Patient admitted Successfully ..!")

    elif choice == "2":
        print("\nPatients List.........")
        if not patients:
            print("No patients admitted yet.")
        else:
            for p in patients:
                print(f"Name:{p['name']}-Age:({p['age']} yrs) - Disease:{p['disease']}")

    elif choice == "3":
        name = input("Enter patient name to discharge: ")

        new_patients = []
        found = False

        for p in patients:
            if p['name'] != name:
                new_patients.append(p)
            else:
                found = True
        if found:
            print("Patient discharged successfully!")
        else:
            print("No such patient found!")

        patients = new_patients

    elif choice == "4":
        print("Exiting the system... Bye!")
        break

    else:
        print("Invalid Choice ..!!")"""

#Online Exam System

"""questions = {
    "Python is a?(language or tool):": "language",
    "Python invent by(Guido or Russo):": "Guido",
    "2 * 8 =": "16",
    "Capital of Bangladesh:": "Dhaka",
    "Laptop:": "HP"
}

score = 0

for q, ans in questions.items():
    user = input(q + " ")

    if user.strip().lower() == ans.lower():
        score += 1

print(f"\nExam Finished! Your Score: {score}/{len(questions)}")
if score == len(questions):
    print("Excellent work..!!")
elif score >= len(questions):
    print("Good Job..")
else:
    print("Better luck next time")"""

#Cinema Seat booking

"""seats = [0]*20
while True:
    print(f"\nAvailable Seat: {seats}")
    choice = input("Enter choice seat number (0-20) to book (or exit): ")
    if choice.lower() == "exit":
        break
    choice = int(choice)

    if 0 <= choice <20:
        if seats[choice] == 0:
            seats[choice] = 1
            print(f"Seat {choice} booked successfully")
        else:
            print("Seat not available")

    else:
        print("Invalid Seat ..! Better luck next time")"""

#Online Voting System

"""candidates = {"Alice": 0, "Bob": 0, "Charlie": 0}

while True:
    print("\nCandidates:", list(candidates.keys()))
    vote = input("Enter your vote (or 'end'): ")

    if vote.lower() == "end":
        break
    elif vote in candidates:
        candidates[vote] += 1
    else:
        print("Invalid candidate!")

print("\n--- Voting Results ---")
for c, v in candidates.items():
    print(f"{c}: {v} votes")

winner = max(candidates, key=candidates.get)
print("Winner is:", winner)"""






















































