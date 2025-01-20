from typing import List, Tuple

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.PLAYERS = {'X': 'Player 1', 'O': 'Player 2'}
        
    def display_board(self) -> None:
        """Show board"""
        print("\nCurrent Board:")
        print("  1 2 3")
        for i, row in enumerate(self.board, 1):
            print(f"{i} {' '.join(row)}")
        print()

    def is_valid_move(self, row: int, col: int) -> bool:
        """Check if move is valid"""
        return (0 <= row < 3 and 
                0 <= col < 3 and 
                self.board[row][col] == ' ')

    def make_move(self, row: int, col: int, player: str) -> bool:
        """Move"""
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False

    def is_winner(self) -> bool:
        """Check if anyone wins"""
        # Rows and cols
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or
                self.board[0][i] == self.board[1][i] == self.board[2][i] != ' '):
                return True
        
        # Diagonal
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or
            self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '):
            return True
        
        return False

    def is_board_full(self) -> bool:
        """Check if the board is full"""
        return all(cell != ' ' for row in self.board for cell in row)

    def get_move(self) -> Tuple[int, int]:
        """Get player's move"""
        while True:
            try:
                print("Enter row and column (1-3, separated by space): ", end="")
                row, col = map(int, input().split())
                row -= 1  # Transforms into 0-based index
                col -= 1
                
                if self.is_valid_move(row, col):
                    return row, col
                else:
                    print("Invalid move! Cell is either occupied or out of bounds.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter two numbers between 1 and 3.")

def main():
    game = TicTacToe()
    current_player = 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    print("X = Player 1, O = Player 2")
    
    while True:
        game.display_board()
        print(f"{game.PLAYERS[current_player]}'s turn ({current_player})")
        
        row, col = game.get_move()
        game.make_move(row, col, current_player)
        
        if game.is_winner():
            game.display_board()
            print(f"\nCongratulations! {game.PLAYERS[current_player]} wins!")
            break
            
        if game.is_board_full():
            game.display_board()
            print("\nGame Over! It's a tie!")
            break
            
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
