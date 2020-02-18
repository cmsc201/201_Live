if __name__ == '__main__':
    fishes = ["carp", "snapper", "tuna", "trout", "squirtle", "salmon", "cod", "anglerfish", "mahi mahi", "bass", "barracuda", 'eel', 'sharks' * 3]

    for fish in fishes:
        if fish == "squirtle":
            print("That ain't not fish, nerd!")
        else:
            print("{} lives in the water".format(fish))

    # write a loop that prints all integers from 1 to 100 inclusively each on its own line
    for i in range(1, 101, 1):
        print(i**2)

    # remember
    # len() is a thing
    # range() is a thing
    # indexing into a list with an index is a thing (fishes[0] is "carp")
    # print each fish with their index e.g.
    """
    carp 0 
    snapper 1
    tuna 2
    ...
    """
    for i in range(len(fishes)):
        print(fishes[i], i)

    """
    CHANGE the list to have
    ["carp is fish number 1", "snapper is fish number 2, ...]
    
    how do I modify an individual element of a list?
    """
    for i in range(len(fishes)):
        new_value = "{} is fish number {}".format(fishes[i], i + 1)
        #then I do something to modify the list
        fishes[i] = new_value



    print(fishes) # should print ["carp is fish number 1", "snapper is fish number 2", ...]