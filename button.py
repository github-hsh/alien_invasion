#button.py

import pygame.font

class Button():
    def __init__(self, alien_settings, screen, msg):
        '''初始化按钮属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按钮的尺寸和属性
        self.width, self.height = 200, 50
        self.button_color = 0, 255, 0
        self.txt_color = 255, 255, 255
        self.font = pygame.font.SysFont(None, 48)

        #创建按钮的rect对象，居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #按钮标签只创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''msg渲染，居中'''
        self.msg_image = self.font.render(msg, True, self.txt_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''颜色填充，绘制文本'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

