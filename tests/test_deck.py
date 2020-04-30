'''
Tests functionality of deck and card modules
'''
import pytest
import sg_deck

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

        assert(desk.is_empty())

    def test_deck_is_empty_is_false_on_deck_with_cards(self):
        deck = sg_deck.Deck()

        for i in range(52):
            deck.deal_card()
            assert(not desk.is_empty())

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

    def test_init_deck_has_52_cards_objects(self):
        assert 0

    def test_card_has_correct_attributes(self):
        assert 0
        
    def test_card_attributes_are_strings(self):
        assert 0
        
    def test_init_deck_deals_all_poker_cards(self):
        assert 0

    def test_shuffled_deck_deals_all_poker_cards(self):
        assert 0