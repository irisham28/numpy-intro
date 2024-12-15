import numpy as np

#list
list = [1,3,4,5,6]
print(list)

#converting list into np array (matrix)

np_array = np.array(list)
print(np_array)

#numerical operations - dimensions and shape
#dimensions: num of axis - rows and columns. Use: ndim to get the dimensions of the array
np_array = np.array([[1,2],[3,4]])
dimensions = np_array.ndim
print(dimensions)

#Shape: Size of the array
shape = np_array.shape
print(shape)


#numpy array for multi dimensional array (usually called as tensors)
matrix = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(matrix.shape)

print(matrix)


#accecsing value of array using index number
print(np_array[0][1])


#creating array with random value rangers

arr = np.arange(1,11,2)
#arrange (start value, end value, step)
#ending value is not included it will stop before
print(arr)


#reshape - changing the shape of the array without changing the values in it

reshape = np_array.reshape(1,4) # 1 is num of rows, 4 is num of columns 
print(reshape)



