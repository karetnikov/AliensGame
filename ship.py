import pygame

class Ship():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        # Загружаем изображение и получаем прямоугольник
        self.image = pygame.image.load('images/ship_vert.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Новый корабль у правого края
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right
        self.center = float(self.rect.centery)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up:
            if self.rect.top > 0:
                self.center -= self.ai_settings.ship_speed_factor
        elif self.moving_down:
            if self.rect.bottom < self.ai_settings.screen_height:
                self.center += self.ai_settings.ship_speed_factor
        self.rect.centery = self.center

    def blitme(self):
        # Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
