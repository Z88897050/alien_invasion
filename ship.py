#!/usr/bin/python
# encoding: utf-8
import pygame


class Ship(object):
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        # 更新飞船的center值，而不是rect，rect和centerx等属性只能存储整数值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 向右移动飞船
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # 向左移动飞船
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象,centerx只存储center的整数部分
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
