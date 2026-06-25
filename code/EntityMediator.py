from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy) and ent.name != 'Boss':
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, (PlayerShot, EnemyShot)):
            if (ent.rect.right <= 0 or ent.rect.left >= WIN_WIDTH or
                    ent.rect.bottom <= 0 or ent.rect.top >= WIN_HEIGHT):
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                if isinstance(ent1, (PlayerShot, EnemyShot)):
                    projectile, target = ent1, ent2
                else:
                    projectile, target = ent2, ent1
                target.health -= projectile.damage
                target.last_dmg = projectile.name
                projectile.health = 0

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            copied_list = entity_list.copy()
            for ent in copied_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):

        # separado em subgrupos para evitar comparações desnecessárias
        enemies = [ent for ent in entity_list if isinstance(ent, Enemy)]
        enemies_shots = [ent for ent in entity_list if isinstance(ent, EnemyShot)]
        players = [ent for ent in entity_list if isinstance(ent, Player)]
        player_shots = [ent for ent in entity_list if isinstance(ent, PlayerShot)]

        for entity in entity_list:
            EntityMediator.__verify_collision_window(entity)
        for enemy in enemies:
            for shot in player_shots:
                EntityMediator.__verify_collision_entity(enemy, shot)
        for player in players:
            for shot in enemies_shots:
                EntityMediator.__verify_collision_entity(player, shot)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        is_the_boss_dead = False
        dead_enemies = 0
        copied_list = entity_list.copy()
        for ent in copied_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                    dead_enemies += 1
                if ent.name == "Boss":
                    is_the_boss_dead = True
                entity_list.remove(ent)
        return dead_enemies, is_the_boss_dead