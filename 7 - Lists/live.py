# guess one of my favorite movie animals
# FAVORITE_MOVIE_ANIMALS = ["monkey", "panda", "hyena", "that thing from ice age"]
# guess = ""
# while guess not in FAVORITE_MOVIE_ANIMALS:
#     guess = input("Guess a movie animal!")
#
# print("Good job!")

# input grocery items until done
# grocery_items = []
# new_item = ""
# while new_item != "done":
#     new_item = input("What you want?")
#     grocery_items.append(new_item)
#
# print(grocery_items)
#
# remove_item = ""
# while remove_item != "done":
#     remove_item = input("What did you find?")
#     grocery_items.remove(remove_item)
#
# print(grocery_items)

#input numbers take their avg

# numbers = []
# number_inputted = 0
# while number_inputted != -1:
#     number_inputted = int(input("num?"))
#     if number_inputted != -1:
#         numbers.append(number_inputted)
# print(numbers)
#
# counter = 0
# sum = 0
# while counter < len(numbers):
#     sum += numbers[counter]
#     counter += 1
#
# print(sum / len(numbers))


# input numbers print odds

numbers = []
number_inputted = 0
while number_inputted != -1:
    number_inputted = int(input("num?"))
    if number_inputted != -1:
        numbers.append(number_inputted)
print(numbers)

counter = 0
while counter < len(numbers):
    if numbers[counter] % 2 == 1:
        print(numbers[counter])
    counter += 1

