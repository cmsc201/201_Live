# How can we print the even numbers between two integers x and y with a for loop?
# How can we use range to go backwards through a list?
# Print all the elements of a list with their index!  How do?
if __name__ == '__main__':
    # fish_names = ["coelacanth", "plecostamus", "silver dollar", "croaker", "marty", "freddie fish", "nemo", "grouper"]
    # num = 0
    # for name in fish_names:
    #     print(name, "lives in the water!")
    #
    #     for other_name in fish_names:
    #         num += 1
    #         print(name, "eats", other_name)
    #
    # print(num)
    #
    # numbers = [1, 2, 3, 98745897]
    #
    # for i in range(len(numbers)):
    #     numbers[i] += 1
    #
    # print(numbers)

    # How can we print the even numbers between two integers x and y with a for loop?
    # start = 23
    # end = 31
    # for i in range(start, end+1):
    #     if i % 2 == 0:
    #         print(i)
    #
    # # How can we use range to go backwards through a list?
    # weird_super_powers = ["eat gravel", "travel forwards through time at normal speed", "eat food that is uncomfortably cold to most"]
    #
    # # for i in range(len(weird_super_powers) - 1, -1, -1):
    # #     print(weird_super_powers[i])
    #
    # # Print all the elements of a list with their index!  How do?
    # for i in range(len(weird_super_powers)):
    #     print(i, weird_super_powers[i])


    # bird_names = ["nuthatch", "sparrow", "big", "waldo", "birdperson"]
    #
    # for name in bird_names:
    #     if name == "big":
    #         print("I love sesame street!")
    #     elif name == "birdperson":
    #         for other_name in bird_names:
    #             if other_name != name:
    #                 print(name, "thinks", other_name, "is acceptable")
    #     else:
    #         print(name)

    # nuthatch
    # sparrow
    # I love sesame street!
    # waldo
    # birdperson thinks nuthatch is acceptable
    # birdperson thinks sparrow is acceptable
    # birdperson thinks big is acceptable
    # birdperson thinks waldo is acceptable


    # numbers = [1, 2, 3, 4]
    # # make it [2, 3, 4, 5]
    # for i in range(len(numbers)):
    #     print("I'm updating the value at index", i)
    #     numbers[i] += 1
    #
    # print(numbers)

    inappropriate_things_to_throw_at_birds = ["softballs", "chalk", "medium or large pebbles", "other birds"]

    for i in range(len(inappropriate_things_to_throw_at_birds)-1, -2, -1):
        print(inappropriate_things_to_throw_at_birds[i])

    # for i in range(100):
    #     print("Hello!")
