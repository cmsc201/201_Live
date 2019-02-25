# Section 7?
# Road trip for the family simulator.  The "player" is the parent.
# Kids are going to say "are we there yet?" until the road trip is ended due to:
#
# Arrive at McDonald's
# Bears
# Arrive at destination
# Parents curse
# Throwing up
# Crashing the car
# kids ask 10 times

ANNOYING_KIDS_PHRASE = "Are we there yet?"
ARRIVE_AT_MCDS = "HEY IT'S THE CLOWN AND I'M HUNGRY!"
BEARS = "OMG how long has there been a sun bear in the car?"
ARRIVED = "Yes"
THROWING_UP = "Kiddo you don't look so good."
CRASHING = "Is that a bear in the road?"
CURSE = "May romcoms always make you weep."
PARENTS_THRESHOLD_FOR_REPITITION = 3


def main():
    drivin = True
    count = 0
    while drivin:

        count += 1
        parents_said = input(ANNOYING_KIDS_PHRASE)
        if parents_said == ARRIVED:
            print("Out of the car, long hair.")
            drivin = False
        elif parents_said == BEARS:
            print("get out, it's BEARS")
            drivin = False
        elif parents_said == THROWING_UP:
            print("Gross.")
            drivin = False
        elif parents_said == CRASHING:
            print("Yay we got the bear!")
            drivin = False
        elif parents_said == CURSE:
            print("What's a romcom?")
            drivin = False
        elif count >= PARENTS_THRESHOLD_FOR_REPITITION:
            print("I'm turning this car around.")
            drivin = False
        elif parents_said == ARRIVE_AT_MCDS:
            print("ooo nuggets")
            drivin = False


main()
