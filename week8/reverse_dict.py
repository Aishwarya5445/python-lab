# Reverse dictionary lookup

data = {"a": 1,"b": 2,"c": 3}
# Value to search

value_to_find = 2
for key, value in data.items():
    if value == value_to_find:
        print("Key for value", value_to_find, "is:", key)
        break
else:
    print("Value not found")