import random
import sys
from queue import Queue


def random_name():
    file1 = open(r"movies_available.txt", "r+")
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
    print(accepted)
    done.write(accepted)
    print("name deleted")


while True:
    if __name__ == "__main__":
        choice = menu()
        if choice == 1:
            name = random_name()
            print(name)
            print("Enter 'y' to accept\nEnter 'n' to choose another name\nEnter 'e' to go back to main menu")
            choice1 = input("So which is it? : ")
            if choice1 == 'y' or choice1 == 'Y':
                shift(name)
            if choice1 == 'n' or choice1 == 'N':
                name1 = random_name()
                print(name1)
            if choice1 == 'e' or choice1 == 'E':
                num = menu()
        else:
            sys.exit()
