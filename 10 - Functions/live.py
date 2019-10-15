# Write a program that:
# 1. Asks the user whether they want to (1) add (2) subtract or (3) both
# 2. Write a function for add and subtract
ADD = 1
SUBTRACT = 2
BOTH = 3

def add(number1, number2):
    """
    Adds number1 and number2 together and prints the result
    :param number1: the first number
    :param number2: the second number
    :return: what is this crazzy thingg?
    """
    print(number1 + number2)


def subtract(the_first_number, the_second_number):
    print(the_first_number - the_second_number)



if __name__ == '__main__':
    action = int(input("Do you want to (1) add (2) subtract or (3) both"))
    number1 = int(input("What is the first number? "))
    number2 = int(input("What is the second number? "))

    if action == ADD:
        add(number1, number2)
    elif action == SUBTRACT:
        subtract(number1, number2)
    elif action == BOTH:
        add(number1, number2)
        subtract(number1, number2)
    else:
        print("You didn't put in the right thing!  Begone!")

# Ask a user for a number, and then offer to square it, square root it, or multiply by pi.

# Write a function that prints out a list, each item on its own line.

# Modify the grocery app from last class to use that list function.

# Write a function that asks the user for their age until they give something between 0 and 150.  Wait.  Can we do this?

