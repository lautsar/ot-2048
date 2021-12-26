import unittest
import pygame

import gameboard.tiles
import gameboard.gameloop

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

LEVEL_MAP_1 = [[0, 4, 0],
               [1, 0, 0],
               [1, 2, 3]]

CELL_SIZE = 50


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP_1, CELL_SIZE)

    def test_can_complete_level(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
        ]

        game_loop = gameboard.GameLoop(
            self._board,
            StubRenderer(),
            StubEventQueue(events),
        )

        game_loop.start()

        self.assertTrue(self.level_1.is_completed())