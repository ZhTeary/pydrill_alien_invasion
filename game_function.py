import sys

import pygame


def check_events(ship):
    """相应鼠标和事件"""
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
        elif event == pygame.KEYDOWN:
            if event == pygame.K_RIGHT:
                ship.rect.centerx+=1


def upgrade_screen(settings, screen, ship):
    """更新屏幕的图像，切换到新屏幕"""
    # 每次循环时都绘制屏幕
    screen.fill(settings.background_color)
    ship.blitme()

    # 让最近的绘制屏幕可见
    pygame.display.flip()
