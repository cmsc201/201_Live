# This will print "are we there yet until a variety of statements are true"
#
# we will stop if we've heard "are there yet 10 times"
# we will stop if the parent says "yes"
# we will stop if the parent curses
# we will stop if we gotta go
# we will stop if we crash

QUESTION_LIMIT = 10
AFFIRMATIVE_ANSWER = "yes"
CURSE = "May your rice crispies always remain silent."
CRASH = "Is that a deer?"

def main():
    should_we_pull_over = False
    questions_asked = 0
    QUESTION_LIMIT = 5
    while not questions_asked >= QUESTION_LIMIT:
        what_the_parent_said = input("Are we there yet?")
        questions_asked += 1
        if questions_asked >= QUESTION_LIMIT:
            print("I am turning this car around!")
            should_we_pull_over = True
        elif what_the_parent_said == CRASH:
            print("Man, you should pay more attention, dad/mom/parental unit.")
            should_we_pull_over = True
        elif what_the_parent_said == AFFIRMATIVE_ANSWER:
            print("Yay, we're here!  Ice cream!")
            should_we_pull_over = True
        elif what_the_parent_said == CURSE:
            print("Whoa, that escalated.")
            should_we_pull_over = True


main()