def get_input_in_range(min_value, max_value, prompt):
    user_input = int(input(prompt))
    while user_input < min_value or user_input > max_value:
        user_input = int(input(prompt))
    return user_input


def main():
    get_input_in_range(0, 150, "What is your age? ")

    get_input_in_range(0, 120, "How many credits have your earned toward graduation (120 if done)?")

    get_input_in_range(0, 2, "How many of your two required AH courses have you taken?")

    dnd_stats = ["strength", "dexterity", "charisma", "constitution", "wisdom", "intelligence"]
    user_stats = []
    index = 0
    while index < len(dnd_stats):
        stat = dnd_stats[index]
        user_stat = get_input_in_range(3, 18, "what is your {} stat?".format(stat))
        user_stats.append(user_stat)
        index += 1


if __name__ == '__main__':
    main()
