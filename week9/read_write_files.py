# Create and write to a file using write() and writelines()
file = open("sample.txt", "w")
# write() method
file.write("Hello World\n")
file.write("Welcome to Python File Handling concept\n")

# writelines() method
lines = ["implementing the read method using read() and readlines().\n", "implementing write methods as write() and writelines().\n", "the basic operations of files is open, write, read and close.\n"]
file.writelines(lines)

file.close()


# Now read the file using read(), readline(), readlines()

file = open("sample.txt", "r")

print("Using read():")
print(file.read())      # Reads entire file

file.seek(0)            # Move cursor to beginning

print("Using readline():")
print(file.readline())  # Reads one line
print(file.readline())  # Reads next line

file.seek(0)

print("Using readlines():")
print(file.readlines()) # Reads all lines as list

file.close()