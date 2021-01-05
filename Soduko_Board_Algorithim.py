import random

MY_INITIAL_BOARD = [

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
    def find_next_tile(self):
        for i in range(9):
            for j in range(9):
                if self.current_board[i][j] == -1:
                    return i, j
        return False


    def get_length(self):
        self.length = len(MY_INITIAL_BOARD)
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
        if -1 <= number <= 9 and MY_INITIAL_BOARD[row][col] == -1:
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

    def backtrace(self):
        ''' 1. Pick an empty spot
            2. Try all numbers for that spot
            3. Find a number that works
            4. Move onto the next empty spot, repeat
            5. If wrong, backtrace/recurse your way back
            6. End'''
        #THE PROBLEM IS THAT IT IS NOT GOING BACK
        #maybe put another if statement
        if not self.find_next_tile():
            return True
        else:
            row, col = self.find_next_tile()
        if row is not False and col is not False:
            for i in range(1,10):
                if not self.check_wrong(row, col, i) :
                    self.set_tile(row,col,i)
                    if self.backtrace():
                        return True

                    self.set_tile(row,col,-1)
        return False
                #if i == 9 and row is not False and col is not False:
                    # problem is that it's not going backwards.
                    # iterates over same thing when you run out of a number b/c doing set tile to -1
                    # e.g, row 0, column 5, no valid numbers, so need to move backwards
                    # but problem is it won't move backwards
                    #self.set_tile(row,col,-1)
                #    return self.backtrace()




        # going to need to use recursion

''' The row is just the index nested list of where the element resides
    The column is every ith element in EACH nested list'''

a = Algorithm()
pprint(a.get_current_board())
a.backtrace()
print("\n\n\n")
pprint(a.get_current_board())


