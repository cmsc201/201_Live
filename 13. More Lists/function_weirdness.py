def increment_list(some_list):
    copy = some_list[:]
    index = 0
    while index < len(copy):
        copy[index] += 1
        index += 1
    return copy

# mutable function parameter example
def main():
    a = [1, 2, 3, 4]
    b = increment_list(a)
    print(a, b)  # <- should be different


main()