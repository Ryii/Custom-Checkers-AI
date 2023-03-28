import pygame
from graphics import Graphics
from board import Board
from constants import SQUARE_SIZE

class Game:
    def __init__(self):
        self.graphics = Graphics()
        self.board = Board()
        self.selected_piece = None
        self.turn = 1
        self.finished = False

    def initial_setup(self):
        self.graphics.setup(self.board)

    def players_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                print(row, col)
                if self.board.board[row][col] != None:
                    print(self.board.get_steps(row, col))
                # game.select(row, col)
    
    def update(self):
        self.graphics.draw_all(self.board)

    def change_turn(self):
        self.turn = 2 if self.turn == 1 else 1

    def exit_game(self):
        self.finished = True
