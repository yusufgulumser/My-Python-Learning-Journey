# Creating a List of Numbers using a for Loop
numbers=[]
for x in range(10):
    numbers.append(x)
print(numbers)
#"Creating a List of Numbers using a List Comprehension with range()
numbers= [x for x in range(10)]    
print(numbers)



"Printing the Square of Numbers in a Range"
for x in range(10):
    print(x**2)
#Creating a List of Squares of Numbers using a List Comprehension                                              
numbers=[x**2 for x in range(10)]
print(numbers)

#Calculating Ages using List Comprehension
years=[1983,1997,1960,1976]
ages=[2023-year for year in years]
print(ages)

#Generating a List with Numbers and 'ODD' Using List Comprehension
results=[x if x%2==0 else 'ODD' for x in range(1,10)]
print(results)

#Creating a List of Tuples with Cartesian Product of Two Ranges using List Comprehension
numbers=[(x,y) for x in range(3) for y in range(3)]
print(numbers)

