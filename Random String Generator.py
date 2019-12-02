import random


file1 = open(r"C:\Users\Neha\PycharmProjects\personal projects\random movies.txt", "r+")
line = random.choice(list(file1))
print(line)
file1.close()
