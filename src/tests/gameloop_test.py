import unittest
import pygame

import gameboard.tiles
import gameboard.gameloop
import gameboard.board
import gamelogic.game

class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key

class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events

class StubRenderer:
    def render(self):
        pass

    def close_window(self):
        pass

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self._game = gamelogic.game.Game(3, "")
        self._game.map = [[0, 4, 0],
               [16, 0, 0],
               [0, 2, 0]]
        self._board = gameboard.board.Board(self._game)

    def test_can_move_left(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_LEFT)]

        game_loop = gameboard.gameloop.GameLoop(
            self._game,
            StubRenderer(),
            StubEventQueue(events)
        )

        self.assertTrue(game_loop.handle_events())
        self.assertEqual(self._game.map[0][0], 4)
    
    def test_can_move_right(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_RIGHT)]

        game_loop = gameboard.gameloop.GameLoop(
            self._game,
            StubRenderer(),
            StubEventQueue(events)
        )

        self.assertTrue(game_loop.handle_events())
        self.assertEqual(self._game.map[0][2], 4)
    
    def test_can_move_up(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_UP)]

        game_loop = gameboard.gameloop.GameLoop(
            self._game,
            StubRenderer(),
            StubEventQueue(events)
        )

        self.assertTrue(game_loop.handle_events())
        self.assertEqual(self._game.map[0][0], 16)

    def test_can_move_down(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_DOWN)]

        game_loop = gameboard.gameloop.GameLoop(
            self._game,
            StubRenderer(),
            StubEventQueue(events)
        )

        self.assertTrue(game_loop.handle_events())
        self.assertEqual(self._game.map[2][0], 16)

    def test_game_ends(self):
        self._game.map = [[2, 4, 2],
               [1024, 2, 4],
               [1024, 4, 2]]

        events = [StubEvent(pygame.KEYDOWN, pygame.K_DOWN)]

        game_loop = gameboard.gameloop.GameLoop(
            self._game,
            StubRenderer(),
            StubEventQueue(events)
        )

        game_loop.start()

        self.assertFalse(game_loop.handle_events())
        self.assertEqual(self._game.biggest, 2048)
