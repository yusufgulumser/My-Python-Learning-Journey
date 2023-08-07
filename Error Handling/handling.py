#COMMON ERRORS

# print(a) => NameError
# im('1a2') =>ValueError
# print(10/0) =>ZeroDivisionError
# priNt('tryi'ng) =>SyntaxError


#####################################
#ERROR HANDLING
try:
    x=int(input('x: '))
    y=int(input('y: '))
    print(x/y)
except ZeroDivisionError:
    print('y cant be 0')
except ValueError:
    print('You must enter a numerical value for x and y')

#####
while True:
    try:
        x=int(input('x: '))
        y=int(input('y: '))
        print(x/y)
    except Exception as ex:                 #'Exception' covers all errors
        print('wrong information',ex)       # We can see error type with 'ex' here
    else:
        break                   #It continues to ask for values until the user enters correct information.                                    

