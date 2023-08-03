import random
from player import Player


class AutomatedPlayer(Player):
    def __init__(self, playerpick):
        super().__init__(playerpick)

    def get_move(self, game):
        squares = random.choice(game.available_moves())
        return squares
