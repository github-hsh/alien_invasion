#ship.py
import pygame

class Ship():
    def __init__(self,alien_settings, screen):
        '''初始化飞船及其位置'''
        self.screen = screen
        self.alien_settings = alien_settings

        #加载飞船图像，获得外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #飞船在屏幕底部中间
        self.rect.centerx =  self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #允许centerx的属性储存小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False


    def update(self):
        '''移动标志为True，则不断移动'''
        #更新飞船的center值，不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.alien_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.alien_settings.ship_speed_factor

        #由self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''飞船在屏幕居中'''
        self.center = self.screen_rect.centerx