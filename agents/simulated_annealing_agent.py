import random
import math
import chess
from .hill_climbing_agent import HillClimbingAgent

class SimulatedAnnealingAgent(HillClimbingAgent):
    def select_move(self, board):
        opening_move = self.get_opening_move(board)
        if opening_move:
            return opening_move
        moves = list(board.legal_moves)
        current_move = random.choice(moves)
        current_score = self.heuristic(board, self.color)
        T, alpha = 1.0, 0.99

        for _ in range(10):
            new_move = random.choice(moves)
            board.push(new_move)
            new_score = self.heuristic(board, self.color)
            board.pop()

            if new_score > current_score or random.uniform(0, 1) < math.exp((new_score - current_score) / T):
                current_move, current_score = new_move, new_score

            T *= alpha

        return current_move
