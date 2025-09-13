#Problem 1
"""f = open("poem.txt","r")
content = f.read()
if("python" in content):
    print("yes I am here")
else:
    print("sad I am not here")
f.close()"""

#problem 2

"""import random


def game():
    secret = random.randint(1, 100)
    print("......The new guessing game.....")

    while True:
        guess = int(input("Enter the guess number: "))

        # store guess in file
        with open("guessing.txt", "a") as file:  # use append mode
            file.write(str(guess) + "\n")

        if secret == guess:
            print("That was correct. You win!")
            break
        elif secret < guess:
            print("You are too high. Try lower.")
        elif secret > guess:
            print("You are too low. Try bigger.")
        else:
            print("Something went wrong")


game()"""

#problem 3
"""def tables(n):
    with open("multiplication.txt", "w") as file:  # open file once in write mode
        for i in range(1, n + 1):
            line = f"{i} * {n} = {i * n}"
            print(line)              # display on console
            file.write(line + "\n")  # write to file with newline

tables(10)"""

#problem 4

"""word = "donkey"

with open("myfile.txt","r") as file:
    content = file.read()
new_content = content.replace(word,"####")

with open("myfile.txt","w") as file:
    content = file.write(new_content)"""

#Problem 5(Check file exists or not)

"""import os

if os.path.exists("myfile.txt"):
    print("file is here")
else:
    print("file is not here")"""

#write a simple text file

"""with open("hello.txt","w") as file:
    data = file.write("Hello Python\n")
    data1 = file.write("I am rizowan Kabir. i am practicing code in python")
    print(data)
    print(data1)
with open("hello.txt","r") as file:
    data = file.read()
    print(data)"""

#3. Read line by line
"""with open("hello.txt","r") as file:
    for line in file:
        print(line)
with open("hello.txt", "r") as file:
    line = file.readline()   
    while line:
        print(line, end="")
        line = file.readline()"""
#4. Append new content

"""with open("hello.txt","a") as file:
    file.write("this line was added later\n")"""

#5. Write a list to file

"""fruits = ["Apple", "Banana", "Mango", "Orange"]

with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")"""

#8. Copy content from one file to another
"""with open("hello.txt","r") as source:
    with open("fruits.txt","w") as target:
        for line in source:
            target.write(line)"""

#9. Find and replace text in a file
"""with open("hello.txt","r") as file:
    content = file.read()
new_content = content.replace("Hello","Hi")
with open("hello.txt","w") as file:
    file.write(new_content)"""

#10. Store numbers and calculate sum
"""import csv

# Some sample data
students = [
    ["Name", "Age", "Grade"],
    ["Alice", 14, "A"],
    ["Bob", 15, "B"],
    ["Charlie", 13, "A+"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("students.csv created ✅")"""

#Json example
"""import json

student = {
    "name": "Alice",
    "age": 14,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("student.json created ✅")"""
























