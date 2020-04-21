

from proj2 import ChessBoard

def middle(some_list):
    """
    Given a list I will return the middle item, if there is no exact middle,
    I will return the first of the two middle items
    :param some_list: a list of items
    :return: the item in the middle position, None if list is empty
    """
    if not some_list:
        return None
    return some_list[(len(some_list) - 1) // 2]


if __name__ == '__main__':

    cats = ["Jules", "Tybalt", "Scooter"]

    if middle(cats) == "Tybalt":
        print("Pass! Works on odd sized list")
    else:
        print("Fail! Works on odd sized list")

    numbers = [5, 2, 3, 4]
    if middle(numbers) == 2:
        print("Pass! Even sized list")
    else:
        print("Fail! Even sized list")

    empty = []
    if middle(empty) == None:
        print("Pass! Empty list")
    else:
        print("Fail! Empty list")



def test_is_valid_move():

    board = [
        ["r", "b", "q", "b", "r"],
        ["p", "p", "p", "p", "p"],
        ["", "", "", "", ""],
        ["p", "p", "p", "p", "p"],
        ["r", "b", "q", "b", "r"],
    ]
    chess_board = ChessBoard(board)

    if not chess_board.is_valid_move(0, 1, 1, 1):
        print("Passed!  Bishops can move only diagonally")
    else:
        print("Failed!  Bishops can move only diagonally")

    if chess_board.is_valid_move(1, 1, 2, 1):
        print("Passed!  Pawns move vertically into empty spaces")
    else:
        print("Failed! Pawns move vertically into empty spaces")

if __name__ == '__main__':
    test_is_valid_move()