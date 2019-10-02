if __name__ == '__main__':
    arrived = False
    times_we_said_no = 0
    while not arrived:
        response = input("Are we there yet? ")

        if response == "no":
            times_we_said_no += 1
        elif response == "yes":
            arrived = True
        elif response == "bears!":
            arrived = True
            print("OMG thems bears!  Turn it around!")
        elif response == "b room break":
            print("Ok, we'll take the exit")

        if times_we_said_no >= 5:
            arrived = True
            print("I'm turning car around!")
