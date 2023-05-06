import sys

import pygame
from settings import Settings
from ship import Ship
from game_function import *


def run_game():
    """初始化游戏界面"""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_longth, settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个飞船
    ship = Ship(screen)
    # 开始游戏的主循环
    while True:

        # 更新屏幕
        upgrade_screen(settings, screen, ship)

        # 监视键盘和鼠标
        check_events(ship)



run_game()
