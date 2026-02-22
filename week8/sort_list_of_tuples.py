# Sorting list of tuples based on the second element

tuple_list = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

sorted_list = sorted(tuple_list, key=lambda x: x[1])

print("Sorted list based on square value:")
print(sorted_list)