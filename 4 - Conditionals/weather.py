if __name__ == '__main__':
    is_hot = input("Hi!  Is it hot out?")
    if is_hot == "yes":
        is_rainy = input("Is it raining?")
        if is_rainy == "yes":
            print("Take an umbrella!")
        else:
            print("Just wear shorts!")
    else:
        temp = int(input("What is the temp?"))
        is_cel = input("Is that in F or C")
        if is_cel == "F":
            temp = (5/9) * (temp - 32)
            print("Ok so it's",temp,"C")
        if temp > 0:
            print("bundle up!")
        else:
            print("whoa it's freezing!  stay inside!")
