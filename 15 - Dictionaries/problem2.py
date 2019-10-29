if __name__ == '__main__':
    # Make a dictionary of students where the names are the keys and the values are other dictionaries which store their favorite food and favorite sound


    go = True
    student_data = {}
    while go:
        name = input("name? ")
        food = input("food? ")
        sound = input("sound? ")

        student_data[name] = {
            "food": food,
            "sound": sound
        }

        go = input("go?").lower() == "yes"

    print(student_data)
