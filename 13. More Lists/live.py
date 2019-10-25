


def create_new_2d_list(height, width):
    # sticky version... gross
    # row = []
    # mat = []
    #
    # for i in range(width):
    #     row.append(0)
    #
    # for i in range(height):
    #     mat.append(row)
    # return mat

    mat = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        mat.append(row)
    return mat

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 1, 2, 3],
              [4, 5, 6, 7]]
    # how do I get at the 9?
    # print(matrix[2][0])
    # how do I loop through the third row?
    # for element in matrix[2]:
    #     print(element)
    # how do I loop through the second column?
    # for row in matrix:
    #     print(row[1])

    mat = create_new_2d_list(8,2)
    mat[0][0] = 1
    mat[4][1] = 5
    print(mat)
    # should print
    # [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

    matthew = []
    for row in mat:
        new_row = []
        for element in row:
            new_row.append(element)
        matthew.append(new_row)
    mat[1][1] = 9
    print("matthew", matthew)
    print("mat", mat)
    matthew = mat
    mat[2][0] = "peanut butter"
    print("matthew", matthew)
    print("mat", mat)

