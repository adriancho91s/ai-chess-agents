import random
import chess
from .base_agent import ChessAgent

class RandomAgent(ChessAgent):
    def select_move(self, board):
        return random.choice(list(board.legal_moves))
