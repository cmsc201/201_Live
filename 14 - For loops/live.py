# lizards = ["anole", "bearded lizard", "iguana", "komodo dragon", "Lord Z", "Yooka"]
# index = 0
# while index < len(lizards):
#     print("Whoa, there's a", lizards[index], "in my boot!")
#     index += 1
#
# for index in range(len(lizards)):
#     print("There are too stinky many", lizards[index], "on this gosh darn plane!")


# How can we print the even numbers between two integers x and y with a for loop?
# def print_even_between(x, y):
#     if x % 2 == 1: # if x is odd, skip it (by one)
#         x += 1
#     for number in range(x, y + 1, 2):
#         print(number)
#
# print_even_between(0, 40)
# print_even_between(50, 0) # yay it works
# print("odd?")
# print_even_between(1, 10)


# How can we use range to go backwards through a list?
# disappointing_gliding_animals = ["squirrels", "fish", "geese"]
# for i in range(len(disappointing_gliding_animals) - 1, -1, -1):  # I am being clever and it is so wrong
#     print(disappointing_gliding_animals[i])
#
# index = len(disappointing_gliding_animals) - 1
# while index >= 0:
#     print(disappointing_gliding_animals[index])
#     index -= 1
# What lines of code does a for loop write “for” us?
# index = 0
# index += 1
# Print all the elements of a list with their index!  How do?
# incredible_forks = ["in roads", "in git repos", "in unix processes", "ikea", "unholy spoon fork hybrids"]
# for fork_number in range(len(incredible_forks)):
#     print("The fork", incredible_forks[fork_number], "is easily my number", fork_number + 1, "most interesting fork.")
# Print all the elements of a 2d list with their row and column!  How do?
matrix = [[1, 2, 3, 4, 5, 6],
          [5, 6, 7, 8],
          [9, 1, 2, 3],
          [4, 5, 6, 7]]

for row_number in range(len(matrix)):
    for col_number in range(len(matrix[row_number])):
        print("At row", row_number, "and column", col_number, "we have", matrix[row_number][col_number])


