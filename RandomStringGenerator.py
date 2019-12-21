import random
import sys
import os


def random_name():
    file1 = open(r"movies_available.txt", "r")
    line = random.choice(list(file1))
    file1.close()
    return line


def menu():
    print("*********Welcome to the world of randoms********")
    print("What would you like to do?")
    print("1. Get a new name \n2. To exit \n3. To reset the available movies list")
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


def reset():
    available = open(r"movies_available.txt", "a")
    used = open(r"movies_used.txt", "r")
    for movie in list(used):
        available.write(movie)
    used.close()
    os.remove(r"movies_used.txt")
    available.close()
    print("Reset successful")


if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == 1:
            while True:
                name = random_name()
                print(name)
                print("Enter 'y' to accept\nEnter 'n' to choose another name\nEnter 'e' to go back to main menu")
                choice1 = input("So which is it? : ")
                if choice1.casefold() == 'y'.casefold():
                    shift(name)
                    break
                if choice1.casefold() == 'e'.casefold():
                    break
                else:
                    continue
        elif choice == 2:
            sys.exit(0)
        elif choice == 3:
            print("This will reset the available movies to initial unselected state")
            choice1 = input("Continue with reset? (y/n) : ")
            if choice1.casefold() == 'y'.casefold():
                reset()
            else:
                break
        else:
            print("Wrong choice, Please try again.")
