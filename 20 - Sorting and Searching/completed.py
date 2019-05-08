import random


def bubblesort(the_list):
    """
    Sorts a list
    :param the_list: a list of values
    :return: a sorted version of the_list
    """
    compare_count = 0
    swapped = True
    last_index = len(the_list)
    while swapped and last_index > 0:

        swapped = False
        for i in range(last_index - 1):
            compare_count += 1
            if the_list[i] > the_list[i + 1]:
                temp = the_list[i]
                the_list[i] = the_list[i + 1]
                the_list[i + 1] = temp
                swapped = True
        last_index -= 1
    print(compare_count, "comparisons done for bubble sort.")
    return the_list


def quicksort(the_list, count_list):
    """
    Quicksort with a list that stores the comparisons done in the recursive calls
    :param the_list: list to be sorted
    :param count_list: list of integers representing comparison counts
    :return: a sorted version of the_list
    """
    compares = 0
    bigger = []
    smaller = []
    if len(the_list) < 2:
        return the_list
    toCompare = the_list[0]
    for i in range(1, len(the_list)):
        compares += 1
        if the_list[i] < toCompare:
            smaller.append(the_list[i])
        else:
            bigger.append(the_list[i])
    # combine lists
    output = quicksort(smaller, count_list)
    output.append(toCompare)
    output.extend(quicksort(bigger, count_list))
    count_list.append(compares)
    return output


def quick_sort_with_count(copy):
    """
    helper to deal with counting compares
    :param copy:
    :return:
    """
    count_list = []
    output = quicksort(copy, count_list)
    sum = 0
    for i in range(len(count_list)):
        sum += count_list[i]
    print(sum, "comparisons done for quick sort.")
    return output


def selectsort(the_list):
    """
    Sorts a list
    :param the_list: a list of values
    :return: a sorted version of the_list
    """
    compares = 0
    last_index = len(the_list) - 1
    while last_index > 0:
        max = the_list[0]
        max_position = 0
        for i in range(last_index):
            compares += 1
            if the_list[i] > max:
                max = the_list[i]
                max_position = i
        the_list[max_position] = the_list[last_index]
        the_list[last_index] = max
        last_index -= 1
    print(compares, "comparisons done for select sort.")
    return the_list


def linear_search(a_list, to_find):
    compares = 0
    for i in range(len(a_list)):
        compares += 1
        if a_list[i] == to_find:
            print(compares, "comparisons for linear search")
            return i
    print(compares, "comparisons for linear search")
    return -1


def binary_search_actual(sorted, to_find, compare_list):
    if len(sorted) == 0:
        return False
    middle_index = len(sorted) // 2
    middle = sorted[middle_index]
    compare_list.append(1)
    if middle == to_find:
        return True
    if to_find < middle:
        return binary_search_actual(sorted[:middle_index], to_find, compare_list)
    else:
        return binary_search_actual(sorted[middle_index + 1:], to_find, compare_list)


def binary_search(sorted, to_find):
    count_list = []
    output = binary_search_actual(sorted, to_find, count_list)
    sum = 0
    for i in range(len(count_list)):
        sum += count_list[i]
    print(sum, "comparisons done for binary search.")
    return output


def main():
    some_list = [3, 54, 6, 7, 90, 21]
    copy = list(some_list)
    print(bubblesort(copy))
    copy = list(some_list)
    print(selectsort(copy))
    copy = list(some_list)
    print(quick_sort_with_count(copy))

    some_list = []
    SOME_LARGE_NUMBER = 10000
    for i in range(SOME_LARGE_NUMBER):
        some_list.append(random.randint(0, 1000000))

    print("\nWith a list of", SOME_LARGE_NUMBER, "values:")

    copy = list(some_list)
    bubblesort(copy)
    copy = list(some_list)
    selectsort(copy)
    copy = list(some_list)
    sorted = quick_sort_with_count(copy)

    print("\nSearching!")
    print(linear_search(sorted, 82))

    print(binary_search(sorted, 82))


main()
