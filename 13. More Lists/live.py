MATRIX = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 1, 2, 3],
          [4, 5, 6, 7],
          [2,332, 2, 9]]


def create_new_2d_list(height, width):
    """
    Creates a 2d list of 0s with height rows and width columns
    :param height:
    :param width:
    :return: the 2d list
    """
    output = []
    row_index = 0
    while row_index < height:
        col_index = 0
        row = []
        while col_index < width:
            row.append(0)
            col_index += 1
        row_index += 1
        output.append(row)

    return output


def main():
    # how do I get at the 9?
    # print(MATRIX[2][0])
    # how do I loop through the third row?
    index = 0
    while index < len(MATRIX[2]):
        print(MATRIX[2][index])
        index += 1
    print("NEXT:")
    # how do I loop through the second column?
    index = 0
    while index < len(MATRIX):
        print(MATRIX[index][1])
        index += 1

    for item in create_new_2d_list(10, 10):
        print(item)


main()
