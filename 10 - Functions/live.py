# Write a program that:
# 1. Asks the user whether they want to (1) add (2) subtract or (3) both
# 2. Write a function for add and subtract
ADD = 1
SUBTRACT = 2
BOTH = 3

def both(first_num, second_num):
    add(first_num, second_num)
    subtract(first_num, second_num)

def add(huffelpufferinoington, number2):
    print(huffelpufferinoington, "+", number2, "=", huffelpufferinoington + number2)

def subtract(number1, number2):
    print(number1, "-", number2, "=", number1 - number2)


def print_list(some_list):
    for item in some_list:
        print(item)


if __name__ == '__main__':
    puppy_list = ["charlie"]
    print_list(puppy_list)
    action = int(input("Do you want to (1) add (2) subtract or (3) both?"))
    first_num = int(input("NUMBER!"))
    second_num = int(input("NUMBER!"))

    if action == ADD:
        add(first_num, second_num)
    elif action == SUBTRACT:
        subtract(first_num, second_num)
    elif action == BOTH:
        both(first_num, second_num)
    else:
        print("whaaaaaat?")



# Ask a user for a number, and then offer to square it, square root it, or multiply by pi.

# Write a function that prints out a list, each item on its own line.

# Modify the grocery app from last class to use that list function.

# Write a function that asks the user for their age until they give something between 0 and 150.  Wait.  Can we do this?

