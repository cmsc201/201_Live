def increment_list(a):
    index = 0
    while index < len(a):
        a[index] += 1
        index += 1
    return a

# mutable function parameter example
def main():
    a = [1, 2, 3, 4]
    b = increment_list(a)
    print(a, b)  # <- should be different


main()