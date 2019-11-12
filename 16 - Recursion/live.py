# Sum the elements of a list recursively
def sum_list(a_list):
    # base case
    if not a_list:
        return 0
    # recursive call
    return a_list[0] + sum_list(a_list[1:])

if __name__ == '__main__':
    print(sum_list([1, 2, 3, 4]))
    print(sum_list([1, 1, 1, 1]))
    print(sum_list([]))

# For two integers, x and y, compute xy recursively.
# Print out a list of elements recursively

# Calculate whether a string is a palindrome recursively


# def fact(n):
#     if n == 0:
#         print("I'm the base case!  The answer is 1!")
#         return 1
#     else:
#         clone_answer = fact(n - 1)
#         print(clone_answer)
#         return clone_answer * n
#
#
#
# if __name__ == '__main__':
#     print(fact(5))
#
# def fib4(nth):
#     first = 1
#     second = 1
#     current = 1
#     if nth == 1 or nth == 2:
#         return 1
#     for i in range(nth-2):
#         current = first + second
#         first = second
#         second = current
#     return current
#
# def fib(nth):
#     """
#     Computes the nth term of the fibonacci sequence
#     :param nth: an integer representing the position of the requested term in
#     the fibonacci sequence
#     :return: the value of the nth term of the fib sequence
#     """
#     # print("fib", nth)
#     #base case
#     if nth == 1 or nth == 2:
#         return 1
#
#     #recurse case
#     # do I do something with the return?
#     # does it reach the base case?
#     # do I return it?
#     else:
#         return fib(nth-1) + fib(nth-2)
#
# if __name__ == '__main__':
#
#     print(fib(5))
#     print(fib4(5))
