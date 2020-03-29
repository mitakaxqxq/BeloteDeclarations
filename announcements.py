from deck import Deck
from card import Card

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

    def change_rank(char):
        if char=='c':
            char='clubs'
        elif char=='d':
            char='diamonds'
        elif char=='h':
            char='hearts'
        elif char=='s':
            char='spades'
        return char

    def sort_cards_by_ranks(self):
        helping_dictionary = {'c': 1, 'd': 2, 'h': 3,  's': 4}
        new_list=self.cards
        for i in range(0,len(new_list)-1):
            for j in range(i,len(new_list)):
                card1=new_list[i]
                card2=new_list[j]
                suit_f=card1.get_suit()
                suit_s=card2.get_suit()
                if helping_dictionary.get(suit_f)>helping_dictionary.get(suit_s):
                    temp=new_list[i]
                    new_list[i]=new_list[j]
                    new_list[j]=temp
        return new_list

    def sort_cards_by_value(self):
        new_list=self.cards
        for i in range(0,len(new_list)-1):
            for j in range(i,len(new_list)):
                card1=new_list[i]
                card2=new_list[j]
                new_card1=Card(card1.get_value(),Announcements.change_rank(card1.get_suit()))
                new_card2=Card(card2.get_value(),Announcements.change_rank(card2.get_suit()))
                if new_card2<new_card1:
                    temp=new_list[i]
                    new_list[i]=new_list[j]
                    new_list[j]=temp
        return new_list

    def sort_cards_by_rank_and_value(self):
        sorted_cards_by_rank=Announcements.sort_cards_by_ranks(self)
        sorted_list=sorted_cards_by_rank
        for i in range(0,len(sorted_list)-1):
            for j in range(i,len(sorted_list)):
                card1=sorted_list[i]
                card2=sorted_list[j]
                new_card1=Card(card1.get_value(),Announcements.change_rank(card1.get_suit()))
                new_card2=Card(card2.get_value(),Announcements.change_rank(card2.get_suit()))
                suit_f=card1.get_suit()
                suit_s=card2.get_suit()
                if new_card2<new_card1 and suit_s==suit_f:
                    temp=sorted_list[i]
                    sorted_list[i]=sorted_list[j]
                    sorted_list[j]=temp
        return sorted_list

    def group_cards(self):
        list_of_lists = []
        new_list = []
        flag = False
        i = 0
        self.sort_cards_by_rank_and_value()
        while i < len(self.cards):
            while self.cards[i].get_suit() == self.cards[i+1].get_suit():
                new_list.append(self.cards[i])
                i += 1
                if i == len(self.cards)-1:
                    new_list.append(self.cards[i])
                    break
            if i == len(self.cards)-1:
                list_of_lists.append(new_list)
                break
            new_list.append(self.cards[i])
            list_of_lists.append(new_list)
            new_list = []
            i += 1
            if i >= len(self.cards)-1:
                new_list.append(self.cards[i])
                list_of_lists.append(new_list)
                break
        return list_of_lists

    def get_three_consecutive(self,new_list):
        helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        index = 0
        length = len(new_list)
        num_of_tierces = 0
        while index < length - 2:
            card1_value = new_list[index].get_value()
            card2_value = new_list[index+1].get_value()
            card3_value = new_list[index+2].get_value()
            if helping_dictionary[card1_value] + 1 == helping_dictionary[card2_value] and helping_dictionary[card2_value] + 1 == helping_dictionary[card3_value]:
                num_of_tierces += 1
            else:
                num_of_tierces = 0
            if num_of_tierces == 1:
                break
            index += 1
        return new_list[index:index+3]

    def get_four_consecutive(self,new_list):
        helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        index = 0
        length = len(new_list)
        num_of_tierces = 0
        while index < length - 2:
            card1_value = new_list[index].get_value()
            card2_value = new_list[index+1].get_value()
            card3_value = new_list[index+2].get_value()
            if helping_dictionary[card1_value] + 1 == helping_dictionary[card2_value] and helping_dictionary[card2_value] + 1 == helping_dictionary[card3_value]:
                num_of_tierces += 1
            else:
                num_of_tierces = 0
            if num_of_tierces == 2:
                break
            index += 1
        return new_list[index-1:index+3]

    def get_five_consecutive(self,new_list):
        helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        index = 0
        length = len(new_list)
        num_of_tierces = 0
        while index < length - 2:
            card1_value = new_list[index].get_value()
            card2_value = new_list[index+1].get_value()
            card3_value = new_list[index+2].get_value()
            if helping_dictionary[card1_value] + 1 == helping_dictionary[card2_value] and helping_dictionary[card2_value] + 1 == helping_dictionary[card3_value]:
                num_of_tierces += 1
            else:
                num_of_tierces = 0
            if num_of_tierces == 3:
                break
            index += 1
        return new_list[index-2:index+3]

    def remove_three_consecutive(self,new_list):
        helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        index = 0
        length = len(new_list)
        num_of_tierces = 0
        while index < length - 2:
            card1_value = new_list[index].get_value()
            card2_value = new_list[index+1].get_value()
            card3_value = new_list[index+2].get_value()
            if helping_dictionary[card1_value] + 1 == helping_dictionary[card2_value] and helping_dictionary[card2_value] + 1 == helping_dictionary[card3_value]:
                num_of_tierces += 1
            else:
                num_of_tierces = 0
            if num_of_tierces == 1:
                break
            index += 1
        return new_list[:index]+new_list[index+3:]

    def remove_four_consecutive(self,new_list):
        helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        index = 0
        length = len(new_list)
        num_of_tierces = 0
        while index < length - 2:
            card1_value = new_list[index].get_value()
            card2_value = new_list[index+1].get_value()
            card3_value = new_list[index+2].get_value()
            if helping_dictionary[card1_value] + 1 == helping_dictionary[card2_value] and helping_dictionary[card2_value] + 1 == helping_dictionary[card3_value]:
                num_of_tierces += 1
            else:
                num_of_tierces = 0
            if num_of_tierces == 2:
                break
            index += 1
        return new_list[:index-1]+new_list[index+3:]

    def remove_five_consecutive(self,new_list):
        helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        index = 0
        length = len(new_list)
        num_of_tierces = 0
        while index < length - 2:
            card1_value = new_list[index].get_value()
            card2_value = new_list[index+1].get_value()
            card3_value = new_list[index+2].get_value()
            if helping_dictionary[card1_value] + 1 == helping_dictionary[card2_value] and helping_dictionary[card2_value] + 1 == helping_dictionary[card3_value]:
                num_of_tierces += 1
            else:
                num_of_tierces = 0
            if num_of_tierces == 3:
                break
            index += 1
        return new_list[:index-2]+new_list[index+3:]

    def find_consecutive_tierces(self,new_list):
        helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        index = 0
        length = len(new_list)
        num_of_tierces = 0
        while index < length - 2:
            card1_value = new_list[index].get_value()
            card2_value = new_list[index+1].get_value()
            card3_value = new_list[index+2].get_value()

            if helping_dictionary[card1_value] + 1 == helping_dictionary[card2_value] and helping_dictionary[card2_value] + 1 == helping_dictionary[card3_value]:
                num_of_tierces += 1
            else:
                break
            if num_of_tierces >= 4:
                break
            index += 1
        return num_of_tierces

    def get_higher_quinte(self,new_list):
        helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        index = len(new_list)-1
        print(index)
        while index >= 4:
            card1_value = new_list[index].get_value()
            card2_value = new_list[index-1].get_value()
            card3_value = new_list[index-2].get_value()
            card4_value = new_list[index-3].get_value()
            card5_value = new_list[index-4].get_value()

            if helping_dictionary[card1_value] - 1 == helping_dictionary[card2_value] and helping_dictionary[card2_value] - 1 == helping_dictionary[card3_value] and helping_dictionary[card3_value] - 1 == helping_dictionary[card4_value] and helping_dictionary[card4_value] - 1 == helping_dictionary[card5_value]:
                return new_list[index-4:index+1]
            index -= 1

    def remove_higher_quinte(self,new_list):
        helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        helping_list = self.get_higher_quinte(new_list)

        list_without_quinte = []

        for element in new_list:
            if element in helping_list:
                continue
            else:
                list_without_quinte.append(element)

        return list_without_quinte

    def find_consecutive_cards(self):
        list_of_lists = self.group_cards()
        helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        
        for list_of_suits in list_of_lists:

            new_list = list_of_suits
            if len(new_list) < 3:
                continue

            result = self.find_consecutive_tierces(new_list)

            while result != 0:
                if result == 1:
                    self.repr_of_announcements.append(self.get_three_consecutive(new_list))
                    new_list = self.remove_three_consecutive(new_list)
                    self.announced_announcements.append('tierce')
                elif result == 2:
                    self.repr_of_announcements.append(self.get_four_consecutive(new_list))
                    new_list = self.remove_four_consecutive(new_list)
                    self.announced_announcements.append('quarte')
                elif result == 3:
                    self.repr_of_announcements.append(self.get_five_consecutive(new_list))
                    new_list = self.remove_five_consecutive(new_list)
                    self.announced_announcements.append('quinte')
                elif result == 4:
                    self.repr_of_announcements.append(self.get_higher_quinte(new_list))
                    new_list = self.remove_higher_quinte(new_list)
                    self.announced_announcements.append('quinte')
                
                if len(new_list) < 3:
                    break
                result = self.find_consecutive_tierces(new_list)

    def carre_find_function(self):
        list_find_carre_cards=[]
        new_list=[]
        count_of_carre=0
        sorted_array_by_rank=Announcements.sort_cards_by_value(self)
        i=0
        while i<len(sorted_array_by_rank)-3:
            card1=self[i]
            card2=self[i+1]
            card3=self[i+2]
            card4=self[i+3]
            value1=card1.get_value()
            value2=card2.get_value()
            value3=card3.get_value()
            value4=card4.get_value()
            if value1!='7' and value1!='8':
                if value1==value2 and value2==value3 and value3==value4:
                    count_of_carre+=1
                    list_find_carre_cards.append(card1)
                    list_find_carre_cards.append(card2)
                    list_find_carre_cards.append(card3)
                    list_find_carre_cards.append(card4)
                else:
                    if count_of_carre==1:
                        new_list.append(list_find_carre_cards)
                        self.announced_announcements.append('carre')
                        self.repr_of_announcements.append(list_find_carre_cards)
                        count_of_carre=0
                        list_find_carre_cards=[]
            i=i+1
        if count_of_carre==1:
            new_list.append(list_find_carre_cards)
            self.announced_announcements.append('carre')
            self.repr_of_announcements.append(list_find_carre_cards)
        return new_list

    def check_card_in_two_announcements(self):
        if 'carre' in self.getAnnouncedannouncements():
            list_of_carres = self.carre_find_function()[0]
            carre_value = list_of_carres[0].get_value()
            flag = False

            list_of_announcements = self.getRepresentationOfannouncements()
            for announcement in list_of_announcements:
                for card in announcement:
                    if carre_value == card.get_value():
                        flag = True
                        break
                if flag == True:
                    list_of_announcements.remove(announcement)
            return list_of_announcements


