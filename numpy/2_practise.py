import numpy as np


### slicig ********

# arr = np.array([4,2,1,6,7])
# print(arr[::-1])
# print(arr[:3])
# print(arr[:-1])
# print(arr[1:3])
# print(arr[3:])

 
# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# print(arr)

# print(arr[1,2]) # pass to first row and column 
# print(arr[0][1]) # sama to 👆 but use to diffrent
# print(arr[1]) # it only print row 
# print(arr[:,1]) # it only print column
# print(arr[1,1:3]) # select second row and second column slicing
# print(arr[0:3,2]) # select all row and third col


### sort *********

# arr = np.array([[3,4,2],[1,5,7],[0,9,8]])

# print(np.sort(arr)) # sort to column wise
# print(np.sort(arr,axis=0)) # sort to row  to pass 0 axis
# print(np.sort(arr,axis=1)) # sort to column to pass 1 axis


### filter ******

# number = np.arange(1,11)
# print(number)

# even_num = number[number % 2 == 0] # check to even number and return elament of array
# print(even_num)

# print(number[number > 5]) # check to return elament is grater than 5


### where 

# arr = np.arange(1,11)
# print(np.where(arr > 5,arr*2,arr))

# print(np.where(arr % 2 == 0,"true","flase"))


### adding and removing

## concatination
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# print(np.concatenate((arr1,arr2)))

## remove array
# arr = np.array([1,2,3,4,5])
# print(np.delete(arr,4)) # return to array after delete value 

### How to create an array from existing data

arr = np.array([1,2,3,4,5,6])
arr1 = arr[:]
print(arr1)

arr2 = arr[2:5]
print(arr2)

# it divide two part of array
arr3 = np.split(arr,2) # split it work to like [array([1, 2, 3]), array([4, 5, 6])]
print(arr3)

# You can use the view method to create a new array object that looks at the same data as the original array (a shallow copy).
arr4 = arr.view()
print(arr)
print(arr4)
arr[0] = 10 # change to affect tow original and view 
print(arr)
print(arr4)

# add row and column 

arr = np.array([[1,2],[3,4]])
new_row= np.array([[5,6]])

row_add = np.vstack((arr,new_row)) ## add row
print(row_add)

new_col = np.array([[10],[20]])
col_add = np.hstack((arr,new_col)) ## add column
print(col_add)