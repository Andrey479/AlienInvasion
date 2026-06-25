import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_JUMP, ENTITY_SHOT_DELAY, GRAVITY_VALUE, \
    PLAYER_JUMP_FORCE, PLAYER_HITBOX_INSET
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.rect.inflate_ip(PLAYER_HITBOX_INSET, 0)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.on_ground = True
        self.vertical_velocity = 0

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]]:
            self.surf = pygame.transform.flip(self.original_surf, True, False)
        elif pressed_key[PLAYER_KEY_RIGHT[self.name]]:
            self.surf = self.original_surf

        if not self.on_ground:
            self.vertical_velocity += GRAVITY_VALUE
            self.rect.centery += self.vertical_velocity

        if pressed_key[PLAYER_KEY_JUMP] and self.on_ground:
            self.vertical_velocity = PLAYER_JUMP_FORCE
            self.on_ground = False

        if self.rect.bottom >= WIN_HEIGHT and self.vertical_velocity >= 0:
            self.rect.bottom = WIN_HEIGHT
            self.on_ground = True
            self.vertical_velocity = 0


    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            if pygame.mouse.get_pressed()[0]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery), mouse_pos=pygame.mouse.get_pos())
            else:
                return None
        else:
            return None
