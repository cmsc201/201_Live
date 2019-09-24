# How can we print the even numbers between two integers x and y with a for loop?
# How can we use range to go backwards through a list?
# Print all the elements of a list with their index!  How do?

if __name__ == '__main__':
    # fish_names = ["coelacanth", "plecostramus", "golfish", "bev", "nemo", "red lobster"]
    #
    # for fish_name in fish_names:
    #     print(fish_name, "lives in the water!")
    # print(fish_names)

    # numbers = [1, 2, 3, 4, 5]
    # for number in numbers:
    #     number += 1
    #     print(number)
    # print(numbers)
    #
    # for i in range(len(numbers)):
    #     numbers[i] += 1
    #
    # print(numbers)


# How can we print the even numbers between two integers x and y with a for loop?
    x = 22
    y = 32
    # if x % 2 == 0:
    #     for i in range(x, y+1, 2):
    #         print(i)
    # else:
    #     for i in range(x+1, y+1, 2):
    #         print(i)
    for i in range(x, y + 1):
        if i % 2 == 0:
            print(i)

