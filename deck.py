from card import Card
import random
from magic_strings import *

class Deck:

    def __init__(self):
        self.__cards = []
        for value in correct_values:
            self.__cards.append(Card(value,clubs))
            self.__cards.append(Card(value,diamonds))
            self.__cards.append(Card(value,hearts))
            self.__cards.append(Card(value,spades))

    def __str__(self):

        string = ''

        for card in self.__cards:
            string += str(card)
            string += ' '

        return string[:-1]
    
    def get_cards(self):
        return self.__cards

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal(self):
        hand_of_cards = self.__cards[:8]
        self.__cards = self.__cards[8:32] + hand_of_cards
        return sorted(hand_of_cards)

def main():
    pass

if __name__ == '__main__':
    main()