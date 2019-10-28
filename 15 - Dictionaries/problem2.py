if __name__ == '__main__':
    # Make a dictionary of students where the names are the keys and the values are other dictionaries which store their email and favorite sound
    students = {}
    continue_response = "yes"
    while continue_response == "yes":
        name = input("name: ")
        food = input("favorite food:  ")
        sound = input("favorite sound:  ")


        students[name] = {
            "favorite food": food,
            "fave sound": sound
        }

        continue_response = input("Continue?").lower()
    print(students) # <-- should print all the info we put in
