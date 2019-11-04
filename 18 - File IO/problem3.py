if __name__ == '__main__':
    # Read in a file of integers and print their average
    with open("someints.txt", "r") as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            sum += int(line)
        print(sum/len(lines))
