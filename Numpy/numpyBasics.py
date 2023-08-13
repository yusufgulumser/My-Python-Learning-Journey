import numpy as np

# python list and numpy array are the same
py_list = [1,2,3,4,5,6,7,8,9]
np_array = np.array([1,2,3,4,5,6,7,8,9])        
# just their type is different
print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]   # grouping in python list
np_multi = np_array.reshape(3,3)       # grouping in numpy array. (creates a matrix)

print(py_multi)
print(np_multi)
#dimension
print(np_array.ndim)            
print(np_multi.ndim)
#shape
print(np_array.shape)
print(np_multi.shape)