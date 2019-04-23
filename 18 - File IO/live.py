# read in a file, and count how many functions are defined there
def functionCount(filename):
    file = open(filename, 'r')
    contents = file.read()
    file.close()

    count = 0
    for i in range(len(contents)):
        if i + 4 < len(contents) and contents[i:i+4] == "def ":
            count += 1

    return count


def main():
    print(functionCount("live.py"))

main()
# read in a file, find each time it says dogs and replace it with cats, write out the file
# Read in a file of integers and print their average