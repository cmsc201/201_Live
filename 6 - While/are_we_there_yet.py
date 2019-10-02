# if __name__ == '__main__':
#     arrived = False
#     times_we_said_no = 0
#     while not arrived:
#         response = input("Are we there yet? ")
#
#         if response == "no":
#             times_we_said_no += 1
#         elif response == "yes":
#             arrived = True
#         elif response == "bears!":
#             arrived = True
#             print("OMG thems bears!  Turn it around!")
#         elif response == "b room break":
#             print("Ok, we'll take the exit")
#
#         if times_we_said_no >= 5:
#             arrived = True
#             print("I'm turning car around!")



AFFIRMATIVE = "yes"
PATIENCE_COUNT_LIMIT = 10
NEGATIVE = "no"
BEAR = "gasp! bear!"
GROWL = "grr"

if __name__ == '__main__':
    pulled_over = False
    times_i_have_said_no = 0
    while not pulled_over:
        response = input("Are we there yet?")

        # if we're there, end!
        if response == AFFIRMATIVE:
            pulled_over = True
            print("Yay, we're there!")

        # if we've said "no" 10 times, pull over
        # ???
        if response == NEGATIVE:
            times_i_have_said_no += 1

        if times_i_have_said_no >= PATIENCE_COUNT_LIMIT:
            print("I'm turning this thing around!")
            pulled_over = True

        if response == GROWL and times_i_have_said_no >=3:
            print("I've had enough of this")
            pulled_over = True

        if response == BEAR:
            print("Oh dear, it's a bear")
            pulled_over = True

































