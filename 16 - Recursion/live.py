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
def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        what_my_clone_did = factorial(number - 1)
        return what_my_clone_did * number

def main():
    print(factorial(10))

main()