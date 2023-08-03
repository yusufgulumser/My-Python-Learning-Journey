#Show the divisors of a given number in a list.
def div(number):
    divisors = []

    for i in range(2,number):
        if(number%i==0):
            divisors.append(i)
    return divisors

print(div(20))

#Convert the given unlimited number of parameters into a list

def conv(*params):
    list=[]
    for param in params:
        list.append(param)
    return list
result=conv(1,2,3,'hello')
print(result)