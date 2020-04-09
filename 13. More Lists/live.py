


def create_new_2d_list(height, width):
    pass


if __name__ == '__main__':

    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 1, 2, 3],
              [4, 5, 6, 7]]
    # how do I get at the 9?

    # print(matrix[2][0])
    # # how do I loop through the third row?
    # for item in matrix[2]:
    #     print(item)
    # how do I loop through the second column?
    # for row in matrix:
    #     print(row[1])

    for row in matrix:
        for item in row:
            print(item)
    twodee_list = []

    chess_board = ["rkbqXbkr", "pppppppp", "00000000"]
