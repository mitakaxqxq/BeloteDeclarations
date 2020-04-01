from deck import Deck
from card import Card
from magic_strings import *

class Announcements:

    def __init__(self,cards):
        self.cards=cards
        self.announced_announcements=[]
        self.repr_of_announcements=[]

    def __str__(self):
        return f'{self.announced}'

    def __eq__(self,other):
        return self.cards==other.cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def getAnnouncedannouncements(self):
        return self.announced_announcements

    def getRepresentationOfannouncements(self):
        return self.repr_of_announcements

    def find_belotes(self,announcement):
        if announcement == no_trumps:
            return

        dict_of_lists = self.group_cards_by_suit()
        list_of_belotes = []
        
        for key in dict_of_lists.keys():
            list_of_cards = [elem for elem in dict_of_lists[key] if elem.get_value() == queen or elem.get_value() == king]
            if announcement == all_trumps:
                if len(list_of_cards) == 2:
                    self.announced_announcements.append(belote)
                    self.repr_of_announcements.append(list_of_cards)
                    list_of_belotes.append(list_of_cards)
            else:
                if len(list_of_cards) == 2 and list_of_cards[0].get_suit() == helping_dictionary_of_value_representation[announcement]:
                    self.announced_announcements.append(belote)
                    self.repr_of_announcements.append(list_of_cards)
                    list_of_belotes.append(list_of_cards)
        return list_of_belotes

    def group_cards_by_value(self):
        dict_of_cards = {}     
        for card in sorted(self.cards):
            if card.get_value() in dict_of_cards.keys():
                dict_of_cards[card.get_value()].append(card)
            else:
                dict_of_cards[card.get_value()] = [card]
        return dict_of_cards

    def group_cards_by_suit(self):
        dict_of_cards = {}
        for card in sorted(self.cards):
            if card.get_suit() in dict_of_cards.keys():
                dict_of_cards[card.get_suit()].append(card)
            else:
                dict_of_cards[card.get_suit()] = [card]
        return dict_of_cards

    def get_n_consecutive(self,new_list,n):      
        flag = False
        index = len(new_list)-1
        num_of_tierces = 0

        while index >= 0:
            card1_value = new_list[index].get_value()
            card2_value = new_list[index-1].get_value()
            card3_value = new_list[index-2].get_value()
            
            if helping_dictionary_of_values[card1_value] - 1 == helping_dictionary_of_values[card2_value] and helping_dictionary_of_values[card2_value] - 1 == helping_dictionary_of_values[card3_value]:
                num_of_tierces += 1
            else:
                num_of_tierces = 0
            if num_of_tierces == n:
                flag = True
                break
            index -= 1
        
        if flag == False:
            return []
        else:
            return new_list[index-2:index+num_of_tierces]

    def get_consecutive_cards(self,list_of_cards,i):
        result = []     
        while i >= 1:
            result = self.get_n_consecutive(list_of_cards,i)
            if result != [] and len(result) >=3 and len(result) <=5:
                break
            i -= 1
        return result

    def find_consecutive_cards(self):
        dict_of_cards = self.group_cards_by_suit()
        for key in dict_of_cards.keys():
            if len(dict_of_cards[key]) < 3:
                continue
            
            list_of_cards = sorted(dict_of_cards[key])
            i = 8
            result = self.get_consecutive_cards(list_of_cards,i)
            
            if result == []:
                continue
            
            self.repr_of_announcements.append(result)
            self.announced_announcements.append(lengths_of_announcements[len(result)])
            
            list_of_cards = [x for x in list_of_cards if x not in result]
            dict_of_cards[key] = list_of_cards

            if len(dict_of_cards[key]) < 3:
                continue
            
            i = 8-len(result)
            result = self.get_consecutive_cards(list_of_cards,i)

            if result == []:
                continue
            
            self.repr_of_announcements.append(result)            
            self.announced_announcements.append(lengths_of_announcements[len(result)])
            list_of_cards = [x for x in list_of_cards if x not in result]
            dict_of_cards[key] = list_of_cards

    def find_carres(self):
        grouped_cards=self.group_cards_by_value()
        result=[grouped_cards.get(x) for x in grouped_cards if x!= seven and x!=eight and len(grouped_cards.get(x))==4]
        i=0
        while i<len(result):
            self.repr_of_announcements.append(result[i])
            self.announced_announcements.append(carre)
            i=i+1

        return result

    def check_card_in_carre_and_announcement(self):
        if carre in self.getAnnouncedannouncements():
            list_of_announcements = self.getRepresentationOfannouncements()
            
            for elem in list_of_announcements:
                if elem[0].get_value()==elem[1].get_value():
                    list_of_carres = elem
                    break
            
            carre_value = list_of_carres[0].get_value()
            flag = False

            for announcement in self.getRepresentationOfannouncements():
                for card in announcement:
                    if carre_value == card.get_value() and announcement != list_of_carres and len(announcement) > 2:
                        flag = True
                        break

                if flag == True:
                    if len(announcement) == 3:
                        self.announced_announcements.remove(tierce)
                    elif len(announcement) == 4:
                        self.announced_announcements.remove(quarte)
                    elif len(announcement) == 5:
                        self.announced_announcements.remove(quinte)
                    self.repr_of_announcements.remove(announcement)

def main():
    pass

if __name__=='__main__':
    main()