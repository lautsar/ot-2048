import unittest
import game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.new_game = game.Game(4)
        print(self.new_game.map)
        self.new_game.map = [[0, 2, 2, 0], [4, 0, 2, 16], [4, 128, 16, 16], [2, 0, 2, 0]]
        print(self.new_game.map)

    def test_move_left_works(self):
        self.new_game.move_left()
        moved = [[4, 0, 0, 0], [4, 2, 16, 0], [4, 128, 32, 0], [4, 0, 0, 0]]
        self.assertListEqual(self.new_game.map, moved)
