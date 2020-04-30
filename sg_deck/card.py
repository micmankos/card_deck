'''
Card belonging to poker style deck
'''
class Card:
    def __init__(self, rank, suit):
        '''
        Poker Card where suit and rank are represented as strings
        '''
        self.suit = suit
        self.rank = rank
        self.name = f"{rank} of {suit}"
        