file = open("sample2.txt", "w+")

file.write("Python File Handling Example")
file.flush()  # Forces writing data to file immediately

print("Current position using tell():", file.tell())

# Move cursor to beginning
file.seek(0)
print("After seek(0), position:", file.tell())

# Move cursor 7 bytes from beginning
file.seek(7)
print("After seek(7), position:", file.tell())

# Move cursor to end
file.seek(0, 2)  # 2 means from end of file
print("After seek(0,2), position:", file.tell())

file.close()