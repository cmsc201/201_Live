if __name__ == '__main__':
    # Make a dictionary of students where the names are the keys and the values are other dictionaries which store their email and favorite sound
    name = input("Enter a student name or QUIT when done")
    student_info = {}
    while name != "QUIT":
        email = input("Enter an email")
        sound = input("Enter their favorite sound")
        student_info[name] = {
            "email": email,
            "sound": sound,
        }
        name = input("Enter a student name or QUIT when done")
    print(student_info)
    for name in student_info:
        print("{} can be contacted at {} and their favorite sound is {}.".format(
            name, student_info[name]['email'], student_info[name]["sound"])
        )

    # Ben
    # benj1@umbc.edu
    # Cat purring
    # Charlie
    # cdog@dogmail.com
    # Food hitting a bowl

    # Ben can be contacted at benj1@umbc.edu and their favorite sound is cat purring
