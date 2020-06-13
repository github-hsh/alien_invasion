#bullet.py
from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, alien_settings, screen, ship):
        '''在飞船所在位置创建子弹对象'''
        super(Bullet, self).__init__()
        self.screen = screen

        #在(0,0)处创建一个表示子弹的矩形，再设置正确位置
        self.rect = pygame.Rect(0, 0, alien_settings.bullet_width, alien_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #子弹位置
        self.y = float(self.rect.y)

        self.color = alien_settings.bullet_color
        self.speed_factor = alien_settings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        #更新子弹位置的小数值
        self.y -= self.speed_factor
        #更新子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)