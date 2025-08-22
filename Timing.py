import threading
import time
import datetime

def print_time():
    for _ in range(5):
        print("Time: ",datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(1)

def print_message():
    for _ in range(2):
        print("Hello from my Universe")
        time.sleep(2)

print_time()
print_message()

print("!!!!!!  Done   ")