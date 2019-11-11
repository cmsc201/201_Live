# Sum the elements of a list recursively
# For two integers, x and y, compute xy recursively.
# Print out a list of elements recursively
# Calculate whether a string is a palindrome recursively


def fact(n):
    if n == 0:
        print("I'm the base case!  The answer is 1!")
        return 1
    else:
        clone_answer = fact(n - 1)
        print(clone_answer)
        return clone_answer * n



if __name__ == '__main__':
    print(fact(5))
