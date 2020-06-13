#alien.py
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, alien_settings, screen):
        '''初始化外星人并设置初始位置'''
        super(Alien, self).__init__()
        self.screen = screen
        self.alien_settings = alien_settings

        #加载图像，设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #储存精确位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''如果外星人位于屏幕边缘，返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''向右或向左移动外星人'''
        self.x += (self.alien_settings.alien_speed_factor * self.alien_settings.fleet_direction)
        self.rect.x = self.x
