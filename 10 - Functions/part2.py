# playing with functions!
# square function that returns result
# def square(mister_number_value_time):
#     return mister_number_value_time ** 2
#
#
# if __name__ == '__main__':
#     number = 6
#
#     squared = square(6)
#     print(squared + 6)
#
# # puppy printing
#
# def print_list(list_to_print):
#     for item in list_to_print:
#         print(item)
#
#
# if __name__ == '__main__':
#     puppies = ["charles", "charlie"]
#     kitties = ["jules", "tybalt"]
#     print_list(puppies)
#     print_list(kitties)
#
#     kitty = int(input("give me a kitty age"))
#
# def get_exclamation(age):
#     if age > 18:
#         return "My word!"
#
#     print("Whoa it’s a kiddo")
#     return "Gee whiz!"
#
# if __name__ == '__main__':
#     # user_age = int(input("How old are you?"))
#     # message = get_exclamation(user_age)
#     # print("Your greeting is", message)
#     message1 = get_exclamation(3)
#     print("The space in between")
#     message2 = get_exclamation(22)
#     print("Message 1 was", message1)

# slide example

# def getExclamation(age):
# 	if age > 18:
# 		return "My word!"
# 	print("Whoa it’s a kiddo")
# 	return "Gee whiz!"

# example where None is returned even though there is a return statement
def get_exclamation(age):
    age += 1000000
    if age > 18:
        return age
    elif age > 12:
        return "aw hey"
    return "Oh shoot, I didn't want to be here"

if __name__ == '__main__':
    user_age = int(input("How old are you?"))
    message = get_exclamation(user_age)
    print(user_age)
    print("Your greeting is", message)

# example where we try to modify the parameters of a function

# add two numbers and return the sum

# return the sum of some numbers in a list
