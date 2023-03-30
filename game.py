import pygame
from graphics import Graphics
from board import Board
from constants import SQUARE_SIZE

class Game:
    def __init__(self):
        self.graphics = Graphics()
        self.Board = Board()
        self.turn = 1
        self.turnCount = 1
        self.finished = False
        self.selected_piece = None # (row, col)
        self.possible_moves = {} # dictionary of moves

    def initial_setup(self):
        self.graphics.setup(self.Board, self.possible_moves)

    def players_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE

                self.select_square(row, col)

                
                self.print_data() # TO BE DELETED

    def select_square(self, row, col):
        ## check if is in allowed moves -> move the piece
        if (row, col) in self.possible_moves:
            self.move_piece(row, col)
            self.change_turn()
            return
        
        ## check if team piece was selected
        if self.Board.board[row][col] != None and self.Board.board[row][col].team == self.turn:
            self.selected_piece = (row, col)
            self.possible_moves = self.Board.get_all_moves(row, col, self.turn, self.Board.board[row][col].is_king)
            return

        ## otherwise, empty square/enemy piece was selected
        self.selected_piece = None
        self.possible_moves = {}
        
    def move_piece(self, row, col):
        ## set the new position (check if became king)
        self.Board.board[row][col] = self.Board.board[self.selected_piece[0]][self.selected_piece[1]]

        # check if became king

        ## clear original position
        self.Board.board[self.selected_piece[0]][self.selected_piece[1]] = None

        ## remove skipped pieces
        if self.possible_moves[(row, col)]:
            enemy_team = 2 if self.turn == 1 else 1
            self.Board.remove_positions(self.possible_moves[(row, col)], enemy_team)
    
    def update(self):
        self.graphics.draw_all(self.Board, self.possible_moves)

    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
            self.turnCount += 1
        
        self.selected_piece = None
        self.possible_moves = {}

        self.Board.print_board() # TO BE DELETED

    def print_data(self):
        print('-----------------------')
        print("TURN " + str(self.turnCount) + ": TEAM " + str(self.turn))
        print('-----------------------')
        print('SELECTED PIECE: ' + str(self.selected_piece))
        print('POSSIBLE MOVES: ' + str(self.possible_moves))

    def exit_game(self):
        self.finished = True
