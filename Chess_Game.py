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
    print("  a b c d e f g h")
    print(" +-----------------+")
    for i, row in enumerate(board):
        print(f"{8 - i}|{' '.join(row)}|")
    print(" +-----------------+")

def is_valid_move(board, start, end):
    """Check if a move is valid (basic implementation)."""
    # Convert algebraic notation to board indices
    try:
        start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
        end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')

        if 0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8:
            piece = board[start_row][start_col]
            if piece != " " and (piece.isupper() or piece.islower()):
                return True  # Simplified; doesn't enforce specific rules per piece.
        return False
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
    print("Moves are entered in algebraic notation, e.g., 'e2 e4'.")
    print_board(board)

    turn = "White"
    while True:
        print(f"{turn}'s turn")
        move = input("Enter your move (e.g., 'e2 e4'): ").strip()
        if len(move) != 5 or move[2] != " ":
            print("Invalid input format. Use the format 'e2 e4'.")
            continue

        start, end = move.split()
        if not is_valid_move(board, start, end):
            print("Invalid move. Try again.")
            continue

        make_move(board, start, end)
        print_board(board)

        # Switch turns
        turn = "Black" if turn == "White" else "White"

if __name__ == "__main__":
    main()