'''
    Defines Othello Board class and supporting functions.
'''

from board import *


class OthelloBoard(Board):
    def __init__(self, rows, cols, p1, p2):
        Board.__init__(self, rows, cols)
        self.p1_symbol = p1
        self.p2_symbol = p2


#PYTHON: this function is substitute for clone. call as New = Old.clone_of_board()
    def clone_of_board(self):
        tmp = OthelloBoard(self.cols, self.rows, self.p1_symbol, self.p2_symbol)
        tmp.grid = copy.deepcopy(self.grid)
        return tmp

    def initialize(self):
        self.set_cell(self.cols //2 -1, self.rows //2 -1,   self.p1_symbol)
        self.set_cell(self.cols //2,    self.rows //2,      self.p1_symbol)
        self.set_cell(self.cols //2 -1, self.rows //2,      self.p2_symbol)
        self.set_cell(self.cols //2,    self.rows //2 -1,   self.p2_symbol)

#PYTHON: Instead of having side effects this function now returns a TUPLE
    def set_coords_in_direction(self, col, row, d):  # D=direction
        if d.name == 'N':
            row += 1
        elif d.name == 'NE':
            col+=1
            row+=1
        elif d.name == 'E':
            col+=1
        elif d.name == 'SE':
            col+=1
            row-=1
        elif d.name == 'S':
            row-=1
        elif d.name == 'SW':
            col-=1
            row-=1
        elif d.name == 'W':
            col-=1
        elif d.name == 'NW':
            col-=1
            row+=1
        else:
            print("Invalid Direction.")
        return  col, row

#Recursively travel in a direction
    def check_endpoint(self, col, row, symbol, d, match_symbol):#match is bool type
        if not self.is_in_bounds(col, row) or self.is_cell_empty(col,row):
            return False
        else:
            if match_symbol:
                if self.get_cell(col, row) == symbol:
                    return True
                else:
                    (next_col, next_row) = self.set_coords_in_direction(col, row, d)
                    return self.check_endpoint(next_col, next_row, symbol, d, match_symbol)
            else:
                if self.get_cell(col, row) == symbol:
                    return False
                else:
                    (next_col, next_row) = self.set_coords_in_direction(col, row, d)
                    return self.check_endpoint(next_col, next_row, symbol, d, not match_symbol)

    def is_legal_move(self, col, row, symbol):
        result = False
        if not self.is_in_bounds(col, row) or not self.is_cell_empty(col, row):
            return False
        for d in Direction: #enum from board.py
            (next_col, next_row) = self.set_coords_in_direction(col, row, d)
            if self.check_endpoint(next_col, next_row, symbol, d, False):
                return True
        return False
        
    def flip_pieces_helper(self, col, row, symbol, d):
        if self.get_cell(col, row) == symbol:
            return 0
        else:
            self.set_cell(col,row, symbol)
            (next_col, next_row) = self.set_coords_in_direction(col, row, d)
            return 1+ self.flip_pieces_helper(next_col, next_row, symbol, d)

    def flip_pieces(self, col, row, symbol):
        pieces_flipped = 0
        if not self.is_in_bounds(col, row):
            print("Flip Pieces bad params.")
            exit()
        for d in Direction:
            (next_col, next_row) = self.set_coords_in_direction(col,row,d)
            if self.check_endpoint(next_col, next_row, symbol, d, False):
                pieces_flipped += self.flip_pieces_helper(next_col, next_row, symbol, d)

        return pieces_flipped

    def has_legal_moves_remaining(self, symbol):
        for c in range (0, self.cols):
            for r in range (0, self.rows):
                if self.is_cell_empty(c, r) and self.is_legal_move(c, r, symbol):
                    return True
        return False

    def count_score(self, symbol):
        score = 0
        for c in range (0, self.cols):
            for r in range (0, self.rows):
                if self.grid[c][r] == symbol:
                    score+=1
        return score

    def play_move(self, col, row, symbol):
        self.set_cell(col, row, symbol)
        self.flip_pieces(col, row, symbol)

    # returns 1 if player 1 wins, -1 if player 2 wins, 0 if tie or game not over
    def utility(self):
        p1 = self.p1_symbol
        p2 = self.p2_symbol

        # if either player has legal moves remaining, game is not over
        if self.has_legal_moves_remaining(p1) or self.has_legal_moves_remaining(p2):
            return 0
        else:
            # player 1 is the maximizing player so if score is higher, player 1 wins
            if self.count_score(p1) > self.count_score(p2):
                return 1
            # player 2 is the minimizing player so if score is higher, player 2 wins
            elif self.count_score(p2) < self.count_score(p1):
                return -1
            else:
                return 0

    # returns a list of possible board states after a move
    def successors(self, symbol):
        successor_boards = []
        # iterate through all cells on the board
        for c in range (0, self.cols):
            for r in range (0, self.rows):
                # if cell is empty and move is legal, add to list of possible moves
                if self.is_cell_empty(c, r) and self.is_legal_move(c, r, symbol):
                    new_board = self.clone_of_board()   # make a copy of current state
                    new_board.play_move(c, r, symbol)   # play move
                    successor_boards.append(new_board)  # add to list
        return successor_boards
