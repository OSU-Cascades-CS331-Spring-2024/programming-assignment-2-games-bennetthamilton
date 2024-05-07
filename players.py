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

    def get_move(self, board):
        return self.minimax()
    
    def clone(self):
        return MinimaxPlayer(self.symbol)
    
    # returns a tuple for row and col decision after running minimax algorithm
    def minimax(self):
        # TODO: Implement minimax algorithm
        # placeholder code
        row = 0
        col = 0
        return row, col
       
    # returns the max value of the board state
    def max_value(self, board):
        pass

    # returns the min value of the board state
    def min_value(self, board):
        pass

    # returns the heuristic value of the board state
    def heuristic(self, board):
        pass