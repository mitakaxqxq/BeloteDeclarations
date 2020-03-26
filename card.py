class Card:

    def __init__(self,value,suit):
        self.validate_values(value,suit)

        self.value = value
        self.suit = suit

    def __str__(self):
        helping_dictionary = {'clubs':'c','diamonds':'d','hearts':'h','spades':'s'}

        return self.value + helping_dictionary[self.suit]

    def __repr__(self):
        helping_dictionary = {'clubs': 'c', 'diamonds': 'd', 'hearts': 'h',  'spades': 's'}

        return self.value + helping_dictionary[self.suit]

    def __eq__(self,other):
        return self.value == other.value and self.suit == other.suit

    def __lt__(self,other):
        helping_dictionary = {'7': 7, '8': 8,' 9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        return helping_dictionary[self.value] < helping_dictionary[other.value] 

    @staticmethod
    def validate_values(value,suit):
        correct_values = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        correct_suits = ['clubs','diamonds','hearts','spades']

        if not isinstance(value,str):
            raise TypeError('Wrong input - value must be of string type!')
        elif not isinstance(suit,str):
            raise TypeError('Wrong input - suit must be of string type!')
        elif value not in correct_values:
            raise AssertionError('Incorrect value!')
        elif suit not in correct_suits:
            raise AssertionError('Incorrect suit!')


def main():
    pass

if __name__ == '__main__':
    main()