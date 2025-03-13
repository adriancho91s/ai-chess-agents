import chess
from .base_agent import ChessAgent

class MinimaxAgent(ChessAgent):
    def __init__(self, color, depth=3, heuristic=None, openings=None):
        super().__init__(color, openings)
        self.depth = depth
        self.heuristic = heuristic if heuristic else None  # Se espera una función heurística

    def minimax(self, board, depth, maximizing):
        if depth == 0 or board.is_game_over():
            return self.heuristic(board, self.color)

        if maximizing:
            max_eval = -float("inf")
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, False)
                board.pop()
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, True)
                board.pop()
                min_eval = min(min_eval, eval)
            return min_eval

    def select_move(self, board):
        opening_move = self.get_opening_move(board)
        if opening_move:
            return opening_move
        best_move = None
        best_value = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            move_value = self.minimax(board, self.depth - 1, False)
            board.pop()
            if move_value > best_value:
                best_value = move_value
                best_move = move
        return best_move
