import pygame
import values

class Tiles:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.blanks = pygame.sprite.Group()
        self.value2 = pygame.sprite.Group()
        self.value4 = pygame.sprite.Group()
        self.value8 = pygame.sprite.Group()
        self.value16 = pygame.sprite.Group()
        self.value32 = pygame.sprite.Group()
        self.value64 = pygame.sprite.Group()
        self.value128 = pygame.sprite.Group()
        self.value256 = pygame.sprite.Group()
        self.value512 = pygame.sprite.Group()
        self.value1024 = pygame.sprite.Group()
        self.value2048 = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.update_sprites(level_map)

    def update_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.blanks.add(values.Blank(normalized_x, normalized_y))
                elif cell == 2:
                    self.value2.add(values.Value2(normalized_x, normalized_y))
                elif cell == 4:
                    self.value4.add(values.Value4(normalized_x, normalized_y))
                elif cell == 8:
                    self.value8.add(values.Value8(normalized_x, normalized_y))
                elif cell == 16:
                    self.value16.add(values.Value16(normalized_x, normalized_y))
                elif cell == 32:
                    self.value32.add(values.Value32(normalized_x, normalized_y))
                elif cell == 64:
                    self.value64.add(values.Value64(normalized_x, normalized_y))
                elif cell == 128:
                    self.value128.add(values.Value128(normalized_x, normalized_y))
                elif cell == 256:
                    self.value256.add(values.Value256(normalized_x, normalized_y))
                elif cell == 512:
                    self.value512.add(values.Value512(normalized_x, normalized_y))
                elif cell == 1024:
                    self.value1024.add(values.Value1024(normalized_x, normalized_y))
                elif cell == 2048:
                    self.value2048.add(values.Value2048(normalized_x, normalized_y))

        self.all_sprites.add(
            self.blanks,
            self.value2,
            self.value4,
            self.value8,
            self.value16,
            self.value32,
            self.value64,
            self.value128,
            self.value256,
            self.value512,
            self.value1024,
            self.value2048
        )
