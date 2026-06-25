import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_YELLOW, SCORE_POS, C_WHITE, WIN_WIDTH, WIN_HEIGHT, MENU_FONT, \
    SCORE_TITLE_FONT_SIZE, SCORE_BODY_FONT_SIZE, PLAYER_NAME_LENGTH, SCORE_FORMAT, \
    COL_NAME_RATIO, COL_SCORE_RATIO, COL_DATE_RATIO
from code.DBProxy import DBProxy

COL_NAME_X = WIN_WIDTH * COL_NAME_RATIO
COL_SCORE_X = WIN_WIDTH * COL_SCORE_RATIO
COL_DATE_X = WIN_WIDTH * COL_DATE_RATIO


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        score = player_score[0]
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(SCORE_TITLE_FONT_SIZE, 'YOU WIN', C_YELLOW, SCORE_POS['Title'])
            text = f'Enter Player1 name (exactly {PLAYER_NAME_LENGTH} characters):'
            self.score_text(SCORE_BODY_FONT_SIZE, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == PLAYER_NAME_LENGTH:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < PLAYER_NAME_LENGTH:
                            name += event.unicode
            self.score_text(SCORE_BODY_FONT_SIZE, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(SCORE_TITLE_FONT_SIZE, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        label_y = SCORE_POS['Label'][1]
        self.score_text(SCORE_BODY_FONT_SIZE, 'NAME', C_YELLOW, (COL_NAME_X, label_y))
        self.score_text(SCORE_BODY_FONT_SIZE, 'SCORE', C_YELLOW, (COL_SCORE_X, label_y))
        self.score_text(SCORE_BODY_FONT_SIZE, 'DATE', C_YELLOW, (COL_DATE_X, label_y))

        for i, player_score in enumerate(list_score):
            id_, name, score, date = player_score
            _, row_y = SCORE_POS[i]
            self.score_text(SCORE_BODY_FONT_SIZE, name, C_YELLOW, (COL_NAME_X, row_y))
            self.score_text(SCORE_BODY_FONT_SIZE, f'{score:{SCORE_FORMAT}}', C_YELLOW, (COL_SCORE_X, row_y))
            self.score_text(SCORE_BODY_FONT_SIZE, date, C_YELLOW, (COL_DATE_X, row_y))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font(MENU_FONT, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
