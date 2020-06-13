#settings.py
'''
创建settings类，将游戏的所有设置储存在这里
'''

class Settings():
    def __init__(self):
        '''初始化设置'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船的设置
        self.ship_speed_factor = 1.5

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1
        #fleet_drop_speed为外星人撞到屏幕边缘时向下移动的速度
        self.fleet_drop_speed = 10
        #fleet_direction为1,表示向右，为-1表示向左
        self.fleet_direction = 1

        #飞船设置
        self.ship_limit = 3
