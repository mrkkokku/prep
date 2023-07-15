import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A Class to represent a single alien in the fleet. """

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 화면 좌상단에서 시작할 수 있게 크기 잡아 줌
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 위치 추적
        self.x = float(self.rect.x)