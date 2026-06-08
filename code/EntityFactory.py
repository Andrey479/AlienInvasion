#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):  # level1bg images number
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(5):  # level2bg images number
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                player = Player('Player1', (10, 0))
                player.rect.bottom = WIN_HEIGHT
                return player
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                enemy = Enemy('Enemy1', (WIN_WIDTH + 10,  0))
                enemy.rect.bottom = WIN_HEIGHT
                return enemy
            case 'Enemy2':
                enemy = Enemy('Enemy2', (WIN_WIDTH + 10, 0))
                enemy.rect.bottom = WIN_HEIGHT
                return enemy
