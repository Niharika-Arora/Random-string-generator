import random
import sys


def random_name():
    file1 = open(r"movies_available.txt", "r+")
    line = random.choice(list(file1))
    file1.close()
    return line


def menu():
    print("*********Welcome to the world of randoms********")
    print("What would you like to do?")
    print("1. Get a new name \n2. To exit")
    ch = int(input("Enter the corresponding number for your choice : "))
    return ch


def delete(line):
    file = open(r"movies_available.txt", "r")
    content = list(file)
    file.close()
    file = open(r"movies_available.txt", "w")
    for c in content:
        if c == line:
            continue
        file.write(c)
    file.close()


def shift(s):
    done = open(r"movies_used.txt", "a")
    print(s)
    done.write(s)
    delete(s)
    print("name deleted")
    done.close()


if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == 1:
            while True:
                name = random_name()
                print(name)
                print("Enter 'y' to accept\nEnter 'n' to choose another name\nEnter 'e' to go back to main menu")
                choice1 = input("So which is it? : ")
                if choice1 == 'y' or choice1 == 'Y':
                    shift(name)
                    break
                if choice1 == 'e' or choice1 == 'E':
                    break
                else:
                    continue
        else:
            sys.exit(0)
