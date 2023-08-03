# CHANGING
def changeName(n):
    n= 'ada'
name= 'jose'
changeName(name)
print(name)


def change(n):
    n[0]= 'ankara'
cities= ['istanbul', 'mersin']          # n[0] will be ankara and n[1] will be mersin
change(cities)
print(cities)

#ADDING
def add(a,b):                  # you can add just 2 number
   return sum((a,b))
print(add(10,23))

def add(*parameters):          # you can add as many numbers as you want
    return sum((parameters))
print(add(10,20,34))            

# ONE STAR(*)= TUPLE  two star(**)=DICTIONARY

def displayUser(**args):
    for key,value in args.items():
        print('{} is {}'.format(key,value))

displayUser( name='yusuf' ,age=2 ,city='istanbul')

