# Creating a list
lst = [21, 20, 89, 100, 67]

# a) len()
print("Length of list:", len(lst))

# b) extend()
lst.extend([3, 8])
print("After extend:", lst)

# c) sort()
lst.sort()
print("After sort:", lst)

# d) append()
lst.append(10)
print("After append:", lst)

# e) insert()
lst.insert(2, 6)
print("After insert:", lst)

# f) remove()
lst.remove(67)
print("After remove:", lst)
