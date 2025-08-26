import numpy as np

### basic arrya opration 

a1 = np.array([1,2,3]) 
a2 = np.ones(3,dtype=np.int64)
print(a1 + a2) #  [1,2,3] + [1,1,1] = [2,3,4]
print(a1 - a2) # [1,2,3] - [1,1,1] = [0,1,2]

print(a1 * a1) # [1,2,3] * [1,2,3] = [1,4,9]
print(a1 / a1) # [1,2,3] / [1,2,3] = [1,1,1]


### sum function

arr = np.array([1,2,3,4,5,6])
print("sum of array elements : ",np.sum(arr))
arr = arr.reshape((2,3))
print("sum of array column : ",np.sum(arr,axis=0)) 
print("sum of array row : ",np.sum(arr,axis=1)) 

### Broadcasting

data = np.array([1,2,3])
data = data * 2 # scalar is {2}
print("Broadcasting : ",data)
# --- or ---
data = np.array([4,5,6]) + 2
print(data)


### his section covers maximum, minimum, sum, mean, product, standard deviation, and more
arr = np.arange(1,11)
print("minimum number is : ",np.min(arr))
print("maximum number is : ",np.max(arr))
print("sum of number is : ",np.sum(arr))

arr = arr.reshape((2,5))

## perfrom to axis
print("Min number on col : ",np.min(arr,axis=0))
print("Min number on row : ",np.min(arr,axis=1))

print("Max number on col : ",np.max(arr,axis=0))
print("Max number on row : ",np.max(arr,axis=1))

print("Sum of col : ",np.sum(arr,axis=0))
print("Sum of row : ",np.sum(arr,axis=1))

## matrix multiplication broadcast rull

d1 = np.array([[1,2,3],[4,5,6]])
d2 = np.array([[3,2,1],[6,5,4]])
print(d1+d2)

## generatin random number
print(np.random.random((2,4)))
print(np.random.randint(0,10,10))