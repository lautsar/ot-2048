import pygame

class GameLoop:
    def __init__(self, board, renderer, event_queue):
        self._board = board
        self._renderer = renderer
        self._event_queue = event_queue

    def start(self):
        while True:
            if self.handle_events() is False:
                self._board.set_biggest()
                break

            self.render()

    def handle_events(self):
        for event in self._event_queue.get():
            if self._board.game_continues() is False:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self._board.move_left() is True:
                        self._board.new_tile()
                if event.key == pygame.K_RIGHT:
                    if self._board.move_right() is True:
                        self._board.new_tile()
                if event.key == pygame.K_UP:
                    if self._board.move_up() is True:
                        self._board.new_tile()
                if event.key == pygame.K_DOWN:
                    if self._board.move_down() is True:
                        self._board.new_tile()
            elif event.type == pygame.QUIT:
                return False

    def render(self):
        self._renderer.render()
