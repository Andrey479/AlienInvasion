import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, EVENT_ENEMY, SPAWN_TIME, C_GREEN, TIMEOUT_LEVEL, MENU_FONT
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        self.dead_enemies = 0
        self.boss_spawned = 0
        self.font14: Font = pygame.font.Font(MENU_FONT, 14)

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            player_pos = None

            copied_list = self.entity_list.copy()
            found_player = False
            for ent in copied_list:
                self.window.blit(source=ent.surf, dest=ent.rect)

                if isinstance(ent, Player):
                    found_player = True
                    player_pos = ent.rect
                    shoot = ent.shoot()

                    if shoot is not None:
                        self.entity_list.append(shoot)

                if isinstance(ent, Enemy):
                    ent.move(player_pos)
                    shoot = ent.shoot(player_pos)
                    if shoot is not None:
                        self.entity_list.append(shoot)
                else:
                    ent.move()

                if ent.name == 'Player1':
                    self.level_text(f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 55))

                if self.dead_enemies >= 20 and self.boss_spawned == 1:
                    if isinstance(ent, Player) and ent.name == 'Player1':
                        player_score[0] = ent.score

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    if self.boss_spawned == 0:
                        choice = random.choice(('Enemy1', 'Enemy2'))
                        self.entity_list.append(EntityFactory.get_entity(choice))


            self.level_text(f'{self.name}', C_WHITE, (10, 5))
            self.level_text(f'Enemies killed: {self.dead_enemies}', C_WHITE, (10, 30))
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            self.dead_enemies += EntityMediator.verify_health(entity_list=self.entity_list)
            if self.dead_enemies >= 20 and self.boss_spawned == 0:
                self.entity_list.append(EntityFactory.get_entity('Boss'))
                self.boss_spawned = 1

            if found_player and self.dead_enemies >= 21 and self.boss_spawned == 1:
                return True
            if not found_player:
                return False

    def level_text(self, text: str, text_color: tuple, text_pos: tuple):
        text_surf: Surface = self.font14.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
