import pygame

import config as c
from game_object import GameObject


class Paddle(GameObject):
    def __init__(self, x, y, w, h, color, offset):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.offset = offset
        self.moving_left = False
        self.moving_right = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)
#При нажатии или отпускании клавиши вызывается метод handle.
# Ракетки не нужно знать, было ли это событие нажатия или отпускания клавиши,
# потому что он управляет текущим состоянием с помощью: moving_left и moving_right.
# Если moving_left равна True, то значит, была нажата клавиша «влево», и следующим событием будет отжатие клавиши,
# которое сбросит переменную. То же самое относится и к клавише «вправо».
    def handle(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        else:
            self.moving_right = not self.moving_right
#перемещение ракетки, также установка границ, чтобы ракетка не выходила за границы приложения
    def update(self):
        if self.moving_left:
            dx = -(min(self.offset, self.left))
        elif self.moving_right:
            dx = min(self.offset, c.screen_width - self.right)
        else:
            return

        self.move(dx, 0)