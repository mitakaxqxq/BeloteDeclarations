from card import Card
import random

class Deck:

    def __init__(self):
        self.cards = []

        values = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        for value in values:
            self.cards.append(Card(value,'clubs'))
            self.cards.append(Card(value,'diamonds'))
            self.cards.append(Card(value,'hearts'))
            self.cards.append(Card(value,'spades'))

    def __str__(self):

        string = ''

        for card in self.cards:
            string += str(card)
            string += ' '

        return string[:-1]

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal(self):
        hand_of_cards = self.cards[:8]
        self.cards = self.cards[8:32] + hand_of_cards
        return hand_of_cards