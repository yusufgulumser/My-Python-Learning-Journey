def outer(num1):
    print('outer')
    def inner_increment(num1):          #The operation returning outside doesn't affect the function inside.
        print('inner')
        return num1+1
outer(10)                 #prints just outer
#######
def outer(num1):
    print('outer')
    def inner_increment(num1):
        print('inner')
        return num1+1
    num2=inner_increment(num1)
    print(num1+num2)

outer(10)               #prints outer and inner. 
inner_increment(10)     #UNDEFINED. It can only work within the outer scope.
