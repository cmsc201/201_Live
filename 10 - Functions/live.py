# Write a program that:
# 1. Asks the user whether they want to (1) add (2) subtract or (3) both
# 2. Write a function for add and subtract

# PROMPT = "(1) add (2) subtract or (3) both"
# ADD = 1
#
#
# def add(num1, num2):
#     print(num1, "+", num2, "=", (num1 + num2))
#
#
# def subtract(num1, num2):
#     print(num1, "-", num2, "=", (num1 - num2))
#
#
# def main_reason_to_leave_party():
#     # ask the user what they want do
#     menu_option = int(input(PROMPT))
#
#     num1 = int(input("#1"))
#     num2 = int(input("#2"))
#     if menu_option == ADD:
#         add(num1, num2)
#     elif menu_option == 2:
#         subtract(num1, num2)
#     elif menu_option == 3:
#         counter = 0
#         while counter < 10:
#             add(num1 + counter, num2)
#             counter += 1
#         subtract(num1, num2)
#     else:
#         print("you don't follow directions.  SHAME")
#
#
# main_reason_to_leave_party()


# Ask a user for a number, and then offer to square it, square root it, or multiply by pi.

# PI = 3
# def square(some_number):
#     print(some_number ** 2)
#
#
# def root(rootable):
#     print(rootable ** (1 / 2))
#
#
# def pi_times(get_me_times_some_pi):
#     print(get_me_times_some_pi * PI)
#
#
# def main():
#     number = int(input("Number?"))
#     menu_option = int(input("1 sq 2 srt 3 pi time!"))
#     if menu_option == 1:
#         square(number)
#     elif menu_option == 2:
#         root(number)
#     elif menu_option == 3:
#         pi_times(number)
#     else:
#         print("hhhwat?")
#
#
# main()

# Write a function that prints out a list, each item on its own line.
def print_lines(things_to_print):
    index = 0
    while index < len(things_to_print):
        print(things_to_print[index])
        index += 1
#
#
# def divide(x, y):
#     print(x / y)
#
#
#
# def main():
#     some_stuff_to_print = [5, "coke", 10, "squash",
#                            "I'm totally too much of an adult to see the pokemon detective movie"]
#     print_lines(some_stuff_to_print)
#     another_list = [1, 2, 3, 4, 5]
#     print_lines(another_list)
#     print_lines(["a", "b", "c"])
#     divide(4, 3)
#
#
# main()
# Modify the grocery app from last class to use that list function.
#
# DONE = "done"
#
# grocery_items = []
# item_to_add = input("Grocery item! enter 'done' when done")
#
# if item_to_add != DONE:
#     grocery_items.append(item_to_add)
# while item_to_add != DONE:
#     item_to_add = input("Grocery item!")
#     if item_to_add != DONE:
#         grocery_items.append(item_to_add)
#
# print_lines(grocery_items)

# Write a function that asks the user for their age until they give something between 0 and 150.  Wait.  Can we do this?
LOWEST_AGE = 0
HIGHEST_AGE = 150

def give_me_your_age():
    age = int(input("age?"))
    while age < 0 or age > 150:
        age = int(input("age?"))
    print("thanks")

def main():
    age = give_me_your_age()
    print("you are", age)

main()