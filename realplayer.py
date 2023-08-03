from player import Player


class HumanPlayer(Player):
    def __init__(self, pick):
        super().__init__(pick)

    def get_move(self, game):
        valid_moves = False
        val = None
        while not valid_moves:
            squares = input(self.pick + '\'s turn. Enter your move (0-8: )')
            try:
                val = int(squares)
                if val not in game.available_moves():
                    raise ValueError
                valid_moves = True
            except ValueError:
                print('Invalid Move, try again')
        return val
