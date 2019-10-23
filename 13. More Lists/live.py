
def create_new_2d_list(height, width):
    output_list = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        output_list.append(row)
    return output_list


def my_append(matrix):
    matrix.append("what?")


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 1, 2, 3],
              [4, 5, 6, 7],
              [1, 2, 3, 4]]

    my_append(matrix)
    print(matrix)
    # # how do I get at the 9?
    # print(matrix[2][0])
    # # how do I loop through the third row?
    # print("Print the third row")
    # for thing in matrix[2]:
    #     print(thing)
    # # how do I loop through the second column?
    # print("Print second column")
    # for row in matrix:
    #     print(row[1])
    #
    # chess_board = create_new_2d_list(8, 8)
    # print(chess_board)

    # matrix_copy = matrix
    # matrix_copy = []
    # for row in matrix:
    #     new_row = []
    #     for col in row:
    #         new_row.append(col)
    #     matrix_copy.append(new_row)
    # matrix.append([5, 6, 7])
    # print(matrix_copy)

