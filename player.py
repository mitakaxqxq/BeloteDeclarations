class Player:

    def __init__(self,name):
        self.validate_name(name)

        self.__name = name
        self.__hand = []
        self.__declarations = []

    def get_name(self):
        return self.__name

    def set_declarations(self,declarations):
        self.__declarations = declarations

    def set_hand(self,cards):
        if len(cards) != 8:
            raise ValueError('You must add exactly eight cards!')
        else:
            self.__cards = cards

    def get_hand(self):
        return self.__cards

    def __eq__(self,other):
        return self.__name == other.__name

    @staticmethod
    def validate_name(name):
        if not isinstance(name,str):
            raise TypeError('Player name must be of string type!')
