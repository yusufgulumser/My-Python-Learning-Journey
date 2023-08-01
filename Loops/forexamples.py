numbers=[1,3,5,7,9,12,19,21]
# Which ones are multiples of 3?
for num in numbers:
    if(num%3==0):
        print(num)


# What is the sum of the numbers
sum=0
for num in numbers:
    sum = sum + num         # or sum += num
print('sum: ', sum)


# Square of odd numbers
for num in numbers:
    if(num%2==1):
        print(num**2)
        

