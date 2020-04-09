# playing with functions!
# square function that returns result

# slide example


def get_exclamation(age):
    # secretly python did age = my_age
    if age > 18:
        return "My word!"
    print("Whoa it’s a kiddo")
    age += 1
    return "HI"


if __name__ == '__main__':
    my_age = 45
    get_exclamation(my_age)
    print(my_age)

# example where None is returned even though there is a return statement

# example where we try to modify the parameters of a function

# add two numbers and return the sum

# return the sum of some numbers in a list
