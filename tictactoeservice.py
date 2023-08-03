from player import Player
from realplayer import HumanPlayer
from automatedplayer import AutomatedPlayer
from gamecontrol import TicTacToe, play

if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = AutomatedPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
