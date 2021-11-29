import unittest
import gamelogic.game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.new_game = gamelogic.game.Game(4, "Test")
        self.new_game.map = [[0, 2, 2, 0], [4, 0, 2, 16], [4, 128, 16, 16], [2, 0, 2, 0]]
    
    def test_empty_tiles_regocnized(self):
        blanks = [(0, 0), (1, 1), (3, 1), (0, 3), (3, 3)]
        new_list = self.new_game.empty_tiles()

        self.assertListEqual(new_list, blanks)
    
    def test_new_tile_returns_true_when_empty_tiles_exist(self):
        new_tile = self.new_game.new_tile()
        self.assertTrue(new_tile)
    
    def test_new_tile_returns_false_when_empty_tiles_do_no_exist(self):
        self.new_game.map = [[2, 2, 2, 2], [4, 2, 2, 16], [4, 128, 16, 16], [2, 2, 2, 2]]
        new_tile = self.new_game.new_tile()
        self.assertFalse(new_tile)
    
    def test_swap_tiles_returns_false_if_from_is_zero(self):
        swap = self.new_game.swap_tiles(0, 0, 1, 1)
        self.assertFalse(swap)

    def test_swap_tiles_returns_true_if_to_is_zero(self):
        swap = self.new_game.swap_tiles(0, 1, 0, 0)
        self.assertTrue(swap)
    
    def test_swap_tiles_returns_true_if_from_and_to_are_equal(self):
        swap = self.new_game.swap_tiles(1, 0, 2, 0)
        self.assertTrue(swap)

    def test_swap_tiles_returns_false_if_from_and_to_are_not_equal(self):
        swap = self.new_game.swap_tiles(0, 2, 1, 2)
        self.assertFalse(swap)

    def test_move_left_works(self):
        self.new_game.move_left()
        moved = [[4, 0, 0, 0], [4, 2, 16, 0], [4, 128, 32, 0], [4, 0, 0, 0]]
        self.assertListEqual(self.new_game.map, moved)
    
    def test_move_left_legal_move(self):
        legal = self.new_game.move_left()
        self.assertTrue(legal)
    
    def test_move_left_legal_move_move_count_works(self):
        self.new_game.move_left()    
        self.assertEqual(self.new_game.moves, 1)
    
    def test_move_left_illegal_move(self):
        self.new_game.map = [[2, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0]]
        legal = self.new_game.move_left()
        self.assertFalse(legal)
    
    def test_move_left_illegal_move_move_count_works(self):
        self.new_game.map = [[2, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0]]
        self.new_game.move_left()    
        self.assertEqual(self.new_game.moves, 0)

    def test_move_right_works(self):
        self.new_game.move_right()
        moved = [[0, 0, 0, 4], [0, 4, 2, 16], [0, 4, 128, 32], [0, 0, 0, 4]]
        self.assertListEqual(self.new_game.map, moved)

    def test_move_right_legal_move(self):
        legal = self.new_game.move_right()
        self.assertTrue(legal)
    
    def test_move_right_legal_move_move_count_works(self):
        self.new_game.move_right()    
        self.assertEqual(self.new_game.moves, 1)
    
    def test_move_right_illegal_move(self):
        self.new_game.map = [[0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 0]]
        legal = self.new_game.move_right()
        self.assertFalse(legal)
    
    def test_move_right_illegal_move_move_count_works(self):
        self.new_game.map = [[0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 0]]
        self.new_game.move_right()    
        self.assertEqual(self.new_game.moves, 0)

    def test_move_up_works(self):
        self.new_game.move_up()
        moved = [[8, 2, 4, 32], [2, 128, 16, 0], [0, 0, 2, 0], [0, 0, 0, 0]]
        self.assertListEqual(self.new_game.map, moved)

    def test_move_up_legal_move(self):
        legal = self.new_game.move_up()
        self.assertTrue(legal)
    
    def test_move_up_legal_move_move_count_works(self):
        self.new_game.move_up()    
        self.assertEqual(self.new_game.moves, 1)
    
    def test_move_up_illegal_move(self):
        self.new_game.map = [[2, 0, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        legal = self.new_game.move_up()
        self.assertFalse(legal)
    
    def test_move_up_illegal_move_move_count_works(self):
        self.new_game.map = [[2, 0, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.new_game.move_up()    
        self.assertEqual(self.new_game.moves, 0)

    def test_move_down_works(self):
        self.new_game.move_down()
        moved = [[0, 0, 0, 0], [0, 0, 4, 0], [8, 2, 16, 0], [2, 128, 2, 32]]
        self.assertListEqual(self.new_game.map, moved)

    def test_move_down_legal_move(self):
        legal = self.new_game.move_down()
        self.assertTrue(legal)
    
    def test_move_down_legal_move_move_count_works(self):
        self.new_game.move_down()    
        self.assertEqual(self.new_game.moves, 1)
    
    def test_move_down_illegal_move(self):
        self.new_game.map = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 2, 0]]
        legal = self.new_game.move_down()
        self.assertFalse(legal)
    
    def test_move_down_illegal_move_move_count_works(self):
        self.new_game.map = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 2, 0]]
        self.new_game.move_down()    
        self.assertEqual(self.new_game.moves, 0)
    
    def test_game_continues_returns_false_when_won(self):
        self.new_game.map = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2048, 2, 2, 0]]
        game_continues = self.new_game.game_continues()
        self.assertFalse(game_continues)

    def test_game_continues_returns_false_when_lost(self):
        self.new_game.map = [[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]
        game_continues = self.new_game.game_continues()
        self.assertFalse(game_continues)

    def test_game_continues_returns_true_when_empty_tiles(self):
        game_continues = self.new_game.game_continues()
        self.assertTrue(game_continues)

    def test_game_continues_returns_true_when_can_move_left_or_right(self):
        self.new_game.map = [[8, 2, 2, 4], [4, 8, 4, 8], [8, 4, 8, 4], [4, 8, 4, 8]]
        game_continues = self.new_game.game_continues()
        self.assertTrue(game_continues)
    
    def test_game_continues_returns_true_when_can_move_up_or_down(self):
        self.new_game.map = [[8, 2, 8, 4], [4, 2, 4, 8], [8, 4, 8, 4], [4, 8, 4, 8]]
        game_continues = self.new_game.game_continues()
        self.assertTrue(game_continues)
