if __name__ == '__main__':
    is_hot = input("Hi!  Is it hot out?")
    # if it's hot, ask them about whether it's raining
    if is_hot == "yes":
        is_raining = input("it rainin?")
        # if it's hot and raining, tell them to wear a poncho
        if is_raining == "yes":
            print("wear a poncho!")
        # otherwise, tell them to wear shorts
        else:
            print("wear shorts!")
    # if it's not hot ask them about the wind
    else:
        is_wind = input("Hey.  Hey.  Wind?")
        # if it's not windy ask them about rain
        if is_wind != "yes":
            is_raining = input("It wet out?")
            # if it's not rainy have them wear a parka
            if is_raining != "yes":
                print("Parka time!")
            else:
            # if it's cold and rainy, tell them to wear a sweateroncho
                print("Sweateroncho is for you.")
        # if it's cool and calm, wear a fashionable clothing situation
        else:
            print("Stay warm!")

