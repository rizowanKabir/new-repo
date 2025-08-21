import time

def timing_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f}")
    return wrapper
@timing_decorator
def say_hello():
    time.sleep(1)
    print("say Good bye")
say_hello()