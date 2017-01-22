# coding utf_8

import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
#from alien import Alien

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #screen.backgroud = ai_settings.background
    pygame.display.set_caption("Дима Супергерой")
    ship = Ship(screen, ai_settings)
    #alien = Alien(ai_settings, screen)

    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Запуск основоного цикла игры
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, ship, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens,bullets)


run_game()