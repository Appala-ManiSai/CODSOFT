import math

# Constants
X = 'X'
O = 'O'
EMPTY = None

def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return 10
            elif board[i][0] == O:
                return -10
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == X:
                return 10
            elif board[0][i] == O:
                return -10
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return 10
        elif board[0][0] == O:
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == X:
            return 10
        elif board[0][2] == O:
            return -10
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not any(None in row for row in board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = X
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = None
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = O
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = None
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = X
                move_val = minimax(board, 0, False)
                board[i][j] = None
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def print_board(board):
    for row in board:
        print(row)

def is_board_full(board):
    return not any(None in row for row in board)

def main():
    board = [[EMPTY] * 3 for _ in range(3)]

    print("Let's play Tic-Tac-Toe!")

    while True:
        print_board(board)
        row = int(input("Enter the row (1, 2, or 3): ")) - 1
        col = int(input("Enter the column (1, 2, or 3): ")) - 1

        if board[row][col] is not None:
            print("Invalid move. Try again.")
            continue

        board[row][col] = O

        if evaluate(board) == -10:
            print_board(board)
            print("You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = X

        if evaluate(board) == 10:
            print_board(board)
            print("AI wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
