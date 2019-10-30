# read in a file, and count how many functions are defined there
def count_defs(filename):
    """
    Given a file name, counts how many python functions are defined there
    :param filename:  the string of a file name
    :return: an integer for how many functions are defined in that file
    """
    with open(filename, "r") as f:
        # f.read() or f.readlines()???
        function_count = 0
        for line in f.readlines():
            if line.lower().strip().startswith("def"):
                function_count += 1

    return function_count


if __name__ == '__main__':
    print("This code has {} functions.".format(count_defs("live.py")))
    print("This code has {} functions.".format(count_defs("/Users/benj1/src/201_Live/10 - Functions/live.py")))

# read in a file, find each time it says dogs and replace it with cats, write out the file
# Read in a file of integers and print their average
