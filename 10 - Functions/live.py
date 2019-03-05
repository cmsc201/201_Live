# Write a program that:
# 1. Asks the user whether they want to (1) add (2) subtract or (3) both
# 2. Write a function for add and subtract
# def add(num1, num2):
#     print(num1, "+", num2, "=", (num1 + num2))
#
#
# def subtract(num1, num2):
#     print(num1, "-", num2, "=", (num1 - num2))
#
#
# def main():
#     menu_option = int(input("(1) add (2) subtract (3) both"))
#
#     first = int(input("#1"))
#     second = int(input("#2"))
#     if menu_option == 1:
#         add(first, second)
#     if menu_option == 2:
#         subtract(first, second)
#     if menu_option == 3:
#         add(first)
#         subtract(first, second)
#
#
# main()


# Ask a user for a number, and then offer to square it, square root it, or multiply by pi.
# PI = 3
# def square(number):
#     print(number ** 2)
#
# def root(number):
#     print(number ** (1/2))
#
# def pi_times(number_type_thing):
#     print(PI * number_type_thing)
#
# def main():
#     number_thing = int(input("Number for me?"))
#     what_do = int(input("(1) square (2) root (3) have pi times"))
#     if what_do == 1: # ONE SHOULD BE A CONSTANT!!!!!!!!!! (BUT I'M LAZY)
#         square(number_thing)
#     elif what_do == 2:
#         root(number_thing)
#     elif what_do == 3:
#         pi_times(number_thing)
#
# main()


# Write a function that prints out a list, each item on its own line.
def print_out(some_list):
    num = 0
    while num < len(some_list):
        print(some_list[num])
        num += 1


def main():
    stuff_list = ["brake pads", "booster seat", "wiper fluid", "blinker fluid", "strombolis", "pancake mix for racoons"]
    print_out(stuff_list)


main()

# Modify the grocery app from last class to use that list function.

# Write a function that asks the user for their age until they give something between 0 and 150.  Wait.  Can we do this?
