from magic_strings import *

class Card:

    def __init__(self,value,suit):
        self.validate_values(value,suit)

        self.__value = value
        self.__suit = suit

    def __str__(self):
        return self.__value + helping_dictionary_of_value_representation[self.__suit]

    def __repr__(self):
        return self.__value + helping_dictionary_of_value_representation[self.__suit]

    def __eq__(self,other):
        return self.__value == other.__value and self.__suit == other.__suit

    def __lt__(self,other):
        if self.get_value() == other.get_value():
            return helping_dictionary_of_suits[self.get_suit()] < helping_dictionary_of_suits[other.get_suit()]
        return helping_dictionary_of_values[self.get_value()] < helping_dictionary_of_values[other.get_value()]


    def get_value(self):
        return self.__value

    def get_suit(self):
        return helping_dictionary_of_value_representation[self.__suit]

    @staticmethod
    def validate_values(value,suit):
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