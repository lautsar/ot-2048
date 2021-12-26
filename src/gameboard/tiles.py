import pygame
import gameboard.values

class Tiles:
    """Luokka vastaa pelilaudan laattojen asettamisesta pelilaudalle

    Attributes:
        cell_size: Yhden ruudun koko
        all_sprites: Kokoelma sprite-olioita eli numerolaattoja
    """
    def __init__(self, level_map, cell_size):
        """Luokan konstruktori, joka luo uuden pelilaudan

        Args:
            level_map: Piirrettävän pelilaudan kartta taulukkomuodossa
            cell_size: Piirrettävän ruudun koko
        """
        self.cell_size = cell_size
        self.all_sprites = pygame.sprite.Group()
        self.update_sprites(level_map)

    def update_sprites(self, level_map):
        """Metodi päivittää sprite-oliot annetun kartan mukaisesti.

        Args:
            level_map: Päivitetty kartta, joka täytyy piirtää
        """
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.all_sprites.add(gameboard.values.Value(0, normalized_x, normalized_y))
                else:
                    for i in range(1, 12):
                        if cell == pow(2, i):
                            self.all_sprites.add(gameboard.values.Value(pow(2, i), 
                                                normalized_x, normalized_y))
                            break
