import math

import pygame.mixer

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple, mouse_pos: tuple):
        super().__init__(name, position)
        dx = mouse_pos[0] - position[0]
        dy = mouse_pos[1] - position[1]
        hyp = math.hypot(dx, dy)
        if hyp != 0:
            self.dx = (dx / hyp) * ENTITY_SPEED[self.name]
            self.dy = (dy / hyp) * ENTITY_SPEED[self.name]
        else:
            self.dx = 0
            self.dy = 0

        shot_sound = pygame.mixer.Sound("./asset/Player1Shot.mp3")
        shot_sound.play()

    def move(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
