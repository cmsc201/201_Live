# A user must guess my favorite movie animals
# FAVORITE_MOVIE_ANIMALS = ["Flipper", "Happy Feet", "Simba", "Bambi's mom", "Lemurs from Madagascar"]
# guess = ""
# while guess not in FAVORITE_MOVIE_ANIMALS:
#     guess = input("YOU CAPTIVE UNTIL YOU GUESS MY FAVE MOVIE ANIMALS!")
#
# print("Yeah!")

# A user can input grocery items and then check them off by inputting them again
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
# num = 0
# while num < len(grocery_items):
#     print(grocery_items[num])
#     num += 1

# A user inputs a series of numbers and then we print the list of numbers with their average
# user_input = int(input("Gimme numbers, -1 to stop"))
# if user_input != -1:
#     numbers = [user_input]
# while user_input != -1:
#     user_input = int(input("Gimme numbers, -1 to stop"))
#     if user_input != -1:
#         numbers.append(user_input)
#
# index = 0
# sum = 0
# while index < len(numbers):
#     sum += numbers[index]
#     index += 1
#
# print("avg = ", sum / len(numbers))



# A user inputs a series of numbers and then we print out only the odd ones.
# user_input = int(input("Gimme numbers, -1 to stop"))
# if user_input != -1:
#     numbers = [user_input]
# while user_input != -1:
#     user_input = int(input("Gimme numbers, -1 to stop"))
#     if user_input != -1:
#         numbers.append(user_input)
#
# index = 0
# while index < len(numbers):
#     if numbers[index] % 2 == 1:
#         print(numbers[index])
#     index += 1
