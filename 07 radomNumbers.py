import numpy as np

rng = np.random.default_rng()

print(np.random.default_rng().integers(low=1, high=7))
print("\n",np.random.default_rng().integers(low=1, high=7, size=3))
print("\n",rng.integers(low=1, high=7, size=[3,3]))

# to get same result
print("\n",np.random.default_rng(seed=1).integers(low=1, high=70, size=[3,4]))

#to get floating point number
print("\n",np.random.uniform(low=-10, high=10))
print("\n", np.round(np.random.uniform(-10, 10, 3), 2))

#Shuffle an array
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print("\n",array)

#choose an item randomly
fruits = np.array(["Apple", "Banana", "Orange", "Pineapple", "Mango"])
fruit = rng.choice(fruits)
print("\n",fruit)

fruit = rng.choice(fruits, 3)
print("\n",fruit)