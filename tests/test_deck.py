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

            # fail at 53 card
            c = deck.deal_card()

    def test_deal_card_reduces_deck_cnt(self):
        assert 0

    def test_shuffled_deck_has_52_cards(self):
        assert 0

    def test_shuffle_has_valid_cards(self):
        assert 0

    def test_deck_is_empty_on_53rd_card_dealt(self):
        assert 0

    def test_deck_has_cards_for_52_cards_dealt(self):
        assert 0

    def test_init_deck_has_valid_cards(self):
        assert 0

    def test_init_deck_has_52_cards(self):
        assert 0

    def test_card_has_correct_attributes(self):
        assert 0
        
    def test_card_attributes_are_strings(self):
        assert 0
        