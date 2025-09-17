#Part 1: Variables (10 Problems)
#1. Swap Two Variables Without Using Third Variable

"""a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
a,b = b,a
print(f"A = {a} & B = {b}")"""
#2. Calculate Area of a Circle

"""radius = int(input("Enter the radius number: "))
pi = 3.1416
Area = pi * radius * radius
print(f"The Area of circle is: {Area:.2f} cm")"""
#3. Convert Celsius to Fahrenheit

"""celsius = int(input("Enter the degree in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The fahrenheit degree in: {fahrenheit} F")"""

#4. Simple Interest Calculator
"""principle = float(input("Enter your principle: "))
rate = float(input("Enter your rate: "))
time = int(input("Enter your time (in years): "))
simple_interest = (principle * rate * time) / 100
print(f"The interest is: {simple_interest} Tk")"""

#5. Compound Interest Calculator
"""principle = float(input("Enter your principle: "))
rate = float(input("Enter your rate: "))
time = int(input("Enter your time (in years): "))
compound_interest = principle * (1 + rate / 100) ** time - principle
print(f"The compound Interest is: {compound_interest:.2f} TK")"""

#6. Perimeter of Rectangle
"""length = float(input("Enter the number: "))
width = float(input("Enter the number: "))
perimeter = 2 * (length + width)
print(f"The perimeter is: {perimeter:.2f} CM")"""

#7. Volume of Cube
"""side = int(input("Enter the side number: "))
volume = side ** 3
print(f"The volume is: {volume} CM")"""

#8. Convert Days into Years, Months, Days
"""days = int(input("Enter the days: "))
years = days // 365
month = (days % 365) // 30
day_left = (days % 365) % 30
print(f"{days} days into:\nyears {years} month {month} day_left {day_left}")"""

#9. Convert Seconds into H:M:S
"""seconds = int(input("Enter the seconds please: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
second = seconds % 60
print(f"hours {hours} :Minutes {minutes} :seconds {second}")"""

#10. Calculate BMI
"""weight = 70  # kg
height_feet = 5.7 

# feet → inches
height_inches = height_feet * 12

# inches → meters
height_meters = height_inches * 0.0254

# BMI calculation
bmi = weight / (height_meters ** 2)

print("Weight (kg):", weight)
print("Height (feet):", height_feet)
print("Height (inches):", height_inches)
print("Height (meters):", height_meters)
print("BMI:", bmi)"""

#Part 2: Input (10 Problems)
#11. Take Name and Print Greeting
"""name = input("Enter your name please: ")
print(f"Hello {name} Good morning")"""

#12. Sum of Two Numbers
"""num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print(f"The sum of two numbers: {sum}")"""

#13. Square of a Number
"""num = int(input("Enter the number: "))
square = num ** 2
print(f"The result is: {square}")"""

#14. Area of Triangle
"""base = int(input("Enter the number of base: "))
height = int(input("Enter the number of height: "))
Area = 0.5 * base * height
print(f"The Area of triangle is: {Area} CM")"""

#15. Check Odd or Even
"""num = int(input("Enter the number: "))
if num % 2 == 0:
    print(f"{num} this is even number")
else:
    print(f"{num} this is odd number")"""

#16. Convert Kilometers to Miles
"""km = float(input("Enter the number into kilometer: "))
Miles = km * 0.621371
print(f"The kilometer into Miles: {Miles:.2f} mile")"""

#17. Calculate Average of 3 Numbers
"""num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

Average = (num1 + num2 + num3) / 3
print(f"The Average is: {Average}")"""

#18. Reverse a Number
"""num = input("Enter the number: ")
print(f"The Reverse number/word is: {num[::-1]}")"""

#19. Simple Calculator (Add/Sub/Mul/Div)
"""a = float(input("Enter the number(a): "))
operators = input("Enter the operators (+,-,*,/): ")
b = float(input("Enter the number(b): "))
if operators == "+":
    print(a + b)
elif operators == "-":
    print(a - b)
elif operators == "*":
    print(a * b)
elif operators == "/":
    print(a / b)
else:
    print("Invalid Operators.try right one")"""

