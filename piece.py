import pygame
from constants import CROWN, PIECE_1, PIECE_2, SQUARE_WIDTH, SQUARE_HEIGHT

class Piece:
    def __init__(self, team):
        self.team = team
        self.image = PIECE_1 if self.team == 1 else PIECE_2
        self.king = False

    def draw(self, row, col, screen):
        x = SQUARE_HEIGHT * col + SQUARE_HEIGHT / 2
        y = SQUARE_WIDTH * row + SQUARE_WIDTH / 2
        screen.blit(self.image, (x - self.image.get_width() / 2, y - self.image.get_height() / 2))
        if self.king:
            screen.blit(CROWN, (x - CROWN.get_width() / 2, y - CROWN.get_height() / 2))
        # print('row:', row, ', col:', col, ', x:', x, ', y:', y, self.team)
