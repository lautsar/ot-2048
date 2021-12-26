import pygame

class Renderer:
    def __init__(self, display, board):
        self._display = display
        self._board = board

    def render(self):
        self._board.level.update_sprites(self._board.map)
        self._board.level.all_sprites.draw(self._display)

        pygame.display.update()

    def close_window(self):
        pygame.display.quit()
