# SG Card Deck
Author: Michael Mankos

**This is a sample Python project that is meant to showcase my experience.**

This projects implements a library for a standard Poker-style deck of 52 cards which can, in turn, be used to implement a card game. This deck does not include Jokers. 

## Dev Environment and Setup
This section details the development environment and how to set it up. This project assumes knowledge of conda and pip. 

The project uses conda 4.5.4 and python 3.6.5. Testing and linting are done with pytest and pylint respectively. 

Make sure to activate your conda environment for this project. Install conda dependencies followed by pip dependencies
```sh
conda install --file conda_req.txt
pip install -r requirements.txt
```

From the top-level directory of the repo, run tests 
```sh
python -m pytest tests/
```
This repo follows the coding guidelines from the standard configuration for [pylint](https://docs.pylint.org/en/1.6.0/intro.html) which references pep 8. Run pylint with below. Please make sure your pylint score is >= 9 before commiting to dev/master.
```
pylint <package or module>

# specifically for our repo
pylint sg_deck
pylint tests
```

## Usage
This section details some usage examples of the library. 

There are two classes - a `Deck` object which contains a list of `Card` objects. Please refer to the `Card` class in `card.py` to see the available class members. Usage of `Deck` is discussed in more detail below. This module is meant to be used as a basis for playing games such as Poker or BlackJack. The implementation of the Card values (i.e. 1 or 11 for an Ace in BlackJack) is left up to the discretion of the users of this module. Only basic functionality of a deck is provided, namely `deal_card()` and `shuffle()`. 

To `pip install`, the package must first be pushed up to PyPI. As this is a sample repo, test PyPI is used. Please refer to the `Build` section below to push and build to PyPI before performing a `pip install`. 

Import with
```py
import sg_deck
```
To instantiate a deck and deal the cards
```py
deck = sg_deck.Deck()
while not deck.is_empty():
    card = deck.deal_card()
    print(f"You have been dealt the {card.rank} of {card.suit}")    
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
    card = deck.deal_card()
    print(f"You have been dealt the {card.name}")       
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
    card = deck.deal_card()
    print(f"You have been dealt the {card.rank} of {card.suit}")    
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
"
TestPyPI is a separate instance of the Python Package Index (PyPI) that allows you to try out the distribution tools and process without worrying about affecting the real index.
"
Specifically, I followed the instructions listed by the [Python docs](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives).
```sh
# make sure latest build tools are installed
python -m pip install --user --upgrade setuptools wheel

# create distribution package that you can upload
python setup.py sdist bdist_wheel
```

You will have to create an account and retrieve an API token to [upload to test PyPI](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives). Generate a token and add it to your `$HOME/.pypirc` file as seen [here](https://packaging.python.org/guides/distributing-packages-using-setuptools/#create-an-account). 

Then continue with the build commands:
```sh
# install twine
python -m pip install --user --upgrade twine

# upload package to TESTPYPI
python -m twine upload --repository testpypi dist/*
```

You should now be able to install the pip package with
```sh
# the general command
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE

# as an example, below is specific to me (note that the last argument here is the `name` param in the setuptools.setup tuple in setup.py)
# also note that test pypi constantly refreshes so the package you uploaded may be deleted fairly quickly
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps sg_deck-micmankos
```