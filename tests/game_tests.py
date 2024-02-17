import unittest
from src.game import GameState


class GameTests(unittest.TestCase):
    def test_initial_state(self):
        """
        Tests that the initial state is set correctly
        """
        # Arrange
        game_state = GameState((7, 6))

        # Act
        # No action needed for the initial state

        # Assert
        self.assertEqual(game_state.current_player, 1)

    def test_make_a_move(self):
        """
        Tests that a piece is placed in the board
        """

        # Arrange
        game_state = GameState((7, 6))

        # Act
        game_state.make_move(0)

        # Assert
        self.assertEqual(game_state.board[5][0], 1)

    def test_make_move_on_full_column(self):
        """
        Tests that a piece is not placed in a full column
        """

        # Arrange
        game_state = GameState((7, 6))

        # Act
        for _ in range(6):
            game_state.make_move(0)

        # Assert
        with self.assertRaises(ValueError):
            game_state.make_move(0)

    def test_switch_player(self):
        """
        Tests that the player is switched
        """

        # Arrange
        game_state = GameState((7, 6))

        # Act
        game_state.switch_player()

        # Assert
        self.assertEqual(game_state.current_player, 2)

    def test_horizontal_win(self):
        """
        Tests that a horizontal win is detected
        """

        # Arrange
        game_state = GameState((7, 6))

        # Act
        for i in range(4):
            game_state.make_move(i)
        game_state.make_move(4)

        # Assert
        self.assertTrue(game_state.is_winning_move(3))

    def test_vertical_win(self):
        """
        Tests that a vertical win is detected
        """

        # Arrange
        game_state = GameState((7, 6))

        # Act
        for _ in range(4):
            game_state.make_move(0)
        game_state.make_move(0)

        # Assert
        self.assertTrue(game_state.is_winning_move(0))

    def test_diagonal_win(self):
        """
        Tests that a diagonal win is detected
        """

        # Arrange
        game_state = GameState((7, 6))

        # Act
        for i in range(3):
            for _ in range(i):
                game_state.make_move(i + 1)
            game_state.make_move(i + 1)

        game_state.switch_player()
        for i in range(4):
            game_state.make_move(i)

        # Assert
        self.assertTrue(game_state.is_winning_move(3))

    def test_no_winning_move(self):
        """
        Tests that a non-winning move is detected
        """

        # Arrange
        game_state = GameState((7, 6))

        # Act
        game_state.make_move(0)

        # Assert
        self.assertFalse(game_state.is_winning_move(0))

    def test_full_board(self):
        """
        Tests that a full board is detected
        """

        # Arrange
        game_state = GameState((7, 6))

        # Act
        for i in range(7):
            for _ in range(6):
                game_state.make_move(i)

        # Assert
        self.assertTrue(game_state.is_full())
