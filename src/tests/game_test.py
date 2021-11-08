import unittest
import game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.new_game = game.Game(4)
        self.new_game.map = [[0, 2, 2, 0], [4, 0, 2, 16], [4, 128, 16, 16], [2, 0, 2, 0]]
    
    def test_empty_tiles_regocnized(self):
        blanks = [(0, 0), (1, 1), (3, 1), (0, 3), (3, 3)]
        new_list = self.new_game.empty_tiles()

        self.assertListEqual(new_list, blanks)

    def test_move_left_works(self):
        self.new_game.move_left()
        moved = [[4, 0, 0, 0], [4, 2, 16, 0], [4, 128, 32, 0], [4, 0, 0, 0]]
        self.assertListEqual(self.new_game.map, moved)

    def test_move_right_works(self):
        self.new_game.move_right()
        moved = [[0, 0, 0, 4], [0, 4, 2, 16], [0, 4, 128, 32], [0, 0, 0, 4]]
        self.assertListEqual(self.new_game.map, moved)

    def test_move_up_works(self):
        self.new_game.move_up()
        moved = [[8, 2, 4, 32], [2, 128, 16, 0], [0, 0, 2, 0], [0, 0, 0, 0]]
        self.assertListEqual(self.new_game.map, moved)

    def test_move_down_works(self):
        self.new_game.move_down()
        moved = [[0, 0, 0, 0], [0, 0, 4, 0], [8, 2, 16, 0], [2, 128, 2, 32]]
        self.assertListEqual(self.new_game.map, moved)
