def is_win(game):
    win = False
    # Check rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
        win = True
    # Check columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X' or game[0][1] == 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    return win

def print_board(game):
    """
    Print the game board without colors for terminals that don't support ANSI
    Args:
        game: 3x3 list representing the game board
    """
    board_template = """
         1   2   3  
       ┌───┬───┬───┐
    1  │ {} │ {} │ {} │
       ├───┼───┼───┤
    2  │ {} │ {} │ {} │
       ├───┼───┼───┤
    3  │ {} │ {} │ {} │
       └───┴───┴───┘
    """
    
    # Flatten the game board into a single list
    pieces = [cell for row in game for cell in row]
    
    print(board_template.format(*pieces))

def get_valid_input(game):
    """
    Get valid user input for the cell (i, j), ensuring it's within bounds and not already marked.
    """
    while True:
        try:
            i, j = map(int, input("Enter row and column (1-3) separated by space: ").split())
            i -= 1  # Convert to 0-based index
            j -= 1  # Convert to 0-based index
            if i < 0 or i >= 3 or j < 0 or j >= 3:
                print("Invalid input! Please enter values between 1 and 3.")
            elif game[i][j] != ' ':
                print("Cell already marked! Please choose another cell.")
            else:
                return i, j
        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space.")
            
def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    
    for n in range(9):
        turn = not turn  # Switch turns
        print_board(game)  # Print the board before each move
        
        if not turn:
            print("Player 1's turn")
        else:
            print("Player 2's turn")
        
        i, j = get_valid_input(game)  # Get valid input
        
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'
        
        if is_win(game):
            print_board(game)  # Show final board state
            print("Win!")
            break  # Terminate the game
        
        if n == 8:  # All cells have been filled
            print_board(game)  # Show final board state
            print("Tie!")

if __name__ == "__main__":
    main()
