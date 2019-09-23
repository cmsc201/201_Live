# print all the contents of a list of animals
# print all the animals doing everything in a list of actions
# compute the sum of a list of integers
# print double each element in the list of integer
# update a list to increment each integer by one

if __name__ == '__main__':
    animals = ["cat", "dog", "chinchilla", "monkey", "ferret", "road runner", "aardvark", "Professor Benjamin Johnson, Ph.D"]

    for animal in animals:
        if animal == "chinchilla":
            print("I'm ready for my dust bath!")
        elif animal == "road runner":
            for slow_animal in animals:
                if slow_animal != animal:
                    print(animal, "is faster than", slow_animal)
        else:
            print(animal, "is awesome!")

    # cat is awesome!
    # dog is awesome!
    # I'm ready for my dust bath!
    # monkey is awesome!
    # ferret is awesome!
    # road runner is faster than cat!
    # road runner is faster than dog!
    # road runner is faster than chinchilla!
    # road runner is faster than monkey!
    # road runner is faster than aardvark!
    # road runner is faster than Professor Benjamin Johnson, Ph.D!
    # aardvark is awesome!
    # Professor Benjamin Johnson, Ph.D is awesome!

    numbers = [1, 2, 3, 4]
    for number in numbers:
        number += 1
    print(numbers)
