
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, WIN_HEIGHT


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
            # DRAW IMAGES
            for layer in self.bg_layers:
                self.window.blit(source=layer, dest=(0, 0))
            self.menu_text(50, "Alien", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Invasion", C_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            self.menu_text(18, 'Player 1 Controls', C_WHITE, (WIN_WIDTH - 100, WIN_HEIGHT - 80))
            self.menu_text(16, 'A/D - Move', C_WHITE, (WIN_WIDTH - 100, WIN_HEIGHT - 60))
            self.menu_text(16, 'W - Jump', C_WHITE, (WIN_WIDTH - 100, WIN_HEIGHT - 45))
            self.menu_text(16, 'MOUSE CLICK - Shoot', C_WHITE, (WIN_WIDTH - 100, WIN_HEIGHT - 30))
            self.menu_text(16, 'MOUSE MOVE - Shoot position', C_WHITE, (WIN_WIDTH - 100, WIN_HEIGHT - 15))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
