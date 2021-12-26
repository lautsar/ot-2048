import pygame

class Value(pygame.sprite.Sprite):
    """Luokka kuvaa yhtä laudalle piirrettävää numerolaattaa."""
    def __init__(self, value, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load(f"src/assets/{value}.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
