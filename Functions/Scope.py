#Global scope
x= 'global x'

def function():
#Local scope 
    x= 'local x'
    print(x)

function()
print(x)

###########################
#global
name='cinar'
def changeName(newName):
    #local
    name=newName
    print(name)          #it reads ada

changeName('ada')    
print(name)              #it reads cinar

###################################
x=50
def test(x):
    print(f'x:{x}')

    x=100
    print(f'x changed to {x}')       #it will read 100 because 100 is local x

test(x)      
print(x)            #it will read 50 because 50 is global x


####
x=50
def test():
    global x
    print(f'x:{x}')       #it reads 50

    x=100
    print(f'x changed to {x}')      

test()      
print(x)     #it will read 100 becase we made 100 global

