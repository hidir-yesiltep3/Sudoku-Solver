# The size of the  board is 9 x 9

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def print_board(board):

    for i in range(9):

        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(9):

            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])

            else:
                print(board[i][j], end=" ")


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row , column

    return None


def is_valid(board, number, position):

    # Check whether row contains the given value
    for i in board[position[0]]:
        if i == number:
            return False

    # Check whether column contains the given value
    for i in range(9):
        if board[i][position[1]] == number:
            return False

    # Check whether the box contains the given value

    current_row = position[0]
    current_col = position[1]

    starting_row = 3 * (current_row // 3)
    starting_col = 3 * (current_col // 3)

    for i in range(starting_row, starting_row + 3):
        for j in range(starting_col, starting_col + 3):
            if board[i][j] == number:
                return False

    return True


def solve(board):
    location = find_empty(board)

    if not location:
        return True

    pos_x = location[0]
    pos_y = location[1]

    for num in range(1, 10):
        if is_valid(board, num, location):
            board[pos_x][pos_y] = num

            if solve(board):
                return True

            board[pos_x][pos_y] = 0
    return False
