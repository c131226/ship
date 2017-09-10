'''
Created on 2017-8-6

@author: WE
'''
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (220,220,220)
        self.ship_speed_factor = 1.5
         #子弹的背景
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
        
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1