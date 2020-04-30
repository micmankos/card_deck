# SG Card Deck
Author: Michael Mankos

**This is a sample Python project that is meant to showcase my experience.**

This projects implements a library for a standard Poker-style deck of cards which can, in turn, be used to implement a card game. 

## Dev Environment
This section details the development environment and how to set it up. 

TODO: mention pep8 style

TODO: mention conda

Built with Conda and Python 3.6.5. Testing and linting are done with pytest and pylint respectively. 

From the top-level directory of the repo, run tests with
```
python -m pytest tests/
```

TODO: requirements.txt

TODO: setup.py

TODO: To run pylint...

## Usage
This section details some usage examples of the library. 

There are two objects - a `Deck` object which contains a list of `Card` objects. Please refer to the `Card` class in `card.py` to see the available class members. Usage of `Deck` is discussed in more detail below. This module is meant to be used as a basis for playing games such as Poker or BlackJack. The implementation of the Card values (i.e. 1 or 11 for an Ace in BlackJack) is left up to the discretion of the users of this module. Only basic functionality of a deck is provided, namely `deal_card()` and `shuffle()`. 

TODO: come back to this imports
Install with
```py
# Make sure that sg_deck is pushed to PyPI and that pip points at the correct PyPI (i.e. PyPI test server)
# See the "Build" section for more details
pip install sg_deck
```

Import with
```py
import sg_deck
```
To instantiate a deck and deal the cards
```py
deck = sg_deck.Deck()
while not deck.is_empty():
    c = deck.deal_card()
    print(f"You have been dealt the {c.rank} of {c.suit}")    
```
Notice the usage of `c.rank` and `c.suit`. The above code will print.
```
You have been dealt the King of Diamonds
You have been dealt the Queen of Diamonds
You have been dealt the Jack of Diamonds
You have been dealt the 10 of Diamonds
You have been dealt the 9 of Diamonds
You have been dealt the 8 of Diamonds
You have been dealt the 7 of Diamonds
You have been dealt the 6 of Diamonds
You have been dealt the 5 of Diamonds
You have been dealt the 4 of Diamonds
You have been dealt the 3 of Diamonds
You have been dealt the 2 of Diamonds
You have been dealt the Ace of Diamonds
You have been dealt the King of Clubs
You have been dealt the Queen of Clubs
...
```

Alternatively, we can reference the `rank` and `suit` through `name`
```py
deck = sg_deck.Deck()
while not deck.is_empty():
    c = deck.deal_card()
    print(f"You have been dealt the {c.name}")       
```
and we get similar output
```
You have been dealt the King of Diamonds
You have been dealt the Queen of Diamonds
You have been dealt the Jack of Diamonds
...
```

Instantiating the deck without calling `shuffle()` simply created an ordered list of cards. We can generate random permutations with `shuffle()`. Note that shuffling will reset the number of cards in the deck to 52. 
```py
deck.shuffle()
while not deck.is_empty():
    c = deck.deal_card()
    print(f"You have been dealt the {c.rank} of {c.suit}")    
```

```
You have been dealt the 3 of Diamonds
You have been dealt the 4 of Spades
You have been dealt the 6 of Hearts
You have been dealt the Jack of Clubs
You have been dealt the Queen of Diamonds
You have been dealt the Queen of Spades
...
```

Anytime `deal_card()` is called, the number of cards in the deck decreases by 1. As Poker-style decks only have 52 cards, attempting to deal a 53rd card raises an `IndexError` as seen below. 
```
IndexError: Attempted deal_card() called on empty deck. Please call shuffle() to reshuffle deck.
```

A method `is_empty()` is provided to check if the deck has cards left. 
```py
while not deck.is_empty():
  # do something
```
## Build
This example discusses how to package and push this code to PyPI. 

Do note that, as this is a sample project, we use PyPI's testing server. From [here](https://packaging.python.org/guides/using-testpypi/): 
```
TestPyPI is a separate instance of the Python Package Index (PyPI) that allows you to try out the distribution tools and process without worrying about affecting the real index.
```

TODO: build project and verify it works