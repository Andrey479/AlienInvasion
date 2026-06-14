import pygame

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, player_position: pygame.Rect = None):
        if player_position:
            if self.rect.centerx <= player_position.centerx:
                self.rect.centerx += ENTITY_SPEED[self.name]
            else:
                self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self, player_position: pygame.Rect = None):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            if player_position is None:
                return None
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery), player_pos=player_position)
