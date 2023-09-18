import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        # 将屏幕赋予给ship实例的一个属性，以便这个类的所有方法能够轻松访问
        self.screen = ai_game.screen
        # 将屏幕对象的矩阵对象赋予给ship实例的一个属性，同上的功能
        self.screen_rect = self.screen.get_rect()
        # 加载飞船图像并获取相应的surface对象
        self.image = pygame.image.load('images/ship.bmp')
        # 获取飞船的矩阵对象
        self.rect = self.image.get_rect()
        # 对于每艘新飞船都要放在屏幕底部的中央,类似属性还有top/bottom/center/centerx/centery/left/right/mid** ..
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
