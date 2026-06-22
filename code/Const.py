import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player1': 3,
    'Player1Shot': 8,
    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 3,
    'Boss': 2,
    'BossShot': 6,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Player1': 100,
    'Player1Shot': 1,
    'Enemy1': 75,
    'Enemy1Shot': 1,
    'Enemy2': 125,
    'Enemy2Shot': 1,
    'Boss': 600,
    'BossShot': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 10,
    'Boss': 1,
    'BossShot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
    'Boss': 500,
    'BossShot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 6,
    'Enemy1': 120,
    'Enemy2': 120,
    'Boss': 120,
}

GRAVITY_VALUE = 1

MENU_FONT = './asset/PressStart2P-Regular.ttf'

MENU_OPTION = ('NEW GAME 1P',
               'SCORE',
               'EXIT')

PLAYER_KEY_LEFT = {'Player1': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': 0}  # Left mouse button

PLAYER_KEY_JUMP = pygame.K_w

SPAWN_TIME = 2000

TIMEOUT_STEP = 100
WIN_WIDTH = 960
WIN_HEIGHT = 540

SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
