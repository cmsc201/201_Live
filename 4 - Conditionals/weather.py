if __name__ == '__main__':
    is_hot = input("Hi!  Is it hot out?")
    # if it's hot out, ask them if it's humid
    if is_hot == "yes":
        is_humid = input("Do you like in Maryland?")
        # if it's humid tell them to wear shorts and no hat
        if is_humid == "yes":
            print("Wear shorts, leave the hat at home. Sorry, no doffing today.")
        # if it's hot and not humid, tell them just to wear shorts
        else:
            print("Wear shorts.  Hat optional.")
    # if it's not hot, ask them if it's raining
    else:
        is_raining = input("Is it wet out there?")
        if is_raining == "yes":
            # if it's raining ask them if it's cold
            is_cold = input("is it cold?")
            # if it's not cold tell them to wear a poncho
            if is_cold != "yes":
                print("Poncho!")
            # if it's cold tell them to wear a sweateroncho
            else:
                print("Be the first!  Sweateroncho (tm)!")
        # if it's not raining, tell them to dress warm
        else:
            print("Dress warm.")


    # age = int(input("What's your age?"))
    # if age > 18:
    #     print("You are an adult!")
    #
    # else:
    #     print("You are a kiddo!")
    # print("You are", age)
