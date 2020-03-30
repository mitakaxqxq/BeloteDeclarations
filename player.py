from announcements import Announcements

class Player:

    def __init__(self,name):
        self.validate_name(name)

        self.__name = name
        self.__hand = []
        self.__announcements = Announcements(self.__hand)
    def get_name(self):
        return self.__name

    def set_announcements(self,announcements):
        self.__announcements = Announcements(announcements)
        self.__announcements.find_consecutive_cards()
        self.__announcements.carre_find_function()
        self.__announcements.check_card_in_two_announcements()

    def get_belotes(self,contract):
        self.__announcements.announce_belote(contract)

    def set_hand(self,cards):
        if len(cards) != 8:
            raise ValueError('You must add exactly eight cards!')
        else:
            self.__hand = cards
            self.set_announcements(cards)

    def get_hand(self):
        return self.__hand

    def __eq__(self,other):
        return self.__name == other.__name

    @staticmethod
    def validate_name(name):
        if not isinstance(name,str):
            raise TypeError('Player name must be of string type!')

    def get_announced_announcements(self):
        return self.__announcements.getAnnouncedannouncements()

    def get_announcements_representation(self):
        return self.__announcements.getRepresentationOfannouncements()

def main():
    pass

if __name__ == '__main__':
    main()