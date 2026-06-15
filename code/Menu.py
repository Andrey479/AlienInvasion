
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, WIN_HEIGHT, MENU_FONT


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
            self.menu_text(WIN_WIDTH // 19, "Alien Invasion", (0, 0, 0), (WIN_WIDTH // 2, int(WIN_HEIGHT * 0.18) + 3))
            self.menu_text(WIN_WIDTH // 19, "Alien Invasion", C_ORANGE, (WIN_WIDTH // 2, int(WIN_HEIGHT * 0.18)))

            option_y_start = WIN_HEIGHT * 0.45
            option_spacing = WIN_HEIGHT * 0.06
            for i in range(len(MENU_OPTION)):
                y = option_y_start + option_spacing * i
                color = C_YELLOW if i == menu_option else C_WHITE
                self.menu_text(WIN_WIDTH // 53, MENU_OPTION[i], color, (WIN_WIDTH // 2, y))

            self.menu_text(WIN_WIDTH // 64, 'Player1 Controls', C_WHITE, (WIN_WIDTH - 20, WIN_HEIGHT - 90), 'midright')
            self.menu_text(WIN_WIDTH // 64, 'A/D - Move', C_WHITE, (WIN_WIDTH - 20, WIN_HEIGHT - 70), 'midright')
            self.menu_text(WIN_WIDTH // 64, 'W - Jump', C_WHITE, (WIN_WIDTH - 20, WIN_HEIGHT - 55), 'midright')
            self.menu_text(WIN_WIDTH // 64, 'MOUSE CLICK - Shoot', C_WHITE, (WIN_WIDTH - 20, WIN_HEIGHT - 40), 'midright')
            self.menu_text(WIN_WIDTH // 64, 'MOUSE MOVE - Aim', C_WHITE, (WIN_WIDTH - 20, WIN_HEIGHT - 25), 'midright')
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
