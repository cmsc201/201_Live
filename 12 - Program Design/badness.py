def get_integer_from_user_in_range(prompt, range_bottom, range_top):
    """
    Displays the prompt to the user and validates against range.
    :param prompt: string to show user
    :param range_bottom: the lowest valid int (inclusively)
    :param range_top: the highest valid int(inclusively)
    :return: an integer in the specified range
    """
    output = int(input(prompt))
    while output < range_bottom or output > range_top:
        output = int(input(prompt))
    return output


def main():
    age = get_integer_from_user_in_range("What is your age? ", 0, 150)

    credits = get_integer_from_user_in_range("How many credits have your earned toward graduation (120 if done)?", 0, 120)

    arts_and_humanities_courses = get_integer_from_user_in_range("How many of your two required AH courses have you taken?", 0, 2)

    dnd_stats = ["strength", "dexterity", "charisma", "constitution", "wisdom", "intelligence"]
    user_stats = []
    index = 0
    while index < len(dnd_stats):
        stat = dnd_stats[index]
        user_stat = get_integer_from_user_in_range("What would your " + stat + " be if you were a dungeons and dragons character?", 3, 18)

        user_stats.append(user_stat)
        index += 1


main()
