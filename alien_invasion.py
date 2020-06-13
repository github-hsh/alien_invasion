#alien_invasion.py
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button

def run_game():
    #初始化游戏，创建屏幕对象
    pygame.init()
    alien_settings = Settings()
    screen = pygame.display.set_mode((alien_settings.screen_width, alien_settings.screen_height))
    pygame.display.set_caption('alien invasion')

    #创建飞船
    ship = Ship(alien_settings, screen)
    #创建用于子弹，外星人存储的编组
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.create_fleet(alien_settings, screen, ship, aliens)
    #创建用于存储游戏统计信息的实例
    stats = GameStats(alien_settings)
    #创建Play按钮
    play_button = Button(alien_settings, screen, 'Play')

    #开始游戏主循环
    while True:

        gf.check_events(alien_settings, screen, stats, play_button, ship, bullets)

        if stats.game_active  :
            ship.update()
            gf.update_bullets(aliens, bullets)
            gf.update_aliens(alien_settings, stats, screen, ship, aliens, bullets  )

        #每次循环重绘屏幕,对最新绘制的屏幕可见
        gf.update_screen(alien_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()

























