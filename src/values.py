import pygame

class Value2(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load("src/assets/2.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Value4(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load("src/assets/4.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Value8(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load("src/assets/8.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Value16(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load("src/assets/16.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Value32(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load("src/assets/32.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Value64(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load("src/assets/64.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Value128(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load("src/assets/128.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Value256(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load("src/assets/256.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Value512(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load("src/assets/512.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Value1024(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load("src/assets/1024.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Value2048(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load("src/assets/2048.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Blank(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load("src/assets/blank.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        