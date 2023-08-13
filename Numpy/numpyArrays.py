import numpy as np

result = np.array([1,3,5,7,9])

result = np.arange(1,10)   #creates an array (1,2,3,4,5,6,7,8,9)
result = np.arange(10,100,3)   #step size is 3 (10,13,16...97)

result = np.zeros(10)      # consist only zeros
result = np.ones(10)         # consist only ones

result = np.linspace(0,100,5)     # Splits into equal parts based on start and end values. (0,25,50,75,100)

result = np.random.randint(0,10)   # Generates a random number between 0 and 9.
result = np.random.randint(20)      # 0-19
result = np.random.randint(1,10,3)  # Generates three random number between 0 and 9.

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)     # Creates a matrix with 5 rows and 10 columns 
print(np_multi.sum(axis=1))           # Sum of the rows
print(np_multi.sum(axis=0))           # Sum of the columns

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max()         # Prints the largest number.
result = rnd_numbers.min()         # Prints the lowest number.
result = rnd_numbers.mean()        # Prints the mean       
result = rnd_numbers.argmax()      # Prints the index of largest number.
result = rnd_numbers.argmin()

print(result)