"""
Expected number of turns when playing snakes and ladders.

Steps:
1. Construct board object, give options for where the ladders and snakes are. 

2. Function to calculate transition matrix and summation. 
"""
import numpy as np

def extract_start(l):
    """
    l: list of tuples (a_i,b_i)
    get a list of the starting points a_i
    """
    r = [x[0] for x in l]
    return r


def extract_end(l):
    """
    l: list of tuples (a_i,b_i)
    get a list of the starting points a_i
    """
    r = [x[1] for x in l]
    return r

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

    def transition_matrix(self):
        T = np.zeros((self.board_size+1,self.board_size+1)) # +1 for including 0
        snake_mouths = extract_start(self.snakes)
        snake_tails = extract_end(self.snakes)
        ladder_bottoms = extract_start(self.ladders)
        ladder_tops = extract_end(self.ladders)

        for i in range(self.board_size):
            for j in range(i+1,min(i+6,self.board_size)+1):
                # check snakes first
                if j in snake_mouths:
                    # find the jth mouth and take to tail

                    # find index
                    j_ind = snake_mouths.index(j)

                    # put corresponding tail
                    tail = snake_tails[j_ind]
                    T[i,tail] = 1/6
                elif j in ladder_bottoms:
                    # find the jth ladder and take to top

                    j_ind = ladder_bottoms.index(j)

                    top = ladder_tops[j_ind]
                    T[i,top] = 1/6
                else:
                    T[i,j] = 1/6

        # remove rows/cols corresponding to ladder bottoms and snake mouths
        # due to the +1 shift, index is indeed the number
        for i in snake_mouths + ladder_bottoms:
            for j in [0,1]:
                T = np.delete(T,(i),axis=j)



        return T    
    
    def first_row_of_exp(self):
        T = self.transition_matrix()

        # remove final row and col
        for j in [0,1]:
            T = np.delete(T,(-1),axis=j)

        # compute (I-T)^{-1}
        R = np.linalg.inv((np.identity(len(T) - T)))

        return R[0,:]    

    def expected_on_square(self,n):
        R0 = self.first_row_of_exp()
        return R0[n]
    
    def expected_number_of_turns_to_reach_end(self):
        R0 = self.first_row_of_exp()
        return sum(R0)