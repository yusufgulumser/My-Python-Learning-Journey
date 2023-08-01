numbers=[1,3,5,7,9,12,19,21]
# print numbers
i=0
while (i<len(numbers)):
    print(numbers[i])
    i+=1


#Printing odd numbers between start and end values entered by the user
start=int(input('start :'))
end= int(input('end :'))
while start<end:
    start+=1
    if (start%2==1):
        print(start)


#Printing numbers in descending order from 100 to 1
i=100
while i>0:
    print(i)
    i-=1

#Take 5 numbers from the user and sort them
numbers = []
i=0
while i<5:
    num=int(input('number: '))
    numbers.append(num)
    i+=1
    numbers.sort()
print(numbers)


#Take an unlimited number of product information from the user and store them in a list called 'products'
products=[]
quantity= int(input('how many products do you want to add '))
i=0
while (i<quantity):
    name=input('name of product ')
    price=input('price of product ')
    products.append({
        'name':name,
        'price':price
    })
    i+=1
for prod in products:
    print(f'product name:{prod["name"]} product price: {prod["price"]}')









