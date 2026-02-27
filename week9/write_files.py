import random

file = open("random_numbers.txt", "w")

for i in range(20):
    num = random.randint(1, 100)
    file.write(str(num) + "\n")

file.close()
print("20 random numbers written to random_numbers.txt")
# reading the 20 random numbers from random_numbers.txt file
file=open("random_numbers.txt","r")
print("reading the 20 random numbers from random_numbers.txt file")
print(file.read())
