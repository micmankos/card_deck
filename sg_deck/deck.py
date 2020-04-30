'''
Module that implements a basic card deck that can be used to create a card game.
'''
# pylint: disable=len-as-condition

import random
from .card import Card

class Deck:
    '''
    Provides basic functionality of a card deck
    '''
    # pylint: disable=trailing-whitespace
    def __init__(self):
        '''
        Creates a deck of cards and private data structures used for reshuffling
        '''
        self._cards = []
        self.deck = []

        # dictionaries to easily retrieve common card info
        self._num_to_suit = dict()
        self._num_to_rank = dict() 
        self._num_to_suit[0] = "Hearts"
        self._num_to_suit[1] = "Spades"
        self._num_to_suit[2] = "Clubs"
        self._num_to_suit[3] = "Diamonds"
        
        for i in range(1, 14):
            if i == 1:
                self._num_to_rank[i] = "Ace"
            elif i == 11:
                self._num_to_rank[i] = "Jack"
            elif i == 12:
                self._num_to_rank[i] = "Queen"
            elif i == 13:
                self._num_to_rank[i] = "King"
            else:
                self._num_to_rank[i] = str(i)
        
        # create each Card object and create unshuffled deck
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(self._num_to_rank[rank], self._num_to_suit[suit])
                
                self._cards.append(card)
                self.deck.append(card)
        
    def shuffle(self):
        '''
        Shuffle returns no value, but results in the cards in the deck being randomly permuted. 
        '''
        
        # reintialize Cards in case references to Card objects were modified
        self._cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(self._num_to_rank[rank], self._num_to_suit[suit])
                self._cards.append(card)
        
        # create a random permutation of ints in range(52) that we 
        # will use to shuffle
        # Note - random.shuffle() was against the coding prompt
        ordering = [x for x in range(52)]
        card_ordering = list()
        
        # we have a list of unique ints in range 1 - 52 inclusive
        # randomly pull each one out to generate a random ordering
        while len(ordering) > 0:
            index = random.randint(0, len(ordering)-1)
            index = ordering.pop(index)
            card_ordering.append(index)

        # use ordering to add cards to deck
        self.deck = []
        for i in card_ordering:
            next_card = self._cards[i]
            self.deck.append(next_card)
        
    def deal_card(self):
        '''
        Returns one card from the deck to the caller. Else error is raised.
        '''
        if len(self.deck) > 0:
            return self.deck.pop(-1)
        else:
            raise IndexError("Attempted deal_card() called on empty deck. \
                Please call shuffle() to reshuffle deck.")
            
    def is_empty(self):
        '''
        Boolean to check if deck is empty
        '''
        if len(self.deck) == 0:
            return True
           
        return False
