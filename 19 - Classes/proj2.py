class ChessBoard:
    def __init__(self, board):
        self.board = board

    def is_valid_move(self, row_start, col_start, row_end, col_end):
        """

        :param row_start:
        :param col_start:
        :param row_end:
        :param col_end:
        :return: true if the move is permitted, false otherwise
        """
        return True