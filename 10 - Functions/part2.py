# playing with functions!
# square function that returns result
# def square_but_im_kinda_weird_about_four(number):
#     """
#     Squares a number
#     :param number: number to be squared
#     :return: square of number, unless number is 4 then number
#     """
#     if number == 4:
#         for i in [1, 2, 3, 4, 5]:
#             print(i)
#             if i == number:
#                 return number
#     return number ** 2
#
#
# if __name__ == '__main__':
#     user_input = int(input("#!"))
#     squared = square_but_im_kinda_weird_about_four(user_input)
#     squared += 6
#
#
#     print("The square of", user_input, " plus 6 is", squared)
# slide example

# def get_exclamation(age, this_string):
#     if age > 18:
#         return "My word!"
#     print("Whoa it’s a kiddo")
#     print(this_string)
#     return "Gee whiz!"
#
# if __name__ == '__main__':
#     age = int(input("What is your age?"))
#     some_thing = get_exclamation(age, "bears")
#
#     print("This is what it said", some_thing)

# def say_hey_to_the_kitties(num_kitties):
#     for i in range(num_kitties):
#         print("Hi kitties!")
#     if num_kitties == 3:
#         return "There were three kitties!"
#     num_kitties += 34
#
# if __name__ == '__main__':
#     kit_num = int(input("#?"))
#     print(say_hey_to_the_kitties(kit_num))
#     print(kit_num)

# example where None is returned even though there is a return statement

# example where we try to modify the parameters of a function

# add two numbers and return the sum

# return the sum of some numbers in a list

def sum_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
#
# if __name__ == '__main__':
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#     print(sum_list(numbers) * 2)

# return the odd numbers in  a list
def odds(numbers):
    output = []
    for number in numbers:
        if number % 2 == 1:
            output.append(number)
    return output

if __name__ == '__main__':
    # print the sum of all the odd numbers in the numbers list
    numbers = [1, 2, 3, 3, 3, 3,4, 5, 6,3, 7, 8]
    print(sum_list(odds(numbers)))
