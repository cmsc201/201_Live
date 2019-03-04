# Write a program that:
# 1. Asks the user whether they want to (1) add (2) subtract or (3) both
# 2. Write a function for add and subtract

#
# def add(num1, num2):
#     print(num1, "+", num2, "=", (num1 + num2))
#
#
# def subtract(num1, num2):
#     print(num1, "-", num2, "=", (num1 - num2))
#
#
# def main():
#     menu_option = int(input("(1) add (2) subtract or (3) both"))
#
#     num1 = int(input("#1"))
#     num2 = int(input("#2"))
#     if menu_option == 1:
#         add(num1, num2)
#     elif menu_option == 2:
#         subtract(num1, num2)
#     elif menu_option == 3:
#         add(num1, num2)
#         subtract(num1, num2)
#     else:
#         print("what are you talking about?")
#
#
# main()
# Ask a user for a number, and then offer to square it, square root it, or multiply by pi.
# PI = 3
#
#
# def square(n):
#     print(n ** 2)
#
#
# def square_root(n):
#     print(n ** (1 / 2))
#
#
# def pi_times(n):
#     print(n * PI)
#
#
# def main():
#     number = int(input("number!"))
#     menu_option = int(input("(1)square (2)sqrt (3) pi times!"))
#     if menu_option == 1:
#         square(number)
#     elif menu_option == 2:
#         square_root(number)
#     elif menu_option == 3:
#         pi_times(number)


# main()
# Write a function that prints out a list, each item on its own line.
def print_list(a_list):
    num = 0
    while num < len(a_list):
        print(a_list[num])
        num += 1


# def main():
#     my_list = [1, 2, 3, "dave"]
#     print_list(my_list)
#     some_ducks_i_once_knew = ["youssef", "bev", "john", "shirley"]
#     print_list(some_ducks_i_once_knew)
#     print_list(some_ducks_i_once_knew)
#     print_list(some_ducks_i_once_knew)
#     print_list(my_list)
#
#
# main()

# Modify the grocery app from last class to use that list function.
# def main():
#     grocery_items = []
#     new_item = ""
#     while new_item != "done":
#         new_item = input("What you want?")
#         grocery_items.append(new_item)
#
#     print_list(grocery_items)
#
#     remove_item = ""
#     while remove_item != "done":
#         remove_item = input("What did you find?")
#         grocery_items.remove(remove_item)
#
#     print_list(grocery_items)
#
#
# main()

# Write a function that asks the user for their age until they give something between 0 and 150.
# Wait.  Can we do this?

def ask_age():
    age = int(input("How old?"))
    while age < 0 or age > 150:
        age = int(input("Nah, nah. How old?"))
    print("thanks")

def main():
    age = ask_age()
    print(age)

main()