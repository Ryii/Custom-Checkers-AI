import pygame
from constants import *

class Graphics:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))

    def setup(self, Board):
        pygame.display.set_caption(CAPTION)
        self.draw_all(Board)

    def draw_board(self):
        self.screen.fill(BG_COLOR)
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if (row + col) % 2 == 1:
                    pygame.draw.rect(self.screen, BG_COLOR_ALT, (row * SQUARE_WIDTH, col * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT))
                
    def draw_pieces(self, Board):
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if Board.board[row][col] != None:
                    Board.board[row][col].draw(row, col, self.screen)

    def draw_all(self, Board):
        self.draw_board()
        self.draw_pieces(Board)
        pygame.display.update()
        self.clock.tick(FPS)
        