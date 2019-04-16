

# def print_list_in_reverse(some_list):
#     if (len(some_list) != 0):
#         print_list_in_reverse(some_list[1:])
#         print(some_list[0])
#
# def main():
#     # notably absent: the count
#     list_of_overrated_vampires = ["chocula", "dracula", "edward cullen", "nosferatu"]
#     print_list_in_reverse(list_of_overrated_vampires)
#
# main()

# factorial(number) is factorial(number-1) * number OR
# factorial(1) and factorial(0) = 1
# def factorial(number):
#     if number == 1 or number == 0:
#         return 1
#     else:
#         what_my_clone_did = factorial(number - 1)
#         return what_my_clone_did * number
# def main():
#     print(factorial(999))
#
# main()
#
# def fib(n):
#     first_term = 1
#     second_term = 1
#     print(first_term)
#     print(second_term)
#     for i in range(n-2):
#         temp = second_term
#         second_term = first_term + second_term
#         first_term = temp
#         print(second_term)
#
# def fib_rec(n):
#     print(n)
#     if n == 1 or n == 2:
#         return 1
#     return fib_rec(n-1) + fib_rec(n-2)
#
# def main():
#     print(fib_rec(10))
#
# main()


# Sum the elements of a list recursively
# def sum(a_list):
#     # base case
#     if len(a_list) == 1:
#         return a_list[0]
#     # recursion
#     return a_list[0] + sum(a_list[1:]) # add the first number, to the sum of the rest of the list
#
# def main():
#     print(sum([1, 2, 3, 4]))

# main()

# For two integers, x and y, compute x^y recursively.
def power(x, y):
    # ???
    # if base_case:
    #     return some_thing_easy
    # return my part + power(smaller subproblem)
    if y == 0:
        return 1
    return power(x, y - 1) * x

print(power(2, 3))
print(power(3, 3))

# Print out a list of elements recursively
# done!
# Calculate whether a string is a palindrome recursively

def canPay(amount, coins):
    if amount == 0:
        return True
    if len(coins) == 0:
        return False
    for i in range(len(coins)):
        coin = coins[i]
        smallerCoins = coins[:i] + coins[i+1:]
        if canPay(amount - coin, smallerCoins):
            return True
    return False

print(canPay(100, [25, 25, 25, 5, 5, 5, 5]))
print(canPay(50, [5, 10]))
