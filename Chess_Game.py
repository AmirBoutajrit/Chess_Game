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

def is_valid_move(board, start, end):
    """Check if a move is valid (Basic validation, real rules should be implemented)."""
    try:
        start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
        end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')
        
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False  # Move is out of bounds
        
        piece = board[start_row][start_col]
        if piece == " ":
            return False  # No piece to move
        
        return True  # Basic move validation (Piece-specific rules can be added)
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
        if not is_valid_move(board, start, end):
            print("Invalid move! Try again.")
            continue

        make_move(board, start, end)
        print_board(board)
        turn = "Black" if turn == "White" else "White"

if __name__ == "__main__":
    main()
