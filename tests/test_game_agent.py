"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        # self.player1 = "Player1"
        # self.player2 = "Player2"
        self.player1 = game_agent.AlphaBetaPlayer()
        self.player2 = sample_players.RandomPlayer()
        self.game = isolation.Board(self.player1, self.player2)

    def test_example(self):
        # TODO: All methods must start with "test_"

        #Player 1 is active to start so he plays this move

        minmaxplayer=game_agent.AlphaBetaPlayer()
        RandomPlayer=sample_players.RandomPlayer()

        self.game.apply_move((2, 3))
        self.game.apply_move((0, 5))

        assert(self.player1 == self.game.active_player)

        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(self.game.to_string())



        # self.fail("Hello, World!")


if __name__ == '__main__':
    unittest.main()
