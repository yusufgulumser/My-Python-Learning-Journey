def exponentiation(number):
    def inner(power):
        return number**power
    return inner
two=exponentiation(2)         #The 'two' function represents the inner function.
print(two(3))                 #so, power=3
#########

def operation(operation_name):
    def addition(*args):
        addition=0
        for i in args:
            addition +=i
        return addition
    def multiplication(*args):
        multiplication=1
        for i in args:
            multiplication*=i
        return multiplication
    if operation_name=='addition':
        return addition
    else:
        return multiplication
addition= operation('addition')
print(addition(1,3,5,4,6))

multiplication=operation('multiplication')
print(multiplication(3,4,5,3,4))