import math

import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple, player_pos: pygame.Rect):
        super().__init__(name, position)
        dx = player_pos.centerx - position[0]
        dy = player_pos.centery - position[1]
        hyp = math.hypot(dx, dy)
        if hyp != 0:
            self.dx = (dx / hyp) * ENTITY_SPEED[self.name]
            self.dy = (dy / hyp) * ENTITY_SPEED[self.name]
        else:
            self.dx = 0
            self.dy = 0

        shot_sound = pygame.mixer.Sound(f"./asset/{self.name}.mp3")
        shot_sound.play()

    def move(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