def main():

    #announced=Announcements([Card('7','diamonds'),Card('8','diamonds'),Card('9','diamonds'),Card('Q','diamonds'),Card('10','diamonds'),Card('J','diamonds'),Card('K','diamonds'),Card('A','diamonds')])

    announced=Announcements([Card('J','diamonds'),Card('K','diamonds'),Card('9','diamonds'),Card('Q','diamonds'),Card('10','clubs'),Card('10','hearts'),Card('10','spades'),Card('10','diamonds')])

    announced.sort_cards_by_rank_and_value()
    announced.find_consecutive_cards()

    print(announced.getRepresentationOfannouncements())
    print(announced.getAnnouncedannouncements())

    print(announced.carre_find_function())
    print(announced.getAnnouncedannouncements())
    print(announced.group_cards())
    print(announced.getRepresentationOfannouncements())
    print(announced.check_card_in_two_announcements())

    #announced=Announcements([Card('7','diamonds'),Card('8','diamonds'),Card('9','diamonds'),Card('Q','diamonds'),Card('10','diamonds'),Card('J','diamonds'),Card('K','diamonds'),Card('A','diamonds')])

    '''announced.find_consecutive_cards()

    print(announced.getRepresentationOfannouncements())
    print(announced.getAnnouncedannouncements())'''
if __name__=='__main__':
    main()