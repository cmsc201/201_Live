# def print_message(message):
#     print(message)
#     print_message(message)
#
# def main():
#     print_message("And on")
#
# main()

# what is a list
# list is empty OR a list is an item followed by a list

# def print_list(stuff):
#     if len(stuff) == 0:
#         print("Uhh, I got nothing to do")
#     else:
#         print(stuff[0])
#         print_list(stuff[1:]) #break it down
#         # print_list(stuff)  <- don't do this
#
# def main():
#     worst_clone_movies = ["clone wars", "face/off", "total recall"]
#
#     print_list(worst_clone_movies)
#
# main()

# n!
# n * (n-1)!
#
# def factorial(n):
#     if n == 1:
#         print("That's easy, it's 1!")
#         return 1
#     print("Ummmm, hey lemme call my buddy knows about factorial")
#     what_my_buddy_said = factorial(n - 1)
#     return n * what_my_buddy_said
#
#
# def main():
#     print(factorial(10))
#
#
# main()

# fib loop
#
# def fib_loop(n):
#     first_item = 1
#     second_item = 1
#
#     print("We're here:", first_item)
#     print("We're here:", second_item)
#
#     for i in range(n - 2):
#         temp = second_item
#         second_item = first_item + second_item
#         first_item = temp
#         print("We're here:", second_item)
#     print("The answer is", second_item)
#
# def fib_rc(n):
#     print("we're here:", n)
#     if n == 1 or n == 2:
#         return 1
#     return fib_rc(n - 2) + fib_rc(n - 1)
#
# def main():
#     # fib_loop(15)
#     print("The answer is", fib_rc(15))

# main()

# Print the sum of a list *recursively*
# def sum_list(theList):
#     if base_case:
#         return the easy answer
#     else:
#         return some small part + my clones work on the remaining subproblem

# def sum_list(theList):
#
#     if len(theList) == 0:
#         return 0
#     else:
#         import pdb; pdb.set_trace()
#         return theList[0] + sum_list(theList[1:])
#
# print(sum_list([4, 5, 6, 7]))


# implement power(x, y) which returns x ** y but do it recursively
def power(x, y):
    # if base_case:
    #     return simple_answer
    # return my_part + power(a smaller problem without my part)
    if y == 0:
        return 1
    return power(x, y - 1) * x

print(power(2, 3)) # 8
print(power(12, 2)) # 144
print(power(100, 0)) # 1


# given a cost and a list of coin values, determine whether you can make perfect change
def canMakeChange(price, coins):
    # if base_case:
    #     return simple answer
    # return recursive_call + my_subproblem
    if price == 0:
        return True # yeah!
    if len(coins) == 0:
        return False
    for i in range(len(coins)):
        smaller_bag = coins[:i] + coins[i+1:]
        new_cost = price - coins[i]
        if new_cost > 0 and canMakeChange(new_cost, smaller_bag):
            return True
    return False

print(canMakeChange(100, [1, 1, 1, 25, 19, 18, 34]))
# Calculate whether a string is a palindrome recursively
