import pygame
from constants import *

class Graphics:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))

    def setup(self):
        pygame.display.set_caption(CAPTION)
        self.draw_board()

    def draw_board(self):
        self.window.fill(BG_COLOR)
        for row in range(NUM_ROWS):
            for col in range((row + 1) % 2, NUM_COLS, 2):
                pygame.draw.rect(self.window, BG_COLOR_ALT, (row * SQUARE_WIDTH, col * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT))
                
    #def draw_pieces(self):

    def draw_all(self):

        pygame.display.update()
        self.clock.tick(FPS)
        