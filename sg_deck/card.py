'''
Card belonging to poker style deck
'''
class Card:
    def __init__(self, rank, suit):
        '''
        Poker Card where suit and rank are represented as strings
        '''
        self.suit = str(suit)
        self.rank = str(rank)
        self.name = f"{rank} of {suit}"
        