# Write a program that:
# 1. Asks the user whether they want to (1) add (2) subtract or (3) both
# 2. Write a function for add and subtract


# Ask a user for a number, and then offer to square it, square root it, or multiply by pi.

# Write a function that prints out a list, each item on its own line.

# Modify the grocery app from last class to use that list function.

# Write a function that asks the user for their age until they give something between 0 and 150.  Wait.  Can we do this?


def get_user_name_and_greet():
    name = input("What is your name?")
    print_greeting(name)


def print_greeting(name):
    print("Hello!", name)


def add(x, y):
    
    result = x + y
    return result


if __name__ == '__main__':
    # x = 1
    # y = 2
    # add(x, y)
    # # get_user_name_and_greet()
    # # print("Goodbye!")
    first = int(input("num1"))
    second = int(input("num2"))
    print(first, "+", second, "is", add(first, second))

