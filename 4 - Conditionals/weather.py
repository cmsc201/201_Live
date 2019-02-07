def main():
    is_hot = input("Hi!  Is it hot out?")
    if is_hot.lower() == "yes":
        is_raining = input("Is it raining?")
        if is_raining == "yes":
            print("Take an umbrella!")
        elif is_raining == "no":
            print("Something light, perhaps a shawl.")
    else:
        we_cool = input("Hey.  Hey.  We cool?")
        if we_cool == "yes":
            print("cool")
        else:
            something = input("What is your favorite food?")
            if something == "pizza":
                print("How original.  What if it's on a bagel??")
            if something == "roasted turnips with polenta":
                print("Wow, I don't think I'm fancy enough for you.")
            else:
                print("Oh.  Cool.")



main()

