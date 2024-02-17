class GameState:
    """
    Represents the state of the game
    """

    def __init__(self, dimensions: tuple[int], first_player=1) -> None:
        """
        Initializes the game state
        """
        self.columns, self.rows = dimensions
        self.board = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.heights = [0 for _ in range(self.columns)]
        self.current_player = first_player

    def make_move(self, column: int) -> None:
        """
        Makes a move in the game
        """

        # Check if the column is full
        if self.heights[column] == self.rows:
            raise ValueError("Column is full")

        # Place the piece in the column
        self.heights[column] += 1
        row = self.heights[column]
        self.board[self.rows - row][column] = self.current_player

    def switch_player(self) -> None:
        """
        Switches the current player
        """
        self.current_player = 3 - self.current_player

    def is_winning_move(self, column: int) -> bool:
        """
        Checks if the move is a winning move
        """

        # Get the row where the piece is placed
        row = self.columns - (self.heights[column] + 1)

        # Check for an horizontal win
        streak = 0
        start = max(0, column - 3)
        end = min(self.columns - 1, column + 3)
        for c in range(start, end + 1):
            if self.board[row][c] == self.current_player:
                streak += 1
                if streak == 4:
                    return True
            else:
                streak = 0

        # Check for a vertical win
        streak = 0
        start = max(0, row - 3)
        end = min(self.rows - 1, row + 3)
        for r in range(start, end + 1):
            if self.board[r][column] == self.current_player:
                streak += 1
                if streak == 4:
                    return True
            else:
                streak = 0

        # Check for a diagonal win
        streak = 0
        for i in range(-3, 3 + 1):
            r, c = row + i, column + i
            # Check the bounds
            if r < 0 or r >= self.rows or c < 0 or c >= self.columns:
                continue

            if self.board[r][c] == self.current_player:
                streak += 1
                if streak == 4:
                    return True
            else:
                streak = 0

        # Check for a diagonal win (other direction)
        streak = 0
        for i in range(-3, 3 + 1):
            r, c = row - i, column + i
            # Check the bounds
            if r < 0 or r >= self.rows or c < 0 or c >= self.columns:
                continue

            if self.board[r][c] == self.current_player:
                streak += 1
                if streak == 4:
                    return True
            else:
                streak = 0

        # No winning move
        return False

    def is_full(self) -> bool:
        """
        Checks if the board is full
        """
        return all(height == self.rows for height in self.heights)

    def __str__(self) -> str:
        """
        Returns a string representation of the game state
        """

        # Create column numbers
        column_numbers = "|"
        for i in range(self.columns):
            column_numbers += f" {i} |"

        # Create the top line
        top_line = "+"
        for _ in range(self.columns):
            top_line += "---+"

        # Create the board
        board = ""
        for row in self.board:
            board += "|"
            for cell in row:
                if cell == 0:
                    board += "   |"
                elif cell == 1:
                    board += " X |"
                else:
                    board += " O |"
            board += "\n" + top_line + "\n"

        return "\n".join([top_line, column_numbers, top_line, board])


if __name__ == "__main__":
    game = GameState((7, 6))

    print(game)
    while not game.is_full():
        column = int(input(f"Player {game.current_player}, make your move: "))
        game.make_move(column)
        if game.is_winning_move(column):
            print(game)
            print(f"Player {game.current_player} wins!")
            break
        print(game)
        game.switch_player()
