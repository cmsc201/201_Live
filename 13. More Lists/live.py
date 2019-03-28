matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 1, 2, 3],
          [4, 5, 6, 7],
          [8, 9, 1, 2]]


def create_new_2d_list(height, width):
    row_index = 0
    two_dee_list = []
    index = 0

    while row_index < height:
        col_index = 0
        row = []
        two_dee_list.append(row)
        while col_index < width:
            row.append(index)
            index += 1
            col_index += 1
        row_index += 1

    return two_dee_list

def make_square_list(dimension):
    row_index = 0
    two_dee_list = []
    index = 0

    while row_index < dimension:
        col_index = 0
        row = []
        two_dee_list.append(row)
        while col_index < dimension:
            row.append(index)
            index += 1
            col_index += 1
        row_index += 1

    return two_dee_list

def main():
    # how do I get at the 9?
    print("Should be a nine:", matrix[2][0])
    # how do I loop through the third row?
    index = 0
    while index < 4:
        print(matrix[2][index])
        index += 1

    # how do I loop through the second column?
    index = 0
    while index < 4:
        print(matrix[index][2])
        index += 1

    # write a loop to make a 100x100 list


    print(make_square_list(100))
    print(make_square_list(10))
    print(make_square_list(1))



main()
