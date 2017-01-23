import pygame

class Settings():
    def __init__(self):
        """инициализирует настройки игры."""
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #self.background = pygame.image.load('images/background.bmp')
        self.ship_speed_factor = 5
        # Параметры пули
        self.bullet_speed_factor = 3
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
        self.sound_alien_volume = 0.3
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 100
        # fleet_direction = 1 обозначает движение вниз; а -1 - вверх.
        self.fleet_direction = 1


