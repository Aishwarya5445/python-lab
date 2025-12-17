import numpy as np
# 1. Array Creation
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D Array:")
print(arr_2d)
print("Shape of the array:", arr_2d.shape)
print("Data type of elements:", arr_2d.dtype)

# Create an array using NumPy functions (e.g., zeros, ones, arange)
zeros_arr = np.zeros((2, 2))
ones_arr = np.ones((3, 2))
print("Zeros Array (2*2):\n",zeros_arr)
print(" ones array(2*2):\n",ones_arr)
#accesing elements
print("accessing elements by indexing:")
print("Element at row 0, column 1:", arr_2d[0, 1])  
print("Element at row 1, column 2:", arr_2d[1, 2])  

print("accesing elements by slicing:")
print("First row:", arr_2d[0, :]) 
print("First two columns:")
print(arr_2d[:, :2])

# 3. Basic Arithmetic Operations 
arr_b = np.array([[7, 8, 9], [10, 11, 12]])
arr_sum = arr_2d + arr_b
print("Addition:")
print(arr_sum)

arr_mul = arr_2d * arr_b
print("Multiplication:")
print(arr_mul)

# 4. Universal Functions and Statistics
print("Mean of all elements:", np.mean(arr_2d))
print("Maximum element:", np.max(arr_2d))
print("Sum of columns:", np.sum(arr_2d, axis=0))  # axis=0 for columns
print("Sum of rows:", np.sum(arr_2d, axis=1))     # axis=1 for rows

# 5. Array Manipulation
arr_reshaped = arr_2d.reshape((3, 2))
print("Reshaped Array (3x2):")
print(arr_reshaped)

# Flatten the array to 1D
arr_flattened = arr_2d.flatten()
print("Flattened Array (1D):")
print(arr_flattened)
