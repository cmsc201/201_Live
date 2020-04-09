# Sum the elements of a list recursively
# For two integers, x and y, compute xy recursively.
# Print out a list of elements recursively
# Calculate whether a string is a palindrome recursively


def print_list(some_list):
    if len(some_list) == 1:
        print(some_list[0])
    else:
        print(some_list[0])
        print_list(some_list[1:])


def factorial(number):
    # base case i.e. what is the easy version of this problem to solve
    # Base case:  1! => 1
    if number == 1:
        return 1
    # recursive case i.e. what small problem do we ask our clone to solve, and how do solve our problem
    # with the clone's answer
    # we want to return number * number-1! e.g. 6! = 6 * 5!
    return factorial(number - 1) * number


def fib_iter(nth):
    if nth == 1:
        return 1
    if nth == 2:
        return 1
    previous = 1
    two_previous = 1
    for i in range(3, nth+1):
        temp = previous + two_previous
        two_previous = previous
        previous = temp
    return previous

times = 0
def fib(nth):
    """
    Recursively!
    :param nth:
    :return: the nth term of the fib sequence
    """
    """
    What is the base case?
    How do I describe a subproblem of my problem
    If I repeated making that subproblem, do I get a base case?
    At this point we should TRUST the recursive calls
    Assuming I have the solution to the subproblem, HOW DO I SOLVE MY PROBLEM WITH IT?
    I should be careful to make sure I’m returning the answer to MY PROBLEM
    """
    if nth == 1:
        return 1
    if nth == 2:
        return 1
    # print(nth)
    global times
    times += 1 #FORBIDDEN
    return fib(nth - 1) + fib(nth - 2)

if __name__ == '__main__':
    print(fib_iter(500))
    print(times)