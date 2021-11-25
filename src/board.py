import pygame
import tiles

class Board:
    def __init__(self, game):
        self.map = game.map
        self.game = game
        self.cell_size = 100
        self.level = tiles.Tiles(self.map, self.cell_size)

    def render(self):
        self.level.update_sprites(self.map)
        self.level.all_sprites.draw(self.display)
        pygame.display.update()

    def show(self):
        pygame.init()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.level.all_sprites.draw(self.display)
            pygame.display.flip()
