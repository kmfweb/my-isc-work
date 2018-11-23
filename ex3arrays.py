# Exercise 3: Array calculations and operations

import numpy as np

'''
a = np.array([range(4), range(10, 14)])
b = np.array([2, -1, 1, 0])

print(a * b)

b0 = b*100
b1 = np.multiply(b, 100)
b2 = np.multiply(b, 100.0)
b3 = b * 100.0

print(b1)
print(b2)

print(b0 == b1)
print(b2 == b3)
print(b0.dtype, b1.dtype, b2.dtype, b3.dtype)
'''

'''
arr = np.arange(10)
print(arr < 3)
print(np.less(arr, 3))
condition = np.logical_or(arr < 3, arr > 8)
new_arr = np.where(condition, arr * 5, arr * -5)
print(new_arr)
'''
