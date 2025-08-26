import numpy as np

### normal array create **********

arr = np.array([1,2,3])
# print(arr)

# arr2 = np.array((1,2,3))
# print(arr2)


# this is use but it is not use to allow it set is set to all data in sorted from and that resone to not use to some time 

# arr3 = np.array({1,2,3})
# print(arr3)  

### check to array type **********

# print(type(arr)) 
# print(type(arr2))
# print(type(arr3))

# print(arr[0]) # access to array value 
# arr[0] = 100 # change value
# print(arr[0]) 

# it is work slicing  ***

# print(arr[:]) 
# print(arr[::-1])
# print(arr[:2])

## create 0d array || Scalars
scalars = np.array(98)
print("Scalars :",scalars)

## create 1d array || vector 
vector = np.array([1,2,3])
print("vector :",vector)

## create 2d array || matrix
matrix = np.array([[1,2,3],[4,5,6]])
print("matrix :\n",matrix)

## create 3d array || tensor
tensor = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[4,5,6]]
])
print("tensor :\n",tensor)


## store n time value in array ***

## use in list **
# list_arr = [i for i in range(1000)]
# print(list_arr)

# - sum of i vlaue store list
# list_sum = [i+i for i in range(100)]
# print(list_sum)


## use in np.array **
# np_arr = np.arange(1000)
# print(np_arr)

# - sum of i vlaue store np array
# np_sum = np.arange(100) 
# np_sum = np_sum + np_sum
# ****** or ******
# np_sum = np.arange(100) * 2
# print(np_sum)

### Array attributes **********

## check to dimension **
# print("Dimension of scalars : ",scalars.ndim) 
# print("Dimension of vector : ",vector.ndim) 
# print("Dimension of matrix : ",matrix.ndim) 
# print("Dimension of tensor : ",tensor.ndim)

## shape ***
# shape is return row and column 
# print("shape of scalares : ",scalars.shape)
# print("shape of vector : ",vector.shape)
# print("shape of matrix : ",matrix.shape)
# print("shape of tensor : ",tensor.shape) 
## => shape of tensor :  (1, 2, 3) 

# number of blocks (like depth / batch size / first dimension)
# number of rows
# number of columns

## size ***
# print("size of scalares : ",scalars.size)
# print("size of vector : ",vector.size)
# print("size of matrix : ",matrix.size)
# print("size of tensor : ",tensor.size) 

## dtype (data type) ***
# print("data type of scalares : ",scalars.dtype)
# print("data type of vector : ",vector.dtype)
# print("data type of matrix : ",matrix.dtype)
# print("data type of tensor : ",tensor.dtype) 



### How to create a basic array **********

# np.zeros() → Array filled with 0
# Use: Initialize an empty matrix before filling it with real values.
# zeros = np.zeros((3,4))
# print(zeros)

# np.ones() → Array filled with 1
# Use: Helpful when you need a starting array with all values = 1 (common in ML weight initialization).
# ones = np.ones((2,2))
# print(ones) 

# np.empty() → Array with garbage values
# Use: Faster than zeros() if you will overwrite values later (saves time).
# empty = np.empty((2,4))
# print(empty)

# np.arange() → Range of numbers (like Python’s range)
# Use: Generate sequences (indices, time steps, positions).
# arange = np.arange(0,10,2)
# print(arange)

# np.linspace() → Evenly spaced numbers
# Use: Scientific computing → dividing a range into equal parts (like plotting graphs).
# linspace = np.linspace(0,10,num=5)
# print(linspace)


### Specifying your data type *********
# While the default data type is floating point (np.float64), you can explicitly specify which data type you want using the dtype keyword.
# print("Specifying your data type")
# x = np.ones((2,2),dtype=np.int64)
# print(x)

# y = np.linspace(0,10,num=10,dtype=np.int64)
# print(y)


### array reshaping *********

arr = np.arange(12)
print("orignal : ",arr)

reshaped = arr.reshape((3,4))
print(reshaped)

flattened = reshaped.flatten()
print(flattened)

reveled = reshaped.ravel()
print(reveled)

transpose = reshaped.T
print(transpose)

# it is same to like reshape((pass)) 

### You can use np.newaxis to add a new axis:

# Adds a new axis at the beginning (row).
print("\n np.newaxis :",newaxis := arr[np.newaxis,:]) # row vector
print("it convert to 2d array : ",newaxis.shape) 

# Adds a new axis at the end (column).
print("\n",newaxis1 := arr[:,np.newaxis]) # column vector 
print(newaxis1.shape)


### You can use np.expand_dims to add an axis at index position 1 with:

print("\n",np.expand_dims(arr,axis=1)) ## row vector
print("\n",np.expand_dims(arr,axis=0)) ## column vector

### create array useing existing array 
print("\n\n")
arr = np.arange(1,11)
print(arr)

a1 = arr[2:6]
print("slicing using create array : ",a1)

a3 = np.copy(arr)
acon = np.concatenate((a3,[2,4])) # it return new array it not change to original array
print("copy array : ",a3)
print("copy arrya concatenate :",acon)

# arr = np.array([[1,2],[3,4]])
# new_row= np.array([[5,6]])

# row_add = np.vstack((arr,new_row)) ## add row
# print(row_add)

# new_col = np.array([[10],[20]])
# col_add = np.hstack((arr,new_col)) ## add column
# print(col_add)

