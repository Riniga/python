"""
ufuncs ar functions that works on the ndarray
Works with Vectorization
"""
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("- Addition with loop -----------------")
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
result_list = []

for i, j in zip(list1, list2):
  result_list.append(i + j)
print(result_list)

print("- Addition with function -----------------")
result_list = []
result_list = np.add(list1,list2)
print(result_list)


print("- Addition with own function -----------------")
def myadd(item1, item2):
  return item1+item2
custom_function = np.frompyfunc(myadd, 2, 1)
print(custom_function([1, 2, 3, 4], [5, 6, 7, 8]))

print(type(custom_function))
print(type(myadd))

print("- Subtraction -----------------")
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
print(newarr)

print("- Multiplication -----------------")
newarr = np.multiply(arr1, arr2)
print(newarr)

print("- Division -----------------")
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2)
print(newarr)

print("- Power -----------------")
newarr = np.power(arr1, arr2)
print(newarr)

print("- Remainder -----------------")
newarr = np.mod(arr1, arr2)
print(newarr)

print("- Quotient and Mod -----------------")
newarr = np.divmod(arr1, arr2)
print(newarr)

print("- Absolute -----------------")
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)


print("- Truncation -----------------")
arr = np.trunc([-3.1666, 3.6667])
print(arr)

print("- Fix -----------------")
arr = np.fix([-3.1666, 3.6667])
print(arr)

print("- Rounding -----------------")
arr = np.around([-3.1666, 3.6667], 2)
print(arr)

print("- Floor -----------------")
arr = np.floor([-3.1666, 3.6667])
print(arr)

print("- Ceil -----------------")
arr = np.ceil([-3.1666, 3.6667])
print(arr)

print("- Log at Base 2 -----------------")
arr = np.arange(1, 10)
print(np.log2(arr))

print("- Log at Base 10 -----------------")
print(np.log10(arr))

print("- Log at Base e -----------------")
print(np.log(arr))

print("- Log at any Base -----------------")
from math import log
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))


print("- Add vs Sum -----------------")
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(newarr)
newarr = np.sum([arr1, arr2])
print(newarr)
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)
newarr = np.cumsum(arr1)
print(newarr)

print("- Products -----------------")
arr1 = np.array([1, 2, 3, 4])
product = np.prod(arr1)
print(product)
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)
newarr = np.cumprod(arr2)
print(newarr)
