def is_win(game):
    # Check rows and columns for a win
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != ' ':
            return True
        if game[0][i] == game[1][i] == game[2][i] != ' ':
            return True
    
    # Check diagonals for a win
    if game[0][0] == game[1][1] == game[2][2] != ' ':
        return True
    if game[0][2] == game[1][1] == game[2][0] != ' ':
        return True
    
    return False

def print_board(game):
    for row in game:
        print(" ".join(row))

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    
    for n in range(9):
        print_board(game)  # Print the board before each move
        
        if not turn:
            print("Player 1's turn: ", end="")
        else:
            print("Player 2's turn: ", end="")
        
        while True:
            try:
                i, j = map(int, input("Which cell to mark? i:[1..3], j:[1..3]: ").split())
                i -= 1
                j -= 1
                if 0 <= i < 3 and 0 <= j < 3 and game[i][j] == ' ':
                    break  # Valid move
                else:
                    print("Invalid move, try again.")
            except (ValueError, IndexError):
                print("Invalid input, please enter two integers between 1 and 3.")
        
        # Update the board
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'
        
        if is_win(game):
            print_board(game)  # Show final board state
            print(f"Player {'1' if not turn else '2'} wins!")
            break  # Terminate the game
        
        if n == 8:  # All cells have been filled
            print_board(game)  # Show final board state
            print("Tie!")
        
        turn = not turn  # Switch turns

if __name__ == "__main__":
    main()
