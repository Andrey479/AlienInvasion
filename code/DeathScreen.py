import pygame
from pygame import Surface, Rect, KEYDOWN, K_ESCAPE, K_RETURN
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, C_WHITE, C_YELLOW


class DeathScreen:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.death_text(50, 'YOU DIED', C_ORANGE, ((WIN_WIDTH / 2), 100))
            self.death_text(20, 'Press ESC to return to menu', C_WHITE, ((WIN_WIDTH / 2), 200))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                    if event.key == K_RETURN:
                        return

    def death_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
