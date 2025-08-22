import threading
import time

def walk_dog():
    time.sleep(10)
    print("You finish walking first")
def take_out_trash():
    time.sleep(2)
    print("You take out the trash")
def get_mail():
    time.sleep(6)
    print("You get mail soon")

obj1 = threading.Thread(target=walk_dog)
obj1.start()
obj2 = threading.Thread(target=take_out_trash())
obj2.start()
obj3 = threading.Thread(target=get_mail())
obj3.start()

obj1.join()
obj2.join()
obj3.join()

print("All the task are done")


