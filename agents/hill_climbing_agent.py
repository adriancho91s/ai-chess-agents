import chess
from .base_agent import ChessAgent


class HillClimbingAgent(ChessAgent):
    def __init__(self, color, heuristic, openings=None):
        super().__init__(color, openings)
        self.heuristic = heuristic

    def select_move(self, board):
        opening_move = self.get_opening_move(board)
        if opening_move:
            return opening_move
        best_move, best_score = None, -float("inf")
        for move in board.legal_moves:
            board.push(move)
            score = self.heuristic(board, self.color)
            board.pop()
            if score > best_score:
                best_score, best_move = score, move
        return best_move
