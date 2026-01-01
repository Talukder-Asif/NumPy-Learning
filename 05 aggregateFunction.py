import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(array)
print("sum of the array ->", np.sum(array))
print("mean of the array ->", np.mean(array))
print("Standard Division of the array ->", np.std(array))
print("Variance of the array ->", np.var(array))
print("Minimum value of the array ->", np.min(array))
print("Maximum value of the array ->", np.max(array))
print("Position of minimum value ->", np.argmin(array))
print("Position of maximum value ->", np.argmax(array))

#sum of Columns
print(np.sum(array, axis=0))

#sum of Rows
print(np.sum(array, axis=1))