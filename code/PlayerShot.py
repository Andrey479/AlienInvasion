import pygame.mixer

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple, mouse_pos: tuple):
        super().__init__(name, position)
        self.position = pygame.math.Vector2(position)
        self.direction = pygame.math.Vector2(mouse_pos) - self.position

        if self.direction.length() > 0:
            self.direction.normalize_ip()

        shot_sound = pygame.mixer.Sound("./asset/Player1Shot.mp3")
        shot_sound.play()

    def move(self):
        self.position += self.direction * ENTITY_SPEED[self.name]
        self.rect.center = (int(self.position.x), int(self.position.y))
