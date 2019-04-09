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
def factorial(n):
    if n == 1:
        print("That's easy, it's 1!")
        return 1
    print("Ummmm, hey lemme call my buddy knows about factorial")
    what_my_buddy_said = factorial(n - 1)
    return n * what_my_buddy_said


def main():
    print(factorial(10))


main()

# Print out a list of elements recursively
# Calculate whether a string is a palindrome recursively
