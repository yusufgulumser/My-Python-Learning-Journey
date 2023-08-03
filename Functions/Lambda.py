#MAP
def square(num): return num**2

numbers= [1,2,3,5]
result= list(map(square,numbers))
print(result)
#LAMBDA
numbers= [1,2,3,5]
result= list(map(lambda num:num**2,numbers))
print(result)

