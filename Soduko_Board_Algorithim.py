import random

MY_COMPLETED_BOARD = [

    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]

]

MY_INITIAL_BOARD = [

    [-1, 8, -1, 4, -1, 0, 1, 2, 0],
    [6, 0, 0, 0, -1, 5, -1, 0, 9],
    [0, -1, 0, -1, 0, 1, 0, 7, -1],
    [0, -1, 7, -1, 4, -1, -1, -1, -1],
    [0, -1, 1, -1, 5, 0, 9, 3, -1],
    [-1, 0, -1, -1, 6, -1, -1, -1, 5],
    [0, -1, 0, 3, -1, 0, 0, 1, 2],
    [1, 2, 0, -1, -1, 7, -1, -1, 0],
    [0, 4, 9, 2, -1, -1, 0, -1, 7]

]


def pprint(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


class Algorithm:

    def __init__(self):
        self.length = 0
        self.current_board = [

            [-1, 8, -1, 4, -1, 0, 1, 2, 0],
            [6, 0, 0, 0, -1, 5, -1, 0, 9],
            [0, -1, 0, -1, 0, 1, 0, 7, -1],
            [0, -1, 7, -1, 4, -1, -1, -1, -1],
            [0, -1, 1, -1, 5, 0, 9, 3, -1],
            [-1, 0, -1, -1, 6, -1, -1, -1, 5],
            [0, -1, 0, 3, -1, 0, 0, 1, 2],
            [1, 2, 0, -1, -1, 7, -1, -1, 0],
            [0, 4, 9, 2, -1, -1, 0, -1, 7]

        ]

    def get_length(self):
        self.length = len(MY_COMPLETED_BOARD)
        return self.length

    def get_cols(self, col):
        lst = []
        for i in range(9):
            lst.append(self.current_board[i][col])
        return lst

    def get_rows(self, row):
        lst = []
        for i in range(9):
            lst.append(self.current_board[row][i])
        return lst

    def get_current_board(self):
        return self.current_board

    def get_tile(self, row, col):
        return self.current_board[row][col]

    def set_tile(self, row, col, number):
        if 0 <= number <= 9 and MY_INITIAL_BOARD[row][col] == -1 and not self.check_wrong(row, col, number):
            self.current_board[row][col] = number

    def check_wrong(self, row, col, number):
        if number in self.get_cols(col) or number in self.get_rows(row) or number == -1:
            return True
        elif number in self.get_grid(row, col):
            return True
        return False

    def get_grid(self, row, col):
        lst = []
        if row % 3 != 0:
            if (row - 1) % 3 == 0:
                row -= 1
            elif (row - 2) % 3 == 0:
                row -= 2
        if col % 3 != 0:
            if (col - 1) % 3 == 0:
                col -= 1
            elif (col - 2) % 3 == 0:
                col -= 2
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                lst.append(self.current_board[i][j])
        return lst


''' The row is just the index nested list of where the element resides
    The column is every ith element in EACH nested list'''

a = Algorithm()
pprint(a.get_current_board())
print("\n\n")
a.set_tile(8, 7, 5)
pprint(a.get_current_board())
a.set_tile(8, 7, -1)
print(a.check_wrong(8, 4, 3))
a.set_tile(8, 4, 3)
(pprint(a.get_current_board()))
print("\n")
print(a.get_grid(8, 8))
