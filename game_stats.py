#game_stats.py

class GameStats():
    '''跟踪游戏的统计信息'''
    def __init__(self, alien_settings):
        '''初始化统计信息'''
        self.alien_settings = alien_settings
        self.reset_stats()

        #游戏启动时为真
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.alien_settings.ship_limit