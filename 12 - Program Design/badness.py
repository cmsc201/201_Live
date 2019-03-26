def main():
    age = int(input("What is your age? "))
    while age < 0 or age > 150:
        age = int(input("What is your age? "))

    credits = int(input("How many credits have your earned toward graduation (120 if done)?"))
    while credits < 0 or credits > 120:
        credits = int(input("How many credits have your earned toward graduation (120 if done)?"))

    arts_and_humanities_courses = int(input("How many of your two required AH courses have you taken?"))
    while arts_and_humanities_courses < 0 or arts_and_humanities_courses > 2:
        arts_and_humanities_courses = int(input("How many of your two required AH courses have you taken?"))

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

main()