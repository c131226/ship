import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init() #初始化游戏并创建一个屏幕对象
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))#创建一个screen的显示窗口，
                                                             #指定了游戏窗口的尺寸
    pygame.display.set_caption('Alien Invasion')

    #创建一艘飞船
    ship = Ship(ai_settings, screen)    
    #创建一个储存子弹的编组
    bullets = Group()
    aliens = Group()
    
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        #每次循环时都重绘屏幕
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)



run_game()
