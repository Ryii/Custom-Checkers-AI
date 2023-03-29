import pygame
from graphics import Graphics
from board import Board
from constants import SQUARE_SIZE

class Game:
    def __init__(self):
        self.graphics = Graphics()
        self.board = Board()
        self.turn = 1
        self.finished = False
        self.selected_pieces_moves = None

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
                # moves, removals = self.board.get_possible_moves(row, col)
                # print(moves, removals)
                # game.select_square(row, col)

    def select_square(self, row, col):
        # check if is in allowed moves, or is another piece
        if self.selected_pieces_moves != None:
            return
    
    def update(self):
        self.graphics.draw_all(self.board)

    def change_turn(self):
        self.turn = 2 if self.turn == 1 else 1
        self.selected_pieces_moves = None

    def exit_game(self):
        self.finished = True
