import numpy as np
id_array = np.array([101, 102, 103, 104, 105])
print("ID Array:", id_array)
print("\n indexing:\n")
print("First element:", id_array[0])
print("Third element:", id_array[2])
print("Last element:", id_array[-1])
print("\n slicing: \n")
print("First three elements:", id_array[0:3])
print("Elements from index 1 to 3:", id_array[1:4])
print("Elements from index 2 to end:", id_array[2:])
print("elemnts from staring index to some specific index 4:",id_array[:4])
print("All elements:", id_array[:])
id_array[1] = 202
print("\nArray after modifying index 1:", id_array)
id_array[2:4] = [515,517]
print("Array after slicing modification:", id_array)
