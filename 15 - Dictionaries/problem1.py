if __name__ == '__main__':
    # Take two lists of values and make a dictionary that associates the keys in one list with the values of the other list
    cat_friends = ["jules", "tybalt", "scooter"]
    dog_friends = ["charlie", "char", "chuckadero"]
    snuggle_buddies = {}
    # loop through one of the two lists in a for i loop
    # add the item from the cat list in as a key to a dictionary,
    # the value will be the item in the same position in the dog list

    # for i in range(??):
    #     cat = ??
    #     dog = ??
    #     snuggle_buddies[??] = ???
    #
    for i in range(len(cat_friends)):
        cat = cat_friends[i]
        dog = dog_friends[i]
        snuggle_buddies[cat] = dog

    print(snuggle_buddies)






