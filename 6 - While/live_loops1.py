if __name__ == '__main__':
    # print even numbers from 1 to 100 (inclusively)

    # for i in range(1, 101):
    #     if i % 2 == 0:
    #         print(i)

    # Make
    # the
    # user
    # input
    # values
    # until
    # they
    # guess
    # 4.

    # number = int(input("Please enter a number to help me feel better about myself.  Guess wisely. "))
    # while number == 4:
    #     print("Oh bother.  That's not want I wanted.")
    #     number = int(input("Try again? "))
    #
    # print("You got it!")

    # name = input("DO NOT SPEAK MY NAME!")
    # while name != "voldestilskin":
    #     name = input("That's right.  Cower.")
    #
    # print("YOU HAVE DEFIED ME FOR THE LAST TIME!")

    name = input("Say my name.  I dare you.")
    times_names_said = 0
    while name == "beetlejuice" and times_names_said < 3:
        times_names_said += 1
        if times_names_said < 3:
            input("That's me.  What up?")
        else:
            print("alright, I'm already here!")

    print("Yeah, bye.")

    # Please enter a number to help me feel better about myself.  Guess wisely. 68
    # Oh bother.  That's not want I wanted.
    # Try again? 54
    # Oh bother.  That's not want I wanted.
    # Try again? 32
    # Oh bother.  That's not want I wanted.
    # Try again? 4

    # add numbers till the user puts in 10
    # do this next class!!!!!!
