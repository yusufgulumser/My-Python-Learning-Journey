# print x values 1 to 100
x=1
while x<=100:
    print(x)
    x= x+1     # or x+=1
print('finished')


# User name greeting with input validation
name='' #false
while not name:
    name= input('what is your name: ')
print(f'hello, {name}')


# 'name.strip' prevents empty space input in user name greeting
name='' #false
while not name.strip():
    name= input('what is your name: ')
print(f'hello, {name}')