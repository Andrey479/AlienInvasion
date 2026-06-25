
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, WIN_HEIGHT, \
    MENU_FONT, C_BLACK, TITLE_FONT_DIVISOR, MENU_FONT_DIVISOR, CONTROLS_FONT_DIVISOR, \
    TITLE_Y_RATIO, OPTIONS_START_Y_RATIO, OPTIONS_SPACING_RATIO, TITLE_SHADOW_OFFSET, \
    CONTROLS_RIGHT_MARGIN, CONTROLS_TITLE_BOTTOM, CONTROLS_MOVE_BOTTOM, CONTROLS_JUMP_BOTTOM, \
    CONTROLS_SHOOT_BOTTOM, CONTROLS_AIM_BOTTOM


class Menu:
    def __init__(self, window):
        self.window = window
        self.bg_layers = []
        filenames = [
            'layer-bg',
            'layer-mountains-far',
            'layer-mountains',
            'layer-trees',
            'layer-trees-front',
        ]
        for name in filenames:
            surf = pygame.image.load(f'./asset/{name}.png').convert_alpha()
            surf = pygame.transform.scale(surf, (WIN_WIDTH, WIN_HEIGHT))
            self.bg_layers.append(surf)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Level1.mp3')
        pygame.mixer_music.play(-1)
        while True:
            for layer in self.bg_layers:
                self.window.blit(source=layer, dest=(0, 0))
            self.menu_text(WIN_WIDTH // TITLE_FONT_DIVISOR, "Alien Invasion", C_BLACK, (WIN_WIDTH // 2, int(WIN_HEIGHT * TITLE_Y_RATIO) + TITLE_SHADOW_OFFSET))
            self.menu_text(WIN_WIDTH // TITLE_FONT_DIVISOR, "Alien Invasion", C_ORANGE, (WIN_WIDTH // 2, int(WIN_HEIGHT * TITLE_Y_RATIO)))

            option_y_start = WIN_HEIGHT * OPTIONS_START_Y_RATIO
            option_spacing = WIN_HEIGHT * OPTIONS_SPACING_RATIO
            for i in range(len(MENU_OPTION)):
                y = option_y_start + option_spacing * i
                color = C_YELLOW if i == menu_option else C_WHITE
                self.menu_text(WIN_WIDTH // MENU_FONT_DIVISOR, MENU_OPTION[i], color, (WIN_WIDTH // 2, y))

            self.menu_text(WIN_WIDTH // CONTROLS_FONT_DIVISOR, 'Player1 Controls', C_WHITE, (WIN_WIDTH - CONTROLS_RIGHT_MARGIN, WIN_HEIGHT - CONTROLS_TITLE_BOTTOM), 'midright')
            self.menu_text(WIN_WIDTH // CONTROLS_FONT_DIVISOR, 'A/D - Move', C_WHITE, (WIN_WIDTH - CONTROLS_RIGHT_MARGIN, WIN_HEIGHT - CONTROLS_MOVE_BOTTOM), 'midright')
            self.menu_text(WIN_WIDTH // CONTROLS_FONT_DIVISOR, 'W - Jump', C_WHITE, (WIN_WIDTH - CONTROLS_RIGHT_MARGIN, WIN_HEIGHT - CONTROLS_JUMP_BOTTOM), 'midright')
            self.menu_text(WIN_WIDTH // CONTROLS_FONT_DIVISOR, 'MOUSE CLICK - Shoot', C_WHITE, (WIN_WIDTH - CONTROLS_RIGHT_MARGIN, WIN_HEIGHT - CONTROLS_SHOOT_BOTTOM), 'midright')
            self.menu_text(WIN_WIDTH // CONTROLS_FONT_DIVISOR, 'MOUSE MOVE - Aim', C_WHITE, (WIN_WIDTH - CONTROLS_RIGHT_MARGIN, WIN_HEIGHT - CONTROLS_AIM_BOTTOM), 'midright')
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, anchor='center'):
        text_font: Font = pygame.font.Font(MENU_FONT, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(**{anchor: text_center_pos})
        self.window.blit(source=text_surf, dest=text_rect)
