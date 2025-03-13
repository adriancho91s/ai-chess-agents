import chess
from .minimax_agent import MinimaxAgent


class AlphaBetaAgent(MinimaxAgent):
    def alphabeta(self, board, depth, alpha, beta, maximizing):
        if depth == 0 or board.is_game_over():
            return self.heuristic(board, self.color)

        if maximizing:
            best_value = -float("inf")
            for move in board.legal_moves:
                board.push(move)
                best_value = max(best_value, self.alphabeta(board, depth - 1, alpha, beta, False))
                board.pop()
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            return best_value
        else:
            best_value = float("inf")
            for move in board.legal_moves:
                board.push(move)
                best_value = min(best_value, self.alphabeta(board, depth - 1, alpha, beta, True))
                board.pop()
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_value

    def select_move(self, board):
        opening_move = self.get_opening_move(board)
        if opening_move:
            return opening_move
        best_move = None
        best_score = -float("inf")
        alpha, beta = -float("inf"), float("inf")
        for move in board.legal_moves:
            board.push(move)
            score = self.alphabeta(board, self.depth - 1, alpha, beta, False)
            board.pop()
            if score > best_score:
                best_score, best_move = score, move
            alpha = max(alpha, best_score)
        return best_move
