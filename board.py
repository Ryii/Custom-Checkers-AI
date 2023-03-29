import pygame
import numpy as np
from constants import NUM_ROWS, NUM_COLS
from piece import Piece

class Board:
    def __init__(self):
        ## 2D array of pieces ##
        self.board = self.new_board()
        self.team_1_men = self.team_2_men = 12
        self.team_1_kings = self.team_2_kings = 0

    def new_board(self):
        new_board = []
        for row in range(NUM_ROWS):
            new_row = []
            for col in range(NUM_COLS):
                if ((row + col) % 2 == 0 or row == 3 or row == 4):
                    new_row.append(None)
                elif (row < 3):
                    new_row.append(Piece(2))
                else:
                    new_row.append(Piece(1))
            new_board.append(new_row)
        return new_board

    def print_board(self): # for testing purposes
        for x in self.board:
            for y in x:
                print(y.team, end='') if y != None else print(0, end='')
            print()

    def move(self, piece, start_row, start_col, end_row, end_col):
        self.board[end_row, end_col] = piece
        self.board[start_row, start_col] = None

        if (end_row == 0 or end_row == NUM_ROWS - 1) and piece.is_king == False:
            piece.kingify()
            if piece.team == 1:
                self.team_1_kings += 1
                self.team_1_men -= 1
            else:
                self.team_2_kings += 1
                self.team_2_men -= 2

    # def get_possible_moves(self, row, col):
    #     possible_moves = np.array([])
    #     possible_removals = np.array([])
    #     possible_steps = self.get_steps(row, col)
    #     possible_jumps, removals = self.get_jumps(row, col)   

    #     possible_moves = np.append(possible_moves, [possible_steps], axis=0)
    #     possible_removals = np.append() * len(possible_steps)
    #     return possible_moves, possible_removals

    def get_possible_moves(self, row, col):
        possible_moves = []
        possible_removals = []
        possible_steps = self.get_steps(row, col)
        possible_jumps, removals = self.get_jumps(row, col)   

        possible_moves += possible_steps
        possible_removals += [] * len(possible_steps)
        return possible_moves, possible_removals
    
    def get_steps(self, row, col):
        possible_steps = []

        # check for steps going up one row
        if row != 0 and (self.board[row][col].team == 1 or self.board[row][col].is_king):
            if col - 1 >= 0 and self.board[row - 1][col - 1] == None:
                possible_steps.append((row - 1, col - 1))
            if col + 1 < 8 and self.board[row - 1][col + 1] == None:
                possible_steps.append((row - 1, col + 1))

        # check for steps going down one row
        if row != 7 and (self.board[row][col].team == 2 or self.board[row][col].is_king):
            if col - 1 >= 0 and self.board[row + 1][col - 1] == None:
                possible_steps.append((row + 1, col - 1))
            if col + 1 < 8 and self.board[row + 1][col + 1] == None:
                possible_steps.append((row + 1, col + 1))

        return possible_steps
    
    def get_jumps(self):
        possible_jumps = []
        removals = []
        return possible_jumps, removals
    
    def left_move(self):
        return
    
    def right_move(self):
        return
    
    def remove_positions(self, removals, from_team):
        for row, col in removals:
            if from_team == 1:
                if self.board[row][col].is_king:
                    self.team_1_kings -= 1
                else:
                    self.team_1_men -= 1
            else:
                if self.board[row][col].is_king:
                    self.team_2_kings -= 1
                else:
                    self.team_2_men -= 1
            self.board[row][col] = None
            