liste=["1","2","5a","10b""a,b,c","10","50"]

# Find the numerical values within the list elements.
for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue
# Make sure that every input you receive is a number unless the user enters 'q'; otherwise, display an error message.
while True:
    num=input('num: ')
    if num=='q':
        break
    try:
        result=float(num)
        print('the number is:',result)
        break
    except ValueError:
        print('invalid number')
        continue
# Display an error for passwords that contain Turkish characters.
Turkish_characters='şçğüğıİ'
password=input('password: ')
for i in password:
    if i in Turkish_characters:
        raise TypeError('The password cannot contain Turkish characters.')
    else:
        pass
print('valid password')
# Create a factorial function and provide an error message for values passed to the function.
def factorial(x):
    x=int(x)
    if x<0:
        raise ValueError('negative value')

    result=1
    for i in range(1,x+1):
        result*=i
    return result
for x in [5, 10, 20,-3,'3g']:
    try:
        y=factorial(x)
    except ValueError as err:
        print(err)
        continue
    print(y)