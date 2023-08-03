# greeting with python function
def sayHello(name='user'):
    print('hello'+name)
 
sayHello('Yusuf')
sayHello('Efe')
sayHello()

def sayHello(name='user'):
    return 'hello'+name
 
msg= sayHello('Yusuf')
print(msg)

# Basic Addition Function in Python
def total(num1,num2):
    return num1 + num2
result= total(20,34)
print(result)

# Calculating age with function
def ageCalc(birthday):
    return 2023 - birthday
realAge= ageCalc(2010)
print(realAge)



