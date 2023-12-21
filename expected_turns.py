"""
Expected number of turns when playing snakes and ladders.

Steps:
1. Construct board object, give options for where the ladders and snakes are. 

2. Function to calculate transition matrix and summation. 
"""

class Board:
    """
    the inputs snakes and ladders should be a list of tuples, where
    (a,b) represents a snake/ladder that goes from square a to b. 
    Naturally for snakes a>b, and for ladders a<b. - input checks
    """
    def __init__(self,board_size,snakes,ladders):
        self.board_size = board_size
        self.snakes = snakes
        self.ladders = ladders

    
