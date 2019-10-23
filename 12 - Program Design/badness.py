def get_value_in_range_from_user(prompt, min, max):
    value = int(input(prompt))
    while value < min or value > max:
        value = int(input(prompt))
    return value

if __name__ == '__main__':
    age = get_value_in_range_from_user("What is your age?", 0, 150)

    credits = get_value_in_range_from_user(
        "How many credits have your earned toward graduation (120 if done)?"), 0, 120

    arts_and_humanities_courses = get_value_in_range_from_user("How many of your two required AH courses have you taken?", 0, 2)

    dnd_stats = ["strength", "dexterity", "charisma", "constitution", "wisdom",
                 "intelligence"]
    user_stats = []
    for stat in dnd_stats:
        user_stat = get_value_in_range_from_user("What would your " + stat + " be if you were a dungeons and dragons character?", 3, 18)
        user_stats.append(user_stat)
