import threading
import time

def print_number():
    for i in range(1,7):
        print(f"Numbers: {i}")
        time.sleep(0.5)

def print_letter():
    for letter in "ABCDEFGHI":
        print(f"Letters: {letter}")
        time.sleep(0.5)


t1 = threading.Thread(target=print_number())
t1.start()
t2 = threading.Thread(target=print_letter())
t2.start()

t1.join()
t2.join()

print("Done all the work")