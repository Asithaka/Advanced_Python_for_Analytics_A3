import random

# Note 
# methods are fuctions
# method special operation perform on attribute

# The Coin class simulates a coin that can
# be flipped.

class Coin: # Name of our class
    # The _ _init_ _ method initializes the (This is the first method and it has the instructions on how to create this object)
    # sideup data attribute with 'Heads'.

    def __init__(self): 
        self.__sideup = 'Heads' # name of the attribute is sideup

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self): # method is toss
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
            return self.__sideup
