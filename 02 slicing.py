import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#Row Selection
#array[start:end:step]
print(array[0])
print(array[-1])

print(array[0:3],'\n')
print(array[0:],'\n')
print(array[:2],'\n')

print(array[0:4:2],'\n')
print(array[::2],'\n')
print(array[::-1],'\n')

#Column Selection
print(array[:,1],'\n')

print(array[0:3,0:2],'\n')

print(array[0:2,1])
print(array[::-1,1])
