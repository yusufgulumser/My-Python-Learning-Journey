import math
value=help(math)   # You can see all the commands in the "math" module in Python.

value= math.sqrt(49)
value= math.factorial(5)

print(value)

# You can give an alias to a module.
import math as calc
value= calc.factorial(5)

print(value)

#We are importing everything from the 'math' module using *.

from math import *
value=factorial(5)         #we dont need to write 'math.'

print(value)

#Or we can use just a few methods

from math import factorial,sqrt

value=factorial(5)          #it prints 120
value=ceil(5.8)             #ceil method not defined

print(value)