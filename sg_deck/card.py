'''
Card belonging to poker style deck
'''
# pylint: disable=too-few-public-methods

class Card:
    '''
    Card class where all attributes are strings.
    Suit is one of "Hearts", "Diamonds", "Spades", "Clubs".
    Rank can be either a value from 2-10, or an Ace, Jack, Queen, or King.
    '''
    def __init__(self, rank, suit):
        '''
        Poker Card where suit and rank are represented as strings
        '''
        self.suit = str(suit)
        self.rank = str(rank)
        self.name = f"{rank} of {suit}"
        