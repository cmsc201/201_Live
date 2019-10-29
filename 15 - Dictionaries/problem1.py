if __name__ == '__main__':
    # Take two lists of values and make a dictionary that associates the keys in one list with the values of the other list
    unacceptable_animals = ["geese", "wasps", "mosquito"]
    reasons = ["jerkfaces", "stingy", "bitey"]

    reasons_to_dislike_animals = {}

    # loop through unacceptable_animals and add them as keys
    # to the dictionary, and make the values the reasons

    for i in range(len(unacceptable_animals)):
        animal = unacceptable_animals[i]
        reason = reasons[i]
        reasons_to_dislike_animals[animal] = reason

    print(reasons_to_dislike_animals)
