'''
    Defines Player class, and subclasses Human and Minimax Player.
'''

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return col, row


class MinimaxPlayer(Player):

    def __init__(self, symbol,):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
        self.depth = self.get_depth_from_user()

    def get_depth_from_user(self):
        return int(input("Enter depth for Minimax player: "))
    
    def clone(self):
        return MinimaxPlayer(self.symbol)

    def get_move(self, board):
        return self.minimax(board, self.depth)
    
    # returns a tuple for row and col decision after running minimax algorithm
    def minimax(self, board, depth):
        _, col, row = self.max_value(board, depth)
        return col, row
       
    # returns the max value, best column, and best row of the board state
    def max_value(self, board, depth):
        # return utility if depth is 0 or no legal moves
        if depth == 0 or not board.has_legal_moves_remaining(self.symbol):
            return self.heuristic(board), None, None
        
        # initialize best values
        max_value = float('-inf')   # negative infinity
        best_col = None
        best_row = None

        # iterate through all possible moves
        for successor in board.successors(self.symbol):
            # get min value of board state
            value, _, _ = self.min_value(successor, depth - 1)
            # update best values if value is greater
            if value > max_value:
                max_value = value
                best_col, best_row = successor.last_move # get last move

        return max_value, best_col, best_row

    # returns the min value, best column, and best row of the board state
    def min_value(self, board, depth):
        # return utility if depth is 0 or no legal moves
        if depth == 0 or not board.has_legal_moves_remaining(self.oppSym):
            return self.heuristic(board), None, None
        
        # initialize best values
        min_value = float('inf')
        best_col = None
        best_row = None

        # iterate through all possible moves
        for successor in board.successors(self.oppSym):
            # get max value of board state
            value, _, _ = self.max_value(successor, depth - 1)
            # update best values if value is less
            if value < min_value:
                min_value = value
                best_col, best_row = successor.last_move # get last move

        return min_value, best_col, best_row

    # returns the heuristic value of the board state
    def heuristic(self, board):
        return board.utility(self.symbol) - board.utility(self.oppSym)