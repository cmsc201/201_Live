def main():
    is_hot = input("Hi!  Is it hot out?").lower()
    if is_hot.lower() == "yes":
        is_raining = input("It wet out there?")
        if is_raining == "yes":
            print("bring an umbrella")
        else:
            bearness = input("Is there a large bear at your door?")
            if bearness == "yes":
                print("play dead, cause that totally works")
        really = input("like super hot?")
        if really == "super":
            print("play dead")
        else:
            print("something easy breezy, like a sundress")
    else:
        music = input("what is your favorite musical genre")
        if music == "jazz" or music == "jazz funk" or music == "jazz fusion" or music == "swing":
            print("How about a fedora (but also with a suit, please)")
        elif music == "polka metal fusion":
            print("Let's get lunch together, and talk about your life decision")
        else:
            print("Oh, tell me more about", music, "and I will nod.")


main()
#
#
# age = int(float(input("What’s your age?")))
# if age >= 18:
# 	print("You are an adult!")
# 	print("Let's go be adults")
# elif age > 3:
# 	print("hello kiddo!")
# 	print("want some trix?")
# elif age > 0:
# 	print("you are so smarrt")
# else:
# 	print("Hey timey mctimerson")
# # if age < 0:
# # 	print("Welcome time traveller!")
# print("You are", age)
