"""
Works with arrays for linear algebra, fourier transform, and matrices.
Uses ndarray (50x faster)
Used for Data Science
"""

import numpy as np
print(np.__version__)

# Create ndarrays
ndarray = np.array([1, 2, 3, 4, 5]) # from list
ndarray = np.array((1, 2, 3, 4, 5)) # from tupple
print(type(ndarray))
print(ndarray)

# Dimensions
zero_D = np.array(42)
one_D = np.array([1, 2, 3, 4, 5])
two_D = np.array([[1, 2, 3], [4, 5, 6]])
three_D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 9], [4, 5, 6]]])
print(three_D.ndim)

# Indexing
print(three_D[1][0][2])
print(three_D[1,0,2])
print('Last element from 2nd dim: ', two_D[1, -1])

# Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

# Datatypes
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - memory
"""

print(arr.dtype)
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr.dtype)
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print("------------------")

#Copy and View
arr = np.array([1, 2, 3, 4, 5])
a_copy = arr.copy()
a_view = arr.view()
arr[0] = 42
a_view[-1] = 31
print(arr)
print(a_copy)
print(a_view)

print(arr.base) # None as it has no base/parent
print(a_copy.base) # None as it has no base/parent
print(a_view.base)
print("------------------")

# Shaper
two_D_arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
print(three_D.shape)
flat_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = flat_array.reshape(2, 3, 2)
print(newarr)
print(newarr.base)
flat_array2 = two_D_arr.reshape(-1)
print(flat_array2)
print("- Iterate -----------------")

# Iterate
for item in two_D_arr:
    print(item)

for array1 in two_D_arr:
    for item in array1:
        print(item)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Dim:" + str(arr.ndim))
for x in np.nditer(arr):
  print(x)
print()
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for index, item in np.ndenumerate(arr):
  print(index, item)

print("- Joining -----------------")

# Joining arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
concatinated = np.concatenate((arr1, arr2), axis=1)
print(concatinated)
stacked = np.stack((arr1, arr2), axis=1)
print(stacked)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

hor_stacked = np.hstack((arr1, arr2))
ver_stacked = np.vstack((arr1, arr2))
depth_stacked = np.dstack((arr1, arr2))
print(hor_stacked)
print(ver_stacked)
print(depth_stacked)

print("- Split -----------------")

# Split arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)
print(newarr[0])

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

print("- Search -----------------")

# Search arrays
arr = np.array([1, 2, 3, 4, 5, 4, 4])
items = np.where(arr == 4)
print(items)
items = np.where(arr%2 == 0)
print(items)
arr = np.array([6, 7, 8, 9])
index = np.searchsorted(arr, 7)
print("Insert no 7 at position " + str(index) + " to remain ordered") 

print("- Sort -----------------")

# Sort arrays
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
arr = np.array([True, False, True])
print(np.sort(arr))
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

print("- Filter -----------------")

# Filter arrays
arr = np.array([41, 42, 43, 44])
filter = [True, False, True, False]
newarr = arr[filter]
print(newarr)

filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


