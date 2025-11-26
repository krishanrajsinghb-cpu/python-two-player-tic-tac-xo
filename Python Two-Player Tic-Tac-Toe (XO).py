# xo.py — simple Tic-Tac-Toe (X/O) for two players

def print_board(b):
    """Print the board. b is list of 9 items ('' or 'X' or 'O')."""
    def cell(i):
        return b[i] if b[i] != '' else str(i+1)
    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()

def check_winner(b):
    """Return 'X' or 'O' if there's a winner, 'D' for draw, or None for ongoing."""
    wins = [
        (0,1,2),(3,4,5),(6,7,8),  # rows
        (0,3,6),(1,4,7),(2,5,8),  # cols
        (0,4,8),(2,4,6)           # diags
    ]
    for a,b_i,c in wins:
        if b[a] != '' and b[a] == b[b_i] == b[c]:
            return b[a]
    if all(cell != '' for cell in b):
        return 'D'  # draw
    return None

def get_move(player, board):
    """Ask player for a move (1-9). Validate."""
    while True:
        try:
            move = input(f"Player {player} — enter position (1-9): ").strip()
            if move.lower() in ('q','quit','exit'):
                print("Exiting game.")
                raise SystemExit
            pos = int(move) - 1
            if pos < 0 or pos > 8:
                print("Choose a number from 1 to 9.")
                continue
            if board[pos] != '':
                print("That cell is already taken. Pick another.")
                continue
            return pos
        except ValueError:
            print("Please enter a number between 1 and 9, or 'q' to quit.")

def play_game():
    board = [''] * 9
    current = 'X'
    print("Welcome to Tic-Tac-Toe! X goes first. Type 'q' to quit anytime.")
    print_board(board)

    while True:
        pos = get_move(current, board)
        board[pos] = current
        print_board(board)
        result = check_winner(board)
        if result == 'X' or result == 'O':
            print(f"Player {result} wins! 🎉")
            break
        elif result == 'D':
            print("It's a draw.")
            break
        current = 'O' if current == 'X' else 'X'

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ('y','yes'):
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
