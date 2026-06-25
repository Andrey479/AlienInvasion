
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT, BG_LAYER_COUNT, ENEMY_SPAWN_OFFSET, \
    ENEMY_SPAWN_MIN_Y, PLAYER_START_X
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(BG_LAYER_COUNT):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                player = Player('Player1', (PLAYER_START_X, 0))
                player.rect.bottom = WIN_HEIGHT
                return player
            case 'Enemy1':
                x = -ENEMY_SPAWN_OFFSET if random.choice((True, False)) else WIN_WIDTH + ENEMY_SPAWN_OFFSET
                return Enemy('Enemy1', (x, random.randint(ENEMY_SPAWN_MIN_Y, WIN_HEIGHT // 2)))
            case 'Enemy2':
                x = -ENEMY_SPAWN_OFFSET if random.choice((True, False)) else WIN_WIDTH + ENEMY_SPAWN_OFFSET
                enemy = Enemy('Enemy2', (x, 0))
                enemy.rect.bottom = WIN_HEIGHT
                return enemy
            case 'Boss':
                x = -ENEMY_SPAWN_OFFSET if random.choice((True, False)) else WIN_WIDTH + ENEMY_SPAWN_OFFSET
                return Enemy('Boss', (x, random.randint(ENEMY_SPAWN_MIN_Y, WIN_HEIGHT // 2)))
        return None
            