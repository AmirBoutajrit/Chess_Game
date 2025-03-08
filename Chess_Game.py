def initialize_board():
    """Initialize the chess board with pieces in their starting positions."""
    return [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]

def print_board(board):
    """Print the current state of the chess board."""
    print("\n  a b c d e f g h")
    print(" +-----------------+")
    for i, row in enumerate(board):
        print(f"{8 - i}|{' '.join(row)}|")
    print(" +-----------------+\n")

def is_valid_move(board, start, end, turn):
    """Check if a move is valid based on chess rules."""
    try:
        start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
        end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')

        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False  # Move is out of bounds

        piece = board[start_row][start_col]
        target = board[end_row][end_col]

        if piece == " ":
            return False  # No piece to move

        # Ensure it's the correct player's turn
        if (turn == "White" and piece.islower()) or (turn == "Black" and piece.isupper()):
            return False  # Moving the wrong color piece

        # Prevent capturing own piece
        if (piece.isupper() and target.isupper()) or (piece.islower() and target.islower()):
            return False

        row_diff, col_diff = abs(end_row - start_row), abs(end_col - start_col)

        # Piece movement rules
        piece_lower = piece.lower()

        if piece_lower == "p":  # Pawn
            direction = -1 if piece.isupper() else 1  # White moves up (-1), Black moves down (+1)
            if start_col == end_col and target == " ":
                if row_diff == 1 or (row_diff == 2 and (start_row == 6 or start_row == 1)):  # First move allows 2 steps
                    return True
            elif col_diff == 1 and row_diff == 1 and target != " ":  # Capturing diagonally
                return True
            return False  # Invalid pawn move

        elif piece_lower == "r":  # Rook
            if row_diff == 0 or col_diff == 0:  # Must move straight
                return True
            return False

        elif piece_lower == "b":  # Bishop
            if row_diff == col_diff:  # Must move diagonally
                return True
            return False

        elif piece_lower == "q":  # Queen
            if row_diff == col_diff or row_diff == 0 or col_diff == 0:  # Bishop + Rook movement
                return True
            return False

        elif piece_lower == "n":  # Knight
            if (row_diff, col_diff) in [(2, 1), (1, 2)]:  # L-shape move
                return True
            return False

        elif piece_lower == "k":  # King
            if row_diff <= 1 and col_diff <= 1:  # Moves one square in any direction
                return True
            return False

        return False  # If no valid move rule applies
    except (IndexError, ValueError):
        return False

def make_move(board, start, end):
    """Move a piece on the board."""
    start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
    end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')

    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = " "

def main():
    board = initialize_board()
    print("Welcome to Chess!")
    print("Moves are entered as e2e4 (no space). Type 'quit' to exit.")
    print_board(board)

    turn = "White"
    while True:
        move = input(f"{turn}'s move: ").strip().lower()
        
        if move == "quit":
            print("Game Over!")
            break
        
        if len(move) != 4:
            print("Invalid input! Use format e2e4 (no space).")
            continue

        start, end = move[:2], move[2:]
        if not is_valid_move(board, start, end, turn):
            print("Invalid move! Try again.")
            continue

        make_move(board, start, end)
        print_board(board)
        turn = "Black" if turn == "White" else "White"

if __name__ == "__main__":
    main()
