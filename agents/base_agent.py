import chess


class ChessAgent:
    def __init__(self, color, openings=None):
        self.color = color
        self.openings = openings if openings else []

    def select_move(self, board):
        raise NotImplementedError

    def get_opening_move(self, board):
        current_moves = [move.uci() for move in board.move_stack]
        for opening in self.openings:
            if len(opening) > len(current_moves) and opening[:len(current_moves)] == current_moves:
                return chess.Move.from_uci(opening[len(current_moves)])
        return None
