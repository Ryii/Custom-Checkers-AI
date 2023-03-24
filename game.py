import pygame
from graphics import Graphics
from board import Board

class Game:
    def __init__(self):
        pygame.init()
        self.graphics = Graphics()
        self.board = Board()

    def initial_setup(self):
        self.graphics.setup()

    def end_game(self):
        pygame.quit()
    
    def update(self):
        self.graphics.draw_all()
