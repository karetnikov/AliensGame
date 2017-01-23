import sys
import pygame
import os
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # Обработка нажатий клавиш
    if event.key == pygame.K_UP:
        # двигаем корабль вверх
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # двигаем корабль вниз
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Создание новой пули и включение ее в группу bullets.
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    # Обработка отпуска клавиш
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    # Отслеживание событий клавиатуры и мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens ,bullets):
    screen.fill(ai_settings.bg_color)
    #screen.blit(ai_settings.background, screen.get_rect())
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # отброжение последнего прорисованного экрана
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # Проверка попаданий в пришельцев.
    # При обнаружении попадания удалить пулю и пришельца.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # Уничтожение существующих пуль и создание нового флота.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)



def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        Bullet.soundme(new_bullet)


def get_number_aliens_y(ai_settings, alien_height):
    """Вычисляет количество пришельцев в ряду."""
    available_space_y = ai_settings.screen_height - 2 * alien_height
    number_aliens_y = int(available_space_y / (2 * alien_height))
    return number_aliens_y
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду."""
    alien = Alien(ai_settings, screen)
    alien_height = alien.rect.height
    alien.y = alien_height + 2 * alien_height * alien_number
    alien.rect.y = alien.y
    alien.rect.x = alien.rect.width + 2 * alien.rect.width * row_number
    aliens.add(alien)
    aliens.add(alien)
    #alien.soundme()
def create_fleet(ai_settings, screen, ship, aliens):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление количества пришельцев в ряду.
    alien = Alien(ai_settings, screen)
    number_aliens_y = get_number_aliens_y(ai_settings, alien.rect.height)

    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Создание флота пришельцев.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_y):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_rows(ai_settings, ship_width, alien_width):
    """Определяет количество рядов, помещающихся на экране."""
    available_space_x = (ai_settings.screen_width - (3 * alien_width) - ship_width)
    number_rows = int(available_space_x / (2 * alien_width))
    return number_rows

def update_aliens(ai_settings, ship, aliens):
    """Обновляет позиции всех пришельцев во флоте."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Проверка коллизий "пришелец-корабль".
    if pygame.sprite.spritecollideany(ship, aliens):
        #print("Ship hit!!!")
        None

def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижение пришельцем края экрана."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Опускает весь флот и меняет направление флота."""
    for alien in aliens.sprites():
        alien.rect.x += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
