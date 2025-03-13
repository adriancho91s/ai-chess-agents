import chess


class Heuristics:
    @staticmethod
    def evaluate_material(board, color):
        """
        Evaluates the material balance on the board.

        Args:
            board (chess.Board): The current state of the chess board.
            color (bool): The color of the player to evaluate for.

        Returns:
            int: The material score.
        """
        piece_values = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3,
                        chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}
        return sum(piece_values[p.piece_type] * (1 if p.color == color else -1)
                   for square in chess.SQUARES if (p := board.piece_at(square)))

    @staticmethod
    def evaluate_mobility(board, color):
        """
        Evaluates the mobility of the pieces on the board.

        Args:
            board (chess.Board): The current state of the chess board.
            color (bool): The color of the player to evaluate for.

        Returns:
            int: The mobility score.
        """
        return len(list(board.legal_moves)) * (1 if board.turn == color else -1)

    @staticmethod
    def evaluate_center_control(board, color):
        """
        Evaluates the control of the center squares on the board.

        Args:
            board (chess.Board): The current state of the chess board.
            color (bool): The color of the player to evaluate for.

        Returns:
            int: The center control score.
        """
        center_squares = [chess.D4, chess.D5, chess.E4, chess.E5]
        return sum((1 if board.piece_at(square) and board.piece_at(square).color == color else -1)
                   for square in center_squares)

    @staticmethod
    def evaluate_king_safety(board, color):
        """
        Evaluates the safety of the king.

        Args:
            board (chess.Board): The current state of the chess board.
            color (bool): The color of the player to evaluate for.

        Returns:
            int: The king safety score.
        """
        king_square = board.king(color)
        if king_square:
            return -sum(1 for move in board.attacks(king_square)
                        if board.piece_at(move) and board.piece_at(move).color != color)
        return 0

    @staticmethod
    def evaluate_relative_difference(board, color):
        """
        Evaluates the relative material difference between the two players.

        Args:
            board (chess.Board): The current state of the chess board.
            color (bool): The color of the player to evaluate for.

        Returns:
            int: The relative material difference score.
        """
        player_score = Heuristics.evaluate_material(board, color)
        opponent_score = Heuristics.evaluate_material(board, not color)
        return player_score - opponent_score