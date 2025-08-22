import threading
import time

balance = 1000
lock = threading.Lock()

def withdraw(amount):
    global balance
    with lock:
        if balance >= amount:
            print(f"withdrawing: {amount}")
            time.sleep(2)
            balance -= amount
            print(f"Left Balance: {balance}")
        else:
            print("Insufficient balance ! Try right amount ")

t1 = threading.Thread(target=withdraw, args=(700,))
t2 = threading.Thread(target=withdraw, args=(50,))

t1.start()
t2.start()
t1.join()
t2.join()

print("!!!  Have a nice day")