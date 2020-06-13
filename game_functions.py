#game_function.py
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, alien_settings, screen, ship, bullets):
    '''键盘按下'''
    if event.key == pygame.K_RIGHT:
        # 右移飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(alien_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    '''键盘松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(alien_settings, screen, stats, play_button, ship, bullets):
    '''监听鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, alien_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)

def check_play_button(stas, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stas.game_active = True

def update_screen(alien_setting, screen, stats, ship, aliens, bullets, play_button):
    '''更新图像，切换到新屏幕'''
    #重绘屏幕
    screen.fill(alien_setting.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #对于非活动状态的游戏绘制‘Play’按钮
    if not stats.game_active:
        play_button.draw_button()

    #对最新的屏幕可见
    pygame.display.flip()

def update_bullets(aliens, bullets):
    '''更新子弹位置，删除消失的子弹'''
    #更新子弹位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 在确认子弹删除后，print要注释掉
    # print(len(bullets))

    #检查是否有子弹击中了外星人，击中则删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def fire_bullet(alien_settings, screen, ship, bullets):
    '''没有达到子弹数量限制，就发射一颗子弹'''
    # 创建一颗子弹，并加入到编组bullets中
    if len(bullets) < alien_settings.bullets_allowed:
        new_bullet = Bullet(alien_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(alien_settings, screen, ship, aliens):
    '''创建外星人群'''
    alien = Alien(alien_settings, screen)
    number_aliens_x = get_number_aliens_x(alien_settings, alien.rect.width)
    number_rows = get_number_row(alien_settings, ship.rect.height, alien.rect.height)

    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(alien_settings,screen,aliens, alien_number, row_number)

def get_number_aliens_x(alien_settings, alien_width):
    '''计算每行可以容纳的外星人数目'''
    available_space_x = alien_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(alien_settings, screen, aliens, alien_number, row_number):
    '''创建外星人，放入当前行'''
    alien = Alien(alien_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_row(alien_settings, ship_height, alien_height):
    '''计算容纳外星人的行数'''
    available_space_y = (alien_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def check_fleet_edges(alien_settings, aliens):
    '''对边缘的外星人进行操作'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(alien_settings, aliens)
            break

def change_fleet_direction(alien_settings, aliens):
    '''外星人下移，并改变移动方向'''
    for alien in aliens.sprites():
        alien.rect.y += alien_settings.fleet_drop_speed
    alien_settings.fleet_direction *= -1

def update_aliens(alien_settings, stats, screen, ship, aliens, bullets):
    '''检查外星人是否在边缘，更新外星人群中所有外星人的位置'''
    check_fleet_edges(alien_settings, aliens)
    aliens.update()

    #检查外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(alien_settings, stats, screen, ship, aliens, bullets)
        print("ship hit !!".title())
    check_alien_bottom(alien_settings, stats, screen, ship, aliens, bullets)

def ship_hit(alien_settings, stats, screen, ship, aliens, bullets):
    '''对撞到外星人的飞船进行处理'''
    if stats.ships_left > 0:
        #ship_left - 1
        stats.ships_left -= 1

        #清空子弹列表和外星人
        aliens.empty()
        bullets.empty()

        #创建新的外星人，放在屏幕低端
        create_fleet(alien_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(3)
    else:
        stats.game_active = False

def check_alien_bottom(alien_settings, stats, screen, ship, aliens, bullets):
    '''检查是否有外星人到达屏幕底部'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像处理飞船碰撞外星人一样
            ship_hit(alien_settings, stats, screen, ship, aliens, bullets)
            break










































