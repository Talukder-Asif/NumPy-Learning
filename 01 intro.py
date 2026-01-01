import numpy as np

#Python List
my_list = [1,2,3,4]
my_list *=2
print(my_list)

#NumPy Array
array = np.array([1,2,3,4])
array*=2
print(array)
print(type(array))

#Multidimantial Array
array = np.array('A')
print(array.ndim)

array = np.array(['A','B','C','D'])
print(array.ndim)
print("Shape of this Array/Matrix is: ",array.shape)

array = np.array([['A','B','C'],
                  ['M','N','O'],
                  ['X','Y','Z']])
print(array.ndim)
print("Shape of this Array/Matrix is: ",array.shape)

array = np.array([[['A','B','C'], ['M','N','O'], ['X','Y','Z']],
                  [['A', 'B', 'C'], ['M', 'N', 'O'], ['X', 'Y', 'Z']],
                  [['A', 'B', 'C'], ['M', 'N', 'O'], ['X', 'Y', 'Z']]])
print("Dimension of this Array is: ", array.ndim)
# output 3,3,3 that means 3 layers, 3 rows, 3 columns
print("Shape of this Array/Matrix is: ",array.shape)
#Multidimensional indexing
print(array[0,2,1], array[1,1,0])