if __name__ == '__main__':

    with open("animals.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line == "deep sea angler":
            print(line, "is formidable (also pretty)")
        else:
            print(line + " is pretty!")