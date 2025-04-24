# 49. Write a decorator that logs function execution time.
import time 
import math

def decoratir(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        print("before calling function")
        func()
        end=time.time()
        print(f"time to run function {func.__name__}   time take {end-start : .6f} seonds ")
    return wrapper

@decoratir
def greet():
    l=[math.pi*x*x for x in range(1,100)]
    print(l)
    print("HIIIIIIII. . . . .")

greet()