#20. Power of a Number
"""base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Result:", base**exp)"""

# Part 3: If / Else (10 Problems)
#21. Check Positive, Negative or Zero
"""num = int(input("Enter the number: "))
if num > 0:
    print(f"{num} is positive.Because bigger then Zero")
elif num < 0:
    print(f"{num} is negative. Because smaller than Zero")
else:
    print(f"{num} this is Zero")"""

#22. Find Largest of 3 Numbers
"""a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
if a > b and a > c:
    print(f"{a} is the largest number between them")
elif b > a and b > c:
    print(f"{b} is the largest number between them")
else:
    print(f"{c} is the largest number between them")"""

#23. Leap Year Checker
"""year = int(input("Enter the year please: "))
if year % 400 == 0:
    print(f"this {year} is leap year")
else:
    print(f"This {year} is not leap year")"""

#24. Grade System
"""student = input("Enter the student name: ")
marks = int(input("Enter the mark here: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")"""

#25. Even or Odd Without Modulus
"""num = int(input("Enter the number: "))
if (num & 1 == 0):
    print(f"{num} this is even number")
else:
    print(f"{num} this odd number")"""

#26. Absolute Value Without abs()
"""num = int(input("Enter the number: "))
if num < 0:
    num = -num
    print(f"Absolute {num}")"""

#27. Check Vowel or Consonant
"""ch = input("Enter the vowel: ")
vowel = "aeiou"
if ch.lower() in vowel:
    print(f"{ch} is vowel")
else:
    print(f"{ch} is consonant")"""

#28. Electricity Bill Calculator
"""unit = int(input("Enter the unit number: "))
if unit <= 100:
    bill = unit * 5
elif unit <= 200:
    bill = 100*5 + (unit-100)*7
else:
    bill = 100*5 + 100*7 + (unit-200)*10
print("Bill:", bill)"""

#29. Triangle Type Checker
"""a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")"""

#30. Check Number is Divisible by Both 3 and 5
"""num = 30
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible")"""

#Part 4: For Loop (10 Problems)
#31. Print Multiplication Table

"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(f"{i} * {n} = {i * n}")"""

#32. Sum of First N Numbers
"""n = int(input("Enter the number: "))
total = 0
for i in range(1,n+1):
    total += i
print(total)"""

#33. Factorial of N
"""n = int(input("Enter the number: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(f"The factorial is: {fact}")"""

#34. Fibonacci Series (First 10 terms)
"""a,b = 0,1
for _ in range(10):
    print(a)
    a,b = b,a+b"""

#35. Reverse a String
"""s = input("Enter the word: ")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)"""

#36. Count Vowels in a String
"""sentence = input("Enter the sentence: ")
vowel = "aeiou"
count = 0
for ch in sentence:
    if ch.lower() in vowel:
        count += 1
print(f"Vowels: {count}")"""

#37. Print Prime Numbers (1-50)
"""for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")"""

#38. Print Pattern (Triangle)
"""for i in range(1,7):
    print("*" * i)"""

#39. Sum of Digits
"""num = 1234
s = 0
for d in str(num):
    s += int(d)
print("Sum of digits:", s)"""

#40. Armstrong Number Checker
"""num = 153
s = 0
for d in str(num):
    s += int(d) ** 3
print("Armstrong" if s == num else "Not Armstrong")"""

#String Concatenation with Variables:
"""first_name = "Johan"
last_name = "Ali"
result = first_name + " " + last_name
print(f"Concatenation: {result}")"""

#Print Variable with f-string:
"""product = "Laptop"
quantity = 2
print(f"{quantity} {product}")"""

#Ask for name, city, and favorite color, then print a summary.
"""name = input("Enter the name: ")
city = input("Enter your city: ")
color = input("Enter your favorite color: ")
print(f"Hello {name} from {city} & your favorite color is {color}")"""

# Ask for a username, if it's "admin", print "Welcome admin", else "Access Denied".
"""user_name = input("Enter the user_name: ")
if user_name == "admin":
    print("Welcome to Dashboard")
else:
    print("Access Denied")"""

