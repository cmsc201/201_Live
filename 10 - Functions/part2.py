# playing with functions!
# square function that returns result
# WEIRD_EXAMPLE_SENTINEL = 1000
#
# def square(number):
#     return number ** 2
#
# def main():
#     answer = square(25) + 15
#     sample_list = [1, 2, 3, square(2)]
#     print(sample_list)
#     print(square(4))
#     if square(5) == 3:
#         print("Yeah, I knew that")
#     i = 0
#     while square(i) < WEIRD_EXAMPLE_SENTINEL:
#         print(square(i))
#         i += 1
#
#     print("mystery:",square(square(5)))
#
#     print(answer)
#
# main()


# slide example

# def getExclamation(age):
#     if age > 18:
#         return "My word!"
#     return "Whoa it’s a kiddo"
#
#
# def main():
#     print("here comes 3")
#     thing_to_say = getExclamation(3)
#     print(thing_to_say)
#     print("now for 19")
#     print(getExclamation(19))
#     print("done")
#
# main()

# example where None is returned even though there is a return statement

# example where we try to modify the parameters of a function

# def add(num1, num2, answer):
#     answer = num1 + num2
#
# def main():
#     answer = 0
#     add(3, 3, answer)
#     print(answer)
#
# main()

# add two numbers and return the sum

# return the sum of some numbers in a list

def get_sum(some_list):
    i = 0
    sum = 0
    while i < len(some_list):
        sum += some_list[i]
        i += 1
    return sum

def main():
    print(get_sum([1, 2, 3, 4, 5, 60]))

main()
