from copy import deepcopy


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


def neturalize_row_col(row, col):
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
    return row, col


class Algorithm:

    def __init__(self, board, completed=None):
        self.length = 0
        self.current_board = deepcopy(board)
        self.initial_board = deepcopy(board)
        self.completed_board = deepcopy(board)
        self.hints = 3

    def find_next_tile(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == -1:
                    return i, j
        return False

    def get_length(self):
        self.length = len(self.initial_board)
        return self.length

    def get_cols(self, board, col):
        lst = []
        for i in range(9):
            lst.append(board[i][col])
        return lst

    def get_rows(self, board, row):
        lst = []
        for i in range(9):
            lst.append(board[row][i])
        return lst

    def get_initial_board(self):
        return self.initial_board

    def get_current_board(self):
        return self.current_board

    def get_tile(self, board, row, col):
        return board[row][col]

    def get_hints(self):
        return self.hints

    def set_hints(self, number=1):
        self.hints -= number

    def solve_one_tile(self, board, row, col):
        if self.hints > 0 and board == self.current_board:
            self.set_hints()
            completed_value = self.completed_board[row][col]
            self.current_board[row][col] = completed_value
            self.initial_board[row][col] = completed_value
        else:
            print("SORRY RAN OUT OF HINTS")
        return self.current_board[row][col]

    def solve_grid(self, board, row, col):
        count = 0
        if self.hints >= 2 and board == self.get_current_board():
            self.set_hints(2)
            completed_grid = self.get_grid(self.get_finished_board(), row, col)
            row, col = neturalize_row_col(row, col)
            print(completed_grid)
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    self.current_board[i][j] = completed_grid[count]
                    self.initial_board[i][j] = completed_grid[count]
                    count += 1
        else:
            print("SORRY RAN OUT OF HINTS")

    def set_tile(self, board, row, col, number):
        if -1 <= number <= 9 and self.initial_board[row][col] == -1:
            board[row][col] = number
        else:
            print("CANNOT SET PREDETERMINED/COMPLETED CORRECT VALUES")
            print("ALSO VALUE PLACEMENTS MUST ABIDE BY TRADITIONAL SODUKU RULES")

    def get_finished_board(self):
        return self.completed_board

    def set_finished_board(self):
        self.completed_board = self.backtrace(self.completed_board)

    def check_wrong(self, board, row, col, number):
        if number in self.get_cols(board, col) or number in self.get_rows(board, row) or number == -1:
            return True
        elif number in self.get_grid(board, row, col):
            return True
        return False

    def get_grid(self, board, row, col):
        lst = []
        row, col = neturalize_row_col(row, col)
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                lst.append(board[i][j])
        return lst

    def backtrace(self, board):
        ''' 1. Pick an empty spot
            2. Try all numbers for that spot
            3. Find a number that works
            4. Move onto the next empty spot, repeat
            5. If wrong, backtrace/recurse your way back
            6. End'''
        if not self.find_next_tile(board):
            return True
        else:
            row, col = self.find_next_tile(board)
        if row is not False and col is not False:
            for i in range(1, 10):
                if not self.check_wrong(board, row, col, i):
                    self.set_tile(board, row, col, i)
                    if self.backtrace(board):
                        return board
                self.set_tile(board, row, col, -1)
        return False


''' The row is just the index nested list of where the element resides
    The column is every ith element in EACH nested list'''
board = [

    [7, 8, -1, 4, -1, -1, 1, 2, -1],
    [6, -1, -1, -1, 7, 5, -1, -1, 9],
    [-1, -1, -1, 6, -1, 1, -1, 7, 8],
    [-1, -1, 7, -1, 4, -1, 2, 6, -1],
    [-1, -1, 1, -1, 5, -1, 9, 3, -1],
    [9, -1, 4, -1, 6, -1, -1, -1, 5],
    [-1, 7, -1, 3, -1, -1, -1, 1, 2],
    [1, 2, -1, -1, -1, 7, 4, -1, -1],
    [-1, 4, 9, 2, -1, 6, -1, -1, 7]

]

a = Algorithm(board)
a.set_finished_board()
pprint(a.get_finished_board())
"""print("\n\n\n\n")
pprint(a.get_current_board())
a.set_tile(a.get_current_board(), 0, 2, 3)
print("\n\n\n\n")
pprint(a.get_finished_board())
print("\n\n\n\n")
pprint(a.get_initial_board())

print(a.get_grid(a.completed_board, 0, 0))
print(a.get_grid(a.current_board, 0, 0))"""
a.solve_grid(a.get_current_board(), 2, 2)
print("\n\n\n\n")
pprint(a.get_current_board())
print(a.get_grid(a.current_board, 2, 2))
print("\n\n\n")
pprint(a.get_current_board())
print("\n\n\n")
pprint(a.get_finished_board())
print("\n\n\n")
a.solve_one_tile(a.get_current_board(), 0, 4)
pprint(a.get_current_board())
print("\n\n\n")
pprint(a.get_finished_board())
print("\n\n\n")
pprint(a.get_initial_board())

a.solve_one_tile(a.get_current_board(), 0, 5)
a.solve_one_tile(a.get_current_board(), 0, 5)
