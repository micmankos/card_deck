'''
Tests functionality of deck and card modules
'''
import pytest
import sg_deck

CARDS = ['King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', \
            'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', \
            'King of Spades', 'Queen of Spades', 'Jack of Spades', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', \
            'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts']

class TestDeck:
    
    def test_can_deal_52_cards(self):
        deal_cnt = 0
        deck = sg_deck.Deck()

        while not deck.is_empty():
            c = deck.deal_card()
            deal_cnt += 1

        assert(deal_cnt == 52)

    def test_get_53rd_card_fails(self):
        deck = sg_deck.Deck()
        with pytest.raises(IndexError):
            # deal 52 cards
            for i in range(52):
                c = deck.deal_card()

            # fail at 53rd card
            c = deck.deal_card()

    def test_deal_card_reduces_deck_cnt(self):
        deck_len = 52
        deck = sg_deck.Deck()

        while not deck.is_empty():
            assert(len(deck.deck) == deck_len)
            c = deck.deal_card()
            deck_len -= 1

        assert(len(deck.deck) == deck_len)

    def test_shuffled_deck_has_52_cards(self):
        deck = sg_deck.Deck()
        deck.shuffle()
        assert(len(deck.deck) == 52)

    def test_deck_is_empty_after_52_cards_dealt(self):
        deck = sg_deck.Deck()

        for i in range(52):
            deck.deal_card()

        assert(deck.is_empty())

    def test_deck_is_empty_false_on_deck_with_cards(self):
        deck = sg_deck.Deck()

        for i in range(52):
            assert(deck.is_empty() == False)
            deck.deal_card()

    def test_each_item_dealt_is_card_on_init(self):
        card_obj = sg_deck.card.Card
        deck = sg_deck.Deck()

        for i in range(52):
            c = deck.deal_card()
            assert(isinstance(c, card_obj))

    def test_each_item_dealt_is_card_on_shuffle(self):
        card_obj = sg_deck.card.Card
        deck = sg_deck.Deck()
        deck.shuffle()

        for i in range(52):
            c = deck.deal_card()
            assert(isinstance(c, card_obj))

    def test_init_deck_has_52_cards(self):
        deck = sg_deck.Deck()
        assert(len(deck.deck) == 52)

    def test_shuffled_fixes_modified_card_objects(self):
        deck = sg_deck.Deck()

        some_string = "I wrote on this card"
        while not deck.is_empty():
            c = deck.deal_card()
            c.name = some_string

        deck.shuffle()
        while not deck.is_empty():
            c = deck.deal_card()
            assert(c.name != some_string)

    def test_card_has_correct_attributes_on_init(self):
        deck = sg_deck.Deck()

        while not deck.is_empty():
            c = deck.deal_card()
            assert(hasattr(c, 'name'))
            assert(hasattr(c, 'rank'))
            assert(hasattr(c, 'suit'))

    def test_card_has_correct_attributes_on_shuffle(self):
        deck = sg_deck.Deck()

        deck.shuffle()
        while not deck.is_empty():
            c = deck.deal_card()
            assert(hasattr(c, 'name'))
            assert(hasattr(c, 'rank'))
            assert(hasattr(c, 'suit'))
        
    def test_card_attributes_are_strings(self):
        deck = sg_deck.Deck()

        while not deck.is_empty():
            c = deck.deal_card()
            assert(isinstance(c.name, str))
            assert(isinstance(c.rank, str))
            assert(isinstance(c.suit, str))

        deck.shuffle()
        while not deck.is_empty():
            c = deck.deal_card()
            assert(isinstance(c.name, str))
            assert(isinstance(c.rank, str))
            assert(isinstance(c.suit, str))

    def test_card_name_matches_rank_and_suit(self):
        deck = sg_deck.Deck()
        while not deck.is_empty():
            c = deck.deal_card()
            rank_and_suit = f"{c.rank} of {c.suit}"
            assert(c.name == rank_and_suit)

        deck.shuffle()
        while not deck.is_empty():
            c = deck.deal_card()
            rank_and_suit = f"{c.rank} of {c.suit}"
            assert(c.name == rank_and_suit)
        
    def test_init_deck_deals_all_poker_cards(self):
        card_set = set()
        for c in CARDS:
            card_set.add(c)
            
        deck = sg_deck.Deck()
        while not deck.is_empty():
            c = deck.deal_card()
            assert(c.name in card_set)
            card_set.remove(c.name)

        assert(len(card_set) == 0)

    def test_shuffled_deck_deals_all_poker_cards(self):
        card_set = set()
        for c in CARDS:
            card_set.add(c)
            
        deck = sg_deck.Deck()
        deck.shuffle()
        
        while not deck.is_empty():
            c = deck.deal_card()
            assert(c.name in card_set)
            card_set.remove(c.name)

        assert(len(card_set) == 0)