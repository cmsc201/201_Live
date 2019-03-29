
def add_to_list(a, item_to_add):
    output = []
    for thing in a:
        output.append(thing)

    output.append(item_to_add)
    return output


def main():
    a = [1, 2, 3, 4]
    print(add_to_list(a, 5))
    print(a)


main()
