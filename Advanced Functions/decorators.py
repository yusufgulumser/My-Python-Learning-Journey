def my_decorator(func):
    def wrapper():
        print('operations before function')
        func()
        print('operations after function')
    return wrapper

@my_decorator        # we applied the 'my_decorator' to the 'sayHello' function using the @ symbol
def sayHello():
    print('hello')
sayHello()
################ 
import math
import time

def exponentiation(a,b):
    start=time.time()
    time.sleep(1)
    finish=time.time()
    print(math.pow(a,b))

    print('the function took '+ str(finish-start)+'seconds')
def factorial(num):
    start=time.time()
    time.sleep(1)
    finish=time.time()
    print(math.factorial(num))

    print('the function took '+ str(finish-start)+'seconds')
exponentiation(2,3)
factorial(4)

# We can seperate the 'time' into another function with 'DECORATORS'

def calc_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)         #*args and **kwargs in a function's parameter list allows that function to accept any number of these arguments. 
        finish=time.time()
        print('the function took '+ str(finish-start)+'seconds')
    return inner
@calc_time
def exponentiation(a,b):
    print(math.pow(a,b))
@calc_time
def factorial(num):
    print(math.factorial(num))

exponentiation(2,3)
factorial(4)
        