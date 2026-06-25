import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_BLACK = (0, 0, 0)

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

WIN_WIDTH = 960
WIN_HEIGHT = 540

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player1': 3,
    'Player1Shot': 12,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 5,
    'Boss': 1,
    'BossShot': 8,
}

ENTITY_HEALTH = {
    'Level1Bg0': 1,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level1Bg3': 1,
    'Player1': 100,
    'Player1Shot': 1,
    'Enemy1': 125,
    'Enemy1Shot': 1,
    'Enemy2': 100,
    'Enemy2Shot': 1,
    'Boss': 2000,
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
    'Enemy1Shot': 10,
    'Enemy2': 1,
    'Enemy2Shot': 5,
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
    'Enemy1': 100,
    'Enemy2': 100,
    'Boss': 60,
}

GRAVITY_VALUE = 1

PLAYER_JUMP_FORCE = -23
PLAYER_HITBOX_INSET = -40

FPS = 60
MUSIC_VOLUME = 0.3
ENEMIES_TO_SPAWN_BOSS = 50
ENEMIES_TO_WIN = ENEMIES_TO_SPAWN_BOSS + 1
BOSS_NOT_SPAWNED = 0
BOSS_SPAWNED = 1

BG_LAYER_COUNT = 4
ENEMY_SPAWN_OFFSET = 10
ENEMY_SPAWN_MIN_Y = 10
PLAYER_START_X = WIN_WIDTH // 2

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


HUD_FONT_SIZE = 14
HUD_LEVEL_POS = (10, int(WIN_HEIGHT * 0.01))
HUD_CHALLENGE_POS = (10, int(WIN_HEIGHT * 0.05))
HUD_ENEMIES_POS = (10, int(WIN_HEIGHT * 0.09))
HUD_PLAYER_POS = (10, int(WIN_HEIGHT * 0.13))
SCORE_TITLE_FONT_SIZE = 48
SCORE_BODY_FONT_SIZE = 20
PLAYER_NAME_LENGTH = 4
SCORE_FORMAT = '05d'
COL_NAME_RATIO = 0.20
COL_SCORE_RATIO = 0.50
COL_DATE_RATIO = 0.80

DEATH_TITLE_FONT_SIZE = 50
DEATH_BODY_FONT_SIZE = 20
DEATH_TITLE_Y = 100
DEATH_INSTR_Y = 200

TITLE_FONT_DIVISOR = 19
MENU_FONT_DIVISOR = 53
CONTROLS_FONT_DIVISOR = 64
TITLE_Y_RATIO = 0.18
OPTIONS_START_Y_RATIO = 0.45
OPTIONS_SPACING_RATIO = 0.06
TITLE_SHADOW_OFFSET = 3
CONTROLS_RIGHT_MARGIN = 20
CONTROLS_TITLE_BOTTOM = 90
CONTROLS_MOVE_BOTTOM = 70
CONTROLS_JUMP_BOTTOM = 55
CONTROLS_SHOOT_BOTTOM = 40
CONTROLS_AIM_BOTTOM = 25

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
