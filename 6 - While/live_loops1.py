if __name__ == '__main__':
    # for i in range(2, 101, 2):
    #     print(i)

# Make the user input values until they guess 4.
#     some_number = int(input("GUESS THE NUMBER MORTAL!"))
#     while some_number != 4:
#         print("HAHAHA!  YOUR PUNY HUMAN BRAIN CANNOT COMPREHEND MY POWER!")
#         some_number = int(input("GUESS THE NUMBER MORTAL!"))
#     print("FAIR ENOUGH!  HAVE A TINY CAKE!")
# Add numbers until the user puts in 0.
    number = int(input("Give me a number!  0 to stop!"))
    sum = 0
    while number != 0:

        if number == 68:
            print("Oh you!  I'm not adding that!")
        else:
            sum += number
        number = int(input("Give me a number!  0 to stop!"))
    print("The sum is", sum)
#     is_on_fire = True
#     time_on_fire = 0
#     while is_on_fire:
#         time_on_fire += 1
#         print("I've been on fire for", time_on_fire, "seconds")
#         if time_on_fire > 100:
#             is_on_fire = False

# Compute 10!
# Print even numbers between 0 and 100
