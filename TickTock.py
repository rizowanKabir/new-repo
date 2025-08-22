
import threading
import time
def countdown():
    for i in range(5,0,-1):
        print(f"Countdown: {i}")
        time.sleep(1)
def ticktock():
    for _ in range(10):
        print("নিতু ছাগল")
        time.sleep(2)

tt1 = threading.Thread(target=countdown())
tt1.start()
tt2 = threading.Thread(target=ticktock())
tt2.start()

tt1.join()
tt2.join()

print("Yeah !!! Done")