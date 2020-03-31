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

    def find_belote_cards(self):
        helping_dictionary = {'c': 'clubs','d': 'diamonds','h': 'hearts','s': 'spades'}
        
        list_of_belotes_in_desk=[]
        list_of_found_cuples=[]
        
        for card in self.cards:
            
            value=card.get_value()
            suit=card.get_suit()
            
            if value=='Q':
                
                other_half=Card('K',helping_dictionary.get(suit))
                
                if other_half in self.cards:          
                    
                    list_of_found_cuples.append(card)
                    list_of_found_cuples.append(other_half)
                    list_of_belotes_in_desk.append(list_of_found_cuples)
                    
                    list_of_found_cuples=[]

        return list_of_belotes_in_desk

    def announce_belote(self,announcement):
        lists=Announcements.find_belote_cards(self)
        
        string=''
        
        if announcement == 'no trumps':
            return ''
        
        elif announcement == 'all trumps':
            len_of_list=len(lists)
            
            i=0
            
            while i<len_of_list:
                string='belote'
                
                self.announced_announcements.append(string)
                self.repr_of_announcements.append(lists[i])
                
                i=i+1
        elif announcement == 'clubs':
            belote=[Card('Q','clubs'),Card('K','clubs')]
            
            if belote in lists:
                
                string='belote'
                
                self.announced_announcements.append(string)
                self.repr_of_announcements.append(belote)
        
        elif announcement=='hearts':
            
            belote=[Card('Q','hearts'),Card('K','hearts')]
            
            if belote in lists:
                string='belote'
                
                self.announced_announcements.append(string)
                self.repr_of_announcements.append(belote)
        
        elif announcement=='diamonds':
            
            belote=[Card('Q','diamonds'),Card('K','diamonds')]
            
            if belote in lists:
                string='belote'
                
                self.announced_announcements.append(string)
                self.repr_of_announcements.append(belote)
        
        elif announcement=='spades':
            
            belote=[Card('Q','spades'),Card('K','spades')]
            
            if belote in lists:
                string='belote'
                
                self.announced_announcements.append(string)
                self.repr_of_announcements.append(belote)
        
        return string

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
        helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        flag = False
        
        index = len(new_list)-1
        
        num_of_tierces = 0

        while index >= 0:
            card1_value = new_list[index].get_value()
            card2_value = new_list[index-1].get_value()
            card3_value = new_list[index-2].get_value()
            
            if helping_dictionary[card1_value] - 1 == helping_dictionary[card2_value] and helping_dictionary[card2_value] - 1 == helping_dictionary[card3_value]:
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
        result=[grouped_cards.get(x) for x in grouped_cards if x!='7' and x!='8' and len(grouped_cards.get(x))==4]
        i=0
        while i<len(result):
            self.repr_of_announcements.append(result[i])
            self.announced_announcements.append('carre')
            i=i+1
        return result

    def check_card_in_two_announcements(self):
        if 'carre' in self.getAnnouncedannouncements():
            list_of_announcements = self.getRepresentationOfannouncements()
            
            for elem in list_of_announcements:
                if elem[0].get_value()==elem[1].get_value():
                    list_of_carres = elem
                    break
            
            carre_value = list_of_carres[0].get_value()
            flag = False

            for announcement in self.getRepresentationOfannouncements():
                for card in announcement:
                    if carre_value == card.get_value() and announcement != list_of_carres:
                        flag = True
                        break

                if flag == True:
                    if len(announcement) == 3:
                        self.announced_announcements.remove('tierce')
                    elif len(announcement) == 4:
                        self.announced_announcements.remove('quarte')
                    elif len(announcement) == 5:
                        self.announced_announcements.remove('quinte')
                    self.repr_of_announcements.remove(announcement)


def main():
    announced=Announcements([Card('7','diamonds'),Card('8','diamonds'),Card('9','diamonds'),Card('Q','diamonds'),Card('10','diamonds'),Card('J','diamonds'),Card('K','diamonds'),Card('A','diamonds')])
    print(announced.find_consecutive_cards())
    print(announced.getRepresentationOfannouncements())
    print(announced.getAnnouncedannouncements())
    print(announced.find_carres())
    print('===============================================')
    announced=Announcements([Card('7','diamonds'),Card('7','spades'),Card('7','hearts'),Card('7','clubs'),Card('10','spades'),Card('10','hearts'),Card('10','diamonds'),Card('10','clubs')])
    print(announced.find_consecutive_cards())
    print(announced.find_carres())
    print(announced.getRepresentationOfannouncements())
    print(announced.getAnnouncedannouncements())

if __name__=='__main__':
    main()