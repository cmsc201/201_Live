# playing with functions!
# square function that returns result
# def square(number):
#     number = number ** 2
#
#
# def main():
#     number = 3
#     print(square(number))
#     print(number)
#     # if square(50) > 3:
#     #     print("duh")
#     # num = 0
#     # while square(num) < 300000:
#     #     print(num)
#     #     num += 1
#     # print(result)
# #
# main()
# slide example

# def getExclamation(age):
#     if age > 18:
#         return "My word!"
#     else:
#         return "Oh this then"
#
#
# def main():
#     something = getExclamation(4)
#     print("Main() has something to say:")
#     print(something + "3")
#     print(getExclamation(30))
#
# main()

# example where None is returned even though there is a return statement

# example where we try to modify the parameters of a function

# add two numbers and return the sum
def add(num1, num2):
    return num1 + num2

def greater_than(num1, num2):
    return num1 > num2


# return the sum of some numbers in a list
def sum_of_list(some_list):
    index = 0
    sum = 0
    while index < len(some_list):
        sum += some_list[index]
        index += 1
    return sum

def main():
    print(sum_of_list([1, 2, 3, 4]))

main()