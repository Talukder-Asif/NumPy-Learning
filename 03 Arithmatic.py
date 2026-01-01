import numpy as np

array = np.array([1,2,3])

#Scalar Arithmatic
print("\nScalar Arithmatic are ->")
print("Array is = ",array)
print("array + 1= ",array + 1)
print("array - 3= ", array - 3)
print("array * 3= ",array * 3)
print("array / 2= ",array / 2)
print("array % 2= ",array % 2)
print("array power 2= ",array ** 2)

#Vectorized Math Function
print("\nVectorized Math Function are -> ")
print("np.sqrt(array)= ",np.sqrt(array))
array2 = np.sqrt(array)
print("Round up value = ",np.round(array2))
print("Floor value = ",np.floor(array2))
print("Ceil value = ",np.ceil(array2))
print("PI = ", np.pi)

#Element-wise arithmetic
array1 = array
array2 = np.array([4,5,6])
print("\nElement-wise arithmetic")
print("array1 = ", array1)
print("array2 = ", array2)
print("array1 + array2 = ",array + array2)
print("array1 - array2 = ",array - array2)
print("array1 * array2 = ",array * array2)
print("array1 / array2 = ",array / array2)
print("array1 ** array2 = ",array ** array2)

#Comparison Operators
scores = np.array([91, 55, 100, 73, 80, 64])
print("\nComparison Operators ->")
print("Exam Score = ", scores)
print("scores == 100 = ",scores == 100)
print("scores >= 60 = ",scores > 60)
print("scores < 80 = ",scores >= 80)