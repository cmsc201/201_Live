AFFIRMATIVE = "yes"
BEAR = "omg it's a bear"
NEGATIVE = "no"

if __name__ == '__main__':
    pull_over = False
    times_i_said_no = 0
    while not pull_over:
        # continue our family road trip
        happenings = input("Are we there yet?")
        if happenings == AFFIRMATIVE:
            pull_over = True
        elif happenings == BEAR:
            pull_over = True
            print("HIDE KIDS!")
        elif happenings == NEGATIVE:
            times_i_said_no += 1
            print(times_i_said_no)
            if times_i_said_no > 4:
                print("I'm turning this car around!")
                pull_over = True

    print("I'm getting off the road!")