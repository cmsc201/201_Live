import random


def bubblesort(the_list):
    """
    Sorts a list
    :param the_list: a list of values
    :return: a sorted version of the_list
    """
    compare_count = 0
    # add sort
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
    # add sort
    count_list.append(compares)
    return the_list


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
    # add sort
    print(compares, "comparisons done for select sort.")
    return the_list


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
    print("With a list of", SOME_LARGE_NUMBER, "values:")
    copy = list(some_list)
    bubblesort(copy)
    copy = list(some_list)
    selectsort(copy)
    copy = list(some_list)
    quick_sort_with_count(copy)


main()