#Ask for a password, if length >= 8, print "Strong", else "Weak".
"""password = input("Enter the password please: ")
if len(password) >= 8:
    print(f"This {password} is enough strong")
elif len(password) >= 6:
    print(f"{password} this is medium")
else:
    print(f"{password} is so weak")"""
# Ask for age, print ticket price (Child: <12 - $5, Adult: 12-65 - $10, Senior: >65 - $7).
"""age = int(input("Enter the age please: "))
if age < 12:
    print("Ticket price is $5(Child)")
elif 12 <= age <=65:
    print("Ticket price is $10 (Adult)")
else:
    print("Ticket price is $7 (Senior)")"""

#Use a for loop to print numbers from 1 to 5.
"""for i in range(1,6):
    print(i)"""

#Calculate the sum of numbers from 1 to 10 using a for loop.
"""sum = 0
for i in range(1,11):
    sum += i
print(sum)"""

#Print all even numbers from 0 to 10 (inclusive).
"""for i in range(0,11,2):
    print(f"All are even number {i}")"""

# Ask for a sentence, count and print the number of vowels in it.
"""sentence = input("Enter the sentence: ")
vowel = "aeiou"
vowel_count = 0
for ch in sentence:
    if ch.lower() in vowel:
        vowel_count += 1
print(f"The vowels: {vowel_count}")"""

#Ask for a number and calculate its factorial (e.g., 5! = 5*4*3*2*1).
"""num = int(input("Enter the number: "))
fact = 1
if num < 0:
    print("Factorial not define for zero")
elif num == 0:
    print("for zero the factorial number is 1")
else:
    for i in range(1,num+1):
        fact *= i
        print(fact)"""

#Create a list of fruits and print each fruit using a for loop.
"""fruits = ["apple","Banana","orange","coconut","Cherry"]
for fruit in fruits:
    print(fruit)"""

#Use nested for loops to print a simple right-angled triangle pattern of asterisks.
"""rows = int(input("Enter the number: "))
for i in range(1, rows + 1):
    print("*" * i)"""

# Use a while loop to print numbers from 1 to 5.
"""count = 1
while count <= 5:
    print(count)
    count += 1"""

#Use a while loop to print a countdown from 10 to 1, then "Lift off!".
"""countdown = 10
while countdown >= 1:
    print(countdown)
    countdown -= 1
print("Lift off!!")"""

#Continuously ask the user for numbers and add them to a sum until they enter 0.
"""total = 0
num = -1
while num != 0:
    num = int(input("Enter the number: "))
    total += num
print("The total sum is:",total)"""

#Create a simple guessing game. User guesses a number until correct.
"""secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Enter the number: "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")

print("Congratulation !!! you guessed right")"""

#Keep asking the user for a number until they enter a positive number.
"""num = 0
while num <= 0:
    num = int(input("Enter the positive number: "))
    if num <= 0:
        print("Invalid input!! Please entered a positive number: ")
print(f"You entered {num}")"""

#Iterate through a string and print each character using a while loop.
"""word = input("Enter the word here: ")
index = 0
while index < len(word):
    print(word[index])
    index += 1"""

#Implement a login system with a correct password "secret" and 3 attempts.
"""correct_password = "secret"
attempts = 0
max_attempts = 3
password_entered = ""
while password_entered != correct_password and attempts < max_attempts:
    password_entered = input("Enter password: ")
    if password_entered != correct_password:
        attempts += 1
        print(f"Incorrect password. {max_attempts - attempts} attempts remaining.")
    else:
        print("Login successful!")
if attempts == max_attempts and password_entered != correct_password:
    print("Too many incorrect attempts. Account locked.")"""

#Create a simple menu that keeps running until the user enters 'q'.
"""while True:
    print("\n-----Menu-------")
    print("1. Choice option A")
    print("2. Choice Option B")
    print("3. Choice Option C")
    choice = input("Enter your choice here (to stop q):").lower()
    if choice == "q":
        print("Exiting Game.GoodBye")
        break
    elif choice == "1":
        print("Choice option A")
    elif choice == "2":
        print("Choice option B")
    elif choice == "3":
        print("Choice option C")
    else:
        print("Invalid Try!!!!")"""



































































