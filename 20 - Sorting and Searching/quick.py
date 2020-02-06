def quick(some_list):
    """
    sort a list of comparable items
    :param some_list:
    :return: the sorted list
    """
    if not some_list:
        return some_list
    small = []
    large = []

    pivot = some_list[0]

    for item in some_list[1:]:
        if item < pivot:
            small.append(item)
        else:
            large.append(item)

    small = quick(small)
    large = quick(large)
    small.append(pivot)
    #small.extend(large)
    for item in large:
        small.append(item)
    return small

if __name__ == '__main__':
    print(quick([1]))
    print(quick([]))
    print(quick([1,2,3,4]))
    print(quick([1,2,3,2,2,2,2,2,2,4]))
    print(quick([5,4,8,3,9]))