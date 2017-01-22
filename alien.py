import pygame
from pygame.sprite import Sprite
pygame.init()

pygame.init()
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/zombie.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.sound_alien = pygame.mixer.Sound('sounds/zombie.wav')

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def soundme(self):
        sound_alien_chanel = self.sound_alien.play(-1)
        sound_alien_chanel.set_volume(self.ai_settings.sound_alien_volume)

    def update(self):
        """Перемещает        пришельца        вниз."""
        self.y += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.y = self.y


    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True
