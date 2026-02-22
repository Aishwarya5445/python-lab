# Create a dictionary
student = {  "name": "Aishwarya", "age": 19, "grade": "A","section":"C"}

# a) keys()
print("Keys:", student.keys())

# b) values()
print("Values:", student.values())

# c) items()
print("Items:", student.items())

# d) pop()
removed_value = student.pop("age")
print("Removed value:", removed_value)
print("Dictionary after pop:", student)

# e) delete (using del)
del student["grade"]
print("Dictionary after delete:", student)