# Sum the elements of a list recursively

def sum_list(some_list):
    if not some_list:
        return 0
    return some_list[0] + sum_list(some_list[1:])


if __name__ == '__main__':
    print(sum_list([1,2,3,4,5])) # prints 15
    print(sum_list([1,1,1,1,1])) # print 5
    print(sum_list([]))  # prints 0

# For two integers, x and y, compute xy recursively.
# Print out a list of elements recursively
# Calculate whether a string is a palindrome recursively


# def fact(n):
#     if n == 1:
#         return 1
#     return fact(n-1) * n
#
# if __name__ == '__main__':
#     print(fact(6))
#
#
# def fibitr(n):
#     first_item = 1
#     second_item = 1
#     current_item = second_item
#     if n == 1 or n == 2:
#         return 1
#     for i in range(n-2):
#         current_item = first_item + second_item
#         first_item = second_item
#         second_item = current_item
#     return current_item
#
#
# def fibrec(n):
#     print(n)
#     if n == 1 or n == 2:
#         return 1
#     return fibrec(n - 1) + fibrec(n - 2)
#
#
# if __name__ == '__main__':
#     # for i in range(1, 11):
#     #     print(fibitr(i))
#     # for i in range(1, 11):
#     #     print(fibrec(i))
#     print(fibrec(5))
