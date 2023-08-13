import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]     # 5th index
result = numbers[:3]    # 0,1,2 index
result = numbers[3:]    # 3,4,5,6,7 index
result = numbers[::]
result = numbers[::-2]  # Prints from right to left, two by two.

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numbers2[2]
result = numbers2[2,1]   # The 1st element of the 2nd row.
result = numbers2[:,2]   # 2nd element of every row

print(result)

