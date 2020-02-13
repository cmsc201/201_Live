# print all the contents of a list of animals
# print all the animals doing everything in a list of actions
# compute the sum of a list of integers
# print double each element in the list of integer
# update a list to increment each integer by one

if __name__ == '__main__':
    animals = ["panda de refuse", "platypus", "platypus (ditto really)", "charizangled", "bidoof"]

    for animal in animals:
        print(animal)

    numbers = [1, 2, 3, 4]
    # write a loop to print each number divided by 2
    # for some_thing_made_up in numbers:
    #     # print(some_thing_made_up / 2)
    #     # print(some_thing_made_up)
    #     print("next time on the looping show...")
    #     numbers.append(numbers)
    # print("Hi!")
    # print(numbers)
    # print(some_thing_made_up)

    for number in numbers:
        number += 1
        print(number)
    print(numbers)

