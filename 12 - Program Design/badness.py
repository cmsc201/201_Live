AGE_PROMPT = "What is your age? "
CREDIT_PROMPT = "How many credits have your earned toward graduation (120 if done)?"
AH_PROMPT = "How many of your two required AH courses have you taken?"


def get_int_in_range_from_user(min_value, max_value, prompt):
    """
    Shows string prompt to user and keeps prompting until valid int is entered
    :param min_value: the lowest valid int
    :param max_value: the highest valid int
    :param prompt: what to show the user
    :return: an integer in the specified range
    """

    output = int(input(prompt))
    while output < min_value or output > max_value:
        output = int(input(prompt))
    return output


def get_stats():
    dnd_stats = ["strength", "dexterity", "charisma", "constitution", "wisdom", "intelligence"]
    user_stats = []
    index = 0
    while index < len(dnd_stats):
        stat = dnd_stats[index]
        user_stat = int(input("What would your " + stat + " be if you were a dungeons and dragons character?"))
        while user_stat < 3 or user_stat > 18:
            user_stat = int(input("What would your " + stat + " be if you were a dungeons and dragons character?"))
        user_stats.append(user_stat)
        index += 1
    return user_stats


def main():
    age = get_int_in_range_from_user(0, 150, AGE_PROMPT)

    credits = get_int_in_range_from_user(0, 120, CREDIT_PROMPT)

    arts_and_humanities_courses = get_int_in_range_from_user(0, 2, AH_PROMPT)

    user_stats = get_stats()


main()
