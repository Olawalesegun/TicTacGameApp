from realplayer import RealPlayer
from automatedplayer import AutomatedPlayer
from gamecontrol import TicTacToe, play

if __name__ == '__main__':
    player1 = RealPlayer('x')
    player2 = AutomatedPlayer('o')
    t = TicTacToe()
    play(t, player1, player2, print_game=True)
