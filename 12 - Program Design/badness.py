def get_value_in_range(prompt, minimum, maximum):
    """
    Asks the user for input in a range until they provide a reasonable value
    :param prompt: what we prompt the user with
    :param min: the minimum accepted value
    :param max: the max accepted value
    :return: Return the value the user inputted
    """
    user_input = int(input(prompt))
    while user_input < minimum or user_input > maximum:
        user_input = int(input(prompt))
    return user_input


if __name__ == '__main__':

    age = get_value_in_range("What is your age?", 0, 150)

    credits = get_value_in_range("How many credits have your earned toward graduation (120 if done)?", 0, 120)

    arts_and_humanities_courses = get_value_in_range("How many of your two required AH courses have you taken?", 0, 2)

    dnd_stats = ["strength", "dexterity", "charisma", "constitution", "wisdom", "intelligence"]
    user_stats = []
    index = 0
    while index < len(dnd_stats):
        stat = dnd_stats[index]
        user_stat = get_value_in_range("What would your " + stat + " be if you were a dungeons and dragons character?", 3, 18)
        user_stats.append(user_stat)
        index += 1
