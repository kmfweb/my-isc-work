import numpy as np

'''
x = list(range(1,11))

a1 = np.array(x, np.int32)
a2 = np.array(x, np.float32)

print(a1.dtype)
print(a2.dtype)

np.zeros((2, 3, 4))
np.ones((2, 3, 4))
np.arange(1000)
'''

'''
# I am not sure if this works but we wanted it to create a 3D array with entries from 1-999.

list1 = list(range(1,10))
x_1, y_1, z_1 = list1, list1, list1

x3d, y3d, z3d = np.meshgrid(x_1, y_1, z_1)

array1 = np.zeros((9,9,9))

for a in array1:
	index = array1.index(a)
	a= x3d[index]+y3d[index]+z3d[index]
	
print (array1)
'''

'''
a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
print(a[1]) # This should print out 3.2.
print(a[1:4]) # This should give out [3.2 5.5 -6.4].
'''

arr = np.zeros((2, 3, 4))+12
print(arr)
