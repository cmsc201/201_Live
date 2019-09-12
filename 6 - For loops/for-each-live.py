# print all the contents of a list of animals
# print all the animals doing everything in a list of actions
# compute the sum of a list of integers
# print double each element in the list of integer
# update a list to increment each integer by one

if __name__ == '__main__':
    animals = ["alpaca", "snake", "lizard", "ben johnson", "chicken", "red lobster"]

    # for all animals, print their name
    claimed_coolest = []
    for animal in animals:
        # if the animal is a chicken, print its sound instead
        if animal == "chicken":
            print("buckaaaaaw!!?!!")
        # if the animal is a lizard, say it's cooler than all the other animals
        elif animal in ["lizard", "red lobster"]:
            claimed_coolest.append(animal)
            for inferior_animal in animals:
                if inferior_animal != animal and inferior_animal not in claimed_coolest:
                    print(animal, "is way cooler than", inferior_animal)
        else:
            print(animal)

    numbers = [1, 2, 3, 4, 5]
    one_added = []
    # add one to each number in the list
    for number in numbers:
        one_added.append(number + 1)
    print("The result is", one_added)



    numbers = [3, 4,3456, 4, 5, 63, 2,35, 66]
    sum = 0
    for super_awesome_single_number in numbers:
        sum += super_awesome_single_number
    print("The sum is", sum)
