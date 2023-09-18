import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        # 初始化pygame的对象
        pygame.init()
        # 创建Settings对象
        self.settings = Settings()
        # 设置游戏窗口大小
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        # 展示游戏标题在左上角
        pygame.display.set_caption("Alien Invasion")
        # 创建飞船对象
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            self._check_events()
            # 每次循环时都重绘屏幕
            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        # 逐个遍历获取到的事件列表
        for event in pygame.event.get():
            # 若获取到的事件是关闭窗口则推出游戏
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 将飞船绘制到屏幕上，确保它出现在背景前面
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行
    ai = AlienInvasion()
    # 运行游戏
    ai.run_game()
