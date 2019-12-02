import random
import sys
from queue import Queue


def random_name():
    file1 = open(r"C:\Users\Neha\PycharmProjects\personal projects\random movies.txt", "r+")
    line = random.choice(list(file1))
    return line


def menu():
    print("*********Welcome to the world of randoms********")
    print("What would you like to do?")
    print("1. Get a new name \n2. To exit")
    ch = int(input("Enter the corresponding number for your choice : "))
    return ch


def shift(s):
    q = Queue()
    q.put(s)
    done = open(r"Random.txt", "a")
    accepted = q.get()
    done.write(accepted)


if __name__ == "__main__":
    while menu():
        choice = menu()
        if choice == 1:
            name = random_name()
            print(name)
            choice1 = input("Enter 'y' to accept\nEnter 'n' to choose another name\nEnter 'e' to go back to main menu : ")
            if choice1 == 'y' or choice1 == 'Y':
                shift(name)
            if choice1 == 'n' or choice1 == 'N':
                name1 = random_name()
            if choice1 == 'e' or choice1 == 'E':
                num = menu()
        else:
            sys.exit()
