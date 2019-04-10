from random import shuffle
from card import Card

class Deck():
    
    def __init__(self):
        cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        
        #build the deck
        self.cards = []
        for card in cards:
            for suit in suits:
                self.cards.append(Card(suit,card))

        #shuffle the deck
        shuffle(self.cards)

    def __str__(self):
        return str(self.cards)

    def deal_card(self):
        return self.cards.pop()
    