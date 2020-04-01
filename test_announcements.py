from announcements import Announcements
from card import Card
from magic_strings import *
import unittest

class TestGroupingOfCardsByValue(unittest.TestCase):

    def test_when_there_are_cards_of_all_values(self):

        announced=Announcements([Card(seven,diamonds),Card(eight,diamonds),Card(nine,diamonds),Card(queen,diamonds),Card(ten,diamonds),Card(jack,diamonds),Card(king,diamonds),Card(ace,diamonds)])
        
        result = announced.group_cards_by_value()
        expected = {seven: [Card(seven,diamonds)], eight: [Card(eight,diamonds)], nine: [Card(nine,diamonds)], ten: [Card(ten,diamonds)], jack: [Card(jack,diamonds)], queen: [Card(queen,diamonds)], king: [Card(king,diamonds)], ace: [Card(ace,diamonds)]}

        self.assertEqual(result,expected,'Dicts of lists are equal')

    def test_when_there_are_cards_of_only_some_values(self):

        announced=Announcements([Card(seven,diamonds),Card(nine,spades),Card(nine,diamonds),Card(queen,diamonds),Card(queen,hearts),Card(jack,diamonds),Card(king,diamonds),Card(ace,diamonds)])
        
        result = announced.group_cards_by_value()
        expected = {seven: [Card(seven,diamonds)], nine: [Card(nine,diamonds),Card(nine,spades)], jack: [Card(jack,diamonds)], queen: [Card(queen,diamonds),Card(queen,hearts)], king: [Card(king,diamonds)], ace: [Card(ace,diamonds)]}

        self.assertEqual(result,expected,'Dicts of lists are equal')

class TestGroupingOfCardsBySuits(unittest.TestCase):

    def test_when_there_are_cards_of_all_four_suits(self):

        announced=Announcements([Card(jack,diamonds),Card(seven,clubs),Card(nine,diamonds),Card(king,clubs),Card(queen,hearts),Card(ten,hearts),Card(ten,spades),Card(eight,clubs)])
        
        result = announced.group_cards_by_suit()
        expected = {'c':[Card(seven,clubs),Card(eight,clubs),Card(king,clubs)],'d':[Card(nine,diamonds),Card(jack,diamonds)],'h':[Card(ten,hearts),Card(queen,hearts)],'s':[Card(ten,spades)]}
        
        self.assertEqual(result,expected,'Dicts of lists are equal')

    def test_when_there_are_cards_of_three_suits(self):

        announced=Announcements([Card(jack,diamonds),Card(seven,clubs),Card(nine,diamonds),Card(king,clubs),Card(queen,hearts),Card(ten,hearts),Card(ten,diamonds),Card(eight,clubs)])
        
        result = announced.group_cards_by_suit()
        expected = {'c':[Card(seven,clubs),Card(eight,clubs),Card(king,clubs)],'d':[Card(nine,diamonds),Card(ten,diamonds),Card(jack,diamonds)],'h':[Card(ten,hearts),Card(queen,hearts)]}
        
        self.assertEqual(result,expected,'Dicts of lists are equal')

    def test_when_there_are_cards_of_two_suits(self):

        announced=Announcements([Card(jack,diamonds),Card(seven,diamonds),Card(nine,diamonds),Card(king,diamonds),Card(queen,hearts),Card(ten,hearts),Card(eight,hearts),Card(ace,hearts)])
        
        result = announced.group_cards_by_suit()
        expected = {'d':[Card(seven,diamonds),Card(nine,diamonds),Card(jack,diamonds),Card(king,diamonds)],'h':[Card(eight,hearts),Card(ten,hearts),Card(queen,hearts),Card(ace,hearts)]}
        
        self.assertEqual(result,expected,'Lists of lists are equal')

    def test_when_there_are_cards_of_one_suit(self):

        announced=Announcements([Card(ace,diamonds),Card(seven,diamonds),Card(nine,diamonds),Card(king,diamonds),Card(queen,diamonds),Card(jack,diamonds),Card(ten,diamonds),Card(eight,diamonds)])
        result = announced.group_cards_by_suit()
        expected = {'d':[Card(seven,diamonds),Card(eight,diamonds),Card(nine,diamonds),Card(ten,diamonds),Card(jack,diamonds),Card(queen,diamonds),Card(king,diamonds),Card(ace,diamonds)]}
        
        self.assertEqual(result,expected,'Lists of lists are equal')

class TestGetNConsecutive(unittest.TestCase):

    def test_3_consecutive_in_list_of_four_consecutive_cards(self):

        test_list = [Card(seven,diamonds),Card(eight,diamonds),Card(nine,diamonds),Card(ten,diamonds)]
        announced=Announcements([])
        result=announced.get_n_consecutive(test_list,1)

        expected = [Card(eight,diamonds),Card(nine,diamonds),Card(ten,diamonds)]

        self.assertEqual(result,expected,'Lists are equal')

    def test_3_consecutive_in_list_of_three_consecutive_cards(self):

        test_list = [Card(eight,diamonds),Card(nine,diamonds),Card(ten,diamonds)]
        announced=Announcements([])
        result=announced.get_n_consecutive(test_list,1)

        expected = [Card(eight,diamonds),Card(nine,diamonds),Card(ten,diamonds)]

        self.assertEqual(result,expected,'Lists are equal')

    def test_3_consecutive_in_list_of_two_consecutive_cards(self):

        test_list = [Card(seven,diamonds),Card(eight,diamonds)]
        announced=Announcements([])
        result=announced.get_n_consecutive(test_list,1)

        expected = []

        self.assertEqual(result,expected,'Lists are equal')

class TestFindingConsecutiveCards(unittest.TestCase):

    def test_finding_consecutive_cards_when_there_are_no_consecutive_cards(self):

        announced=Announcements([Card(jack,diamonds),Card(queen,hearts),Card(nine,spades),Card(king,clubs),Card(eight,diamonds),Card(nine,hearts),Card(ten,spades),Card(seven,spades)])
        announced.find_consecutive_cards()

        result_announced_announcements = announced.getAnnouncedannouncements()
        result_repr_of_announcements = announced.getRepresentationOfannouncements()

        self.assertEqual(result_announced_announcements,[])
        self.assertEqual(result_repr_of_announcements,[])

    def test_finding_consecutive_cards_when_there_is_a_tierce(self):

        announced=Announcements([Card(jack,diamonds),Card(queen,diamonds),Card(nine,spades),Card(king,clubs),Card(eight,diamonds),Card(nine,hearts),Card(ten,diamonds),Card(seven,spades)])
        announced.find_consecutive_cards()

        result_announced_announcements = announced.getAnnouncedannouncements()
        result_repr_of_announcements = announced.getRepresentationOfannouncements()

        expected_announcements = [tierce]
        expected_representation = [[Card(ten,diamonds),Card(jack,diamonds),Card(queen,diamonds)]]

        self.assertEqual(result_announced_announcements,expected_announcements)
        self.assertEqual(result_repr_of_announcements,expected_representation)

    def test_finding_consecutive_cards_when_there_is_a_quarte(self):

        announced=Announcements([Card(jack,diamonds),Card(queen,diamonds),Card(nine,diamonds),Card(king,clubs),Card(eight,hearts),Card(nine,hearts),Card(ten,diamonds),Card(seven,spades)])
        announced.find_consecutive_cards()

        result_announced_announcements = announced.getAnnouncedannouncements()
        result_repr_of_announcements = announced.getRepresentationOfannouncements()

        expected_announcements = [quarte]
        expected_representation = [[Card(nine,diamonds),Card(ten,diamonds),Card(jack,diamonds),Card(queen,diamonds)]]

        self.assertEqual(result_announced_announcements,expected_announcements)
        self.assertEqual(result_repr_of_announcements,expected_representation)

    def test_finding_consecutive_cards_when_there_is_a_quinte(self):

        announced=Announcements([Card(jack,diamonds),Card(queen,diamonds),Card(nine,diamonds),Card(king,diamonds),Card(eight,hearts),Card(nine,hearts),Card(ten,diamonds),Card(seven,spades)])
        announced.find_consecutive_cards()

        result_announced_announcements = announced.getAnnouncedannouncements()
        result_repr_of_announcements = announced.getRepresentationOfannouncements()

        expected_announcements = [quinte]
        expected_representation = [[Card(nine,diamonds),Card(ten,diamonds),Card(jack,diamonds),Card(queen,diamonds),Card(king,diamonds)]]

        self.assertEqual(result_announced_announcements,expected_announcements)
        self.assertEqual(result_repr_of_announcements,expected_representation)

    def test_if_finding_consecutive_cards_when_there_are_two_quintes_gets_higher_quinte(self):

        announced=Announcements([Card(jack,diamonds),Card(queen,diamonds),Card(nine,diamonds),Card(king,diamonds),Card(eight,hearts),Card(nine,hearts),Card(ten,diamonds),Card(ace,diamonds)])
        announced.find_consecutive_cards()

        result_announced_announcements = announced.getAnnouncedannouncements()
        result_repr_of_announcements = announced.getRepresentationOfannouncements()

        expected_announcements = [quinte]
        expected_representation = [[Card(ten,diamonds),Card(jack,diamonds),Card(queen,diamonds),Card(king,diamonds),Card(ace,diamonds)]]

        self.assertEqual(result_announced_announcements,expected_announcements)
        self.assertEqual(result_repr_of_announcements,expected_representation)

    def test_finding_consecutive_cards_when_there_are_two_tierces(self):

        announced=Announcements([Card(jack,diamonds),Card(queen,diamonds),Card(nine,hearts),Card(king,diamonds),Card(eight,hearts),Card(seven,hearts),Card(ten,clubs),Card(seven,spades)])
        announced.find_consecutive_cards()

        result_announced_announcements = announced.getAnnouncedannouncements()
        result_repr_of_announcements = announced.getRepresentationOfannouncements()

        expected_announcements = [tierce,tierce]
        expected_representation = [[Card(seven,hearts),Card(eight,hearts),Card(nine,hearts)],[Card(jack,diamonds),Card(queen,diamonds),Card(king,diamonds)]]

        self.assertEqual(result_announced_announcements,expected_announcements)
        self.assertEqual(result_repr_of_announcements,expected_representation)

    def test_finding_consecutive_cards_when_there_are_tierce_and_quarte(self):

        announced=Announcements([Card(jack,diamonds),Card(queen,diamonds),Card(ten,diamonds),Card(king,diamonds),Card(eight,hearts),Card(nine,hearts),Card(ten,clubs),Card(seven,hearts)])
        announced.find_consecutive_cards()

        result_announced_announcements = announced.getAnnouncedannouncements()
        result_repr_of_announcements = announced.getRepresentationOfannouncements()

        expected_announcements = [tierce,quarte]
        expected_representation = [[Card(seven,hearts),Card(eight,hearts),Card(nine,hearts)],[Card(ten,diamonds),Card(jack,diamonds),Card(queen,diamonds),Card(king,diamonds)]]

        self.assertEqual(result_announced_announcements,expected_announcements)
        self.assertEqual(result_repr_of_announcements,expected_representation)


    def test_finding_consecutive_cards_when_there_are_tierce_and_quinte(self):

        announced=Announcements([Card(seven,diamonds),Card(eight,diamonds),Card(nine,diamonds),Card(queen,diamonds),Card(ten,diamonds),Card(jack,diamonds),Card(king,diamonds),Card(ace,diamonds)])
        announced.find_consecutive_cards()

        result_announced_announcements = announced.getAnnouncedannouncements()
        result_repr_of_announcements = announced.getRepresentationOfannouncements()

        expected_announcements = [quinte,tierce]
        expected_representation = [[Card(ten,diamonds),Card(jack,diamonds),Card(queen,diamonds),Card(king,diamonds),Card(ace,diamonds)],[Card(seven,diamonds),Card(eight,diamonds),Card(nine,diamonds)]]

        self.assertEqual(result_announced_announcements,expected_announcements)
        self.assertEqual(result_repr_of_announcements,expected_representation)

    def test_finding_consecutive_cards_when_there_are_two_quartes(self):

        announced=Announcements([Card(seven,diamonds),Card(eight,diamonds),Card(nine,diamonds),Card(queen,hearts),Card(ten,diamonds),Card(jack,hearts),Card(king,hearts),Card(ace,hearts)])
        announced.find_consecutive_cards()

        result_announced_announcements = announced.getAnnouncedannouncements()
        result_repr_of_announcements = announced.getRepresentationOfannouncements()

        expected_announcements = [quarte,quarte]
        expected_representation = [[Card(seven,diamonds),Card(eight,diamonds),Card(nine,diamonds),Card(ten,diamonds)],[Card(jack,hearts),Card(queen,hearts),Card(king,hearts),Card(ace,hearts)]]

        self.assertEqual(result_announced_announcements,expected_announcements)
        self.assertEqual(result_repr_of_announcements,expected_representation)


class TestBelote(unittest.TestCase):
    
    def test_belote_announcement_with_announce_noTrumps(self):
        announced=Announcements([Card(jack,diamonds),Card(queen,diamonds),Card(nine,diamonds),Card(king,diamonds),Card(ten,diamonds),Card(ten,hearts),Card(ten,spades),Card(seven,spades)])
        
        result=announced.find_belotes(no_trumps)

        self.assertEqual(result,None)


    def test_belote_announcement_with_announce_allTrumps(self):
        announced=Announcements([Card(queen,diamonds),Card(king,clubs),Card(king,diamonds),Card(queen,clubs),Card(ten,clubs),Card(ten,hearts),Card(ten,spades),Card(ten,diamonds)])

        result=announced.find_belotes(all_trumps)

        self.assertEqual(result,[[Card(queen,clubs),Card(king,clubs)],[Card(queen,diamonds),Card(king,diamonds)]])

    def test_belote_announcement_with_announce_allTrumps_with_no_belote(self):
        announced=Announcements([Card(queen,clubs),Card(king,spades),Card(king,diamonds),Card(queen,hearts),Card(ten,clubs),Card(ten,hearts),Card(ten,spades),Card(ten,diamonds)])

        result=announced.find_belotes(all_trumps)

        self.assertEqual(result,[])

    def test_belote_announcement_with_announce_clubs(self):
        announced=Announcements([Card(queen,clubs),Card(king,clubs),Card(king,diamonds),Card(queen,hearts),Card(ten,clubs),Card(ten,hearts),Card(ten,spades),Card(ten,diamonds)])

        result=announced.find_belotes(clubs)

        self.assertEqual(result,[[Card(queen,clubs),Card(king,clubs)]])

    def test_belote_announcement_with_announce_with_different_of_clubs(self):
        announced=Announcements([Card(queen,clubs),Card(king,hearts),Card(king,diamonds),Card(queen,hearts),Card(ten,clubs),Card(ten,hearts),Card(ten,spades),Card(ten,diamonds)])

        result=announced.find_belotes(clubs)

        self.assertEqual(result,[])

    def test_belote_announcement_with_announce_hearts(self):
        announced=Announcements([Card(queen,clubs),Card(king,hearts),Card(king,diamonds),Card(queen,hearts),Card(ten,clubs),Card(ten,hearts),Card(ten,spades),Card(ten,diamonds)])

        result=announced.find_belotes(hearts)

        self.assertEqual(result,[[Card(queen,hearts),Card(king,hearts)]])

    def test_belote_announcement_with_announce_diamonds(self):
        announced=Announcements([Card(queen,diamonds),Card(king,hearts),Card(king,diamonds),Card(queen,hearts),Card(ten,clubs),Card(ten,hearts),Card(ten,spades),Card(ten,diamonds)])

        result=announced.find_belotes(diamonds)

        self.assertEqual(result,[[Card(queen,diamonds),Card(king,diamonds)]])

    def test_belote_announcement_with_announce_spades(self):
        announced=Announcements([Card(queen,spades),Card(king,spades),Card(king,diamonds),Card(queen,hearts),Card(ten,clubs),Card(ten,hearts),Card(ten,spades),Card(ten,diamonds)])

        result=announced.find_belotes(spades)

        self.assertEqual(result,[[Card(queen,spades),Card(king,spades)]])


class ТestCarreFinder(unittest.TestCase):

    def test_if_it_find_one_count_of_carre_in_front_of_cards(self):
        announced=Announcements([Card(jack,clubs),Card(jack,hearts),Card(jack,diamonds),Card(jack,spades),Card(queen,hearts),Card(king,diamonds),Card(ten,spades),Card(ace,spades)])

        result=announced.find_carres()

        self.assertEqual(result,[[Card(jack,clubs),Card(jack,diamonds),Card(jack,hearts),Card(jack,spades)]])

    def test_if_it_find_two_of_count_of_carre(self):
        announced=Announcements([Card(jack,clubs),Card(jack,hearts),Card(jack,diamonds),Card(jack,spades),Card(queen,hearts),Card(queen,diamonds),Card(queen,clubs),Card(queen,spades)])
        
        result=announced.find_carres()
        
        self.assertEqual(result,[[Card(jack,clubs),Card(jack,diamonds),Card(jack,hearts),Card(jack,spades)],[Card(queen,clubs),Card(queen,diamonds),Card(queen,hearts),Card(queen,spades)]])    

    def test_if_there_is_no_carre(self):
        announced=Announcements([Card(queen,diamonds),Card(king,clubs),Card(king,diamonds),Card(queen,clubs),Card(ten,clubs),Card(eight,hearts),Card(seven,spades),Card(jack,diamonds)])

        result=announced.find_carres()
        
        self.assertEqual(result,[]) 

    def test_if_it_find_carre_of_8(self):
        announced=Announcements([Card(queen,diamonds),Card(king,clubs),Card(king,diamonds),Card(queen,clubs),Card(eight,clubs),Card(eight,hearts),Card(eight,spades),Card(eight,diamonds)])

        result=announced.find_carres()
        
        self.assertEqual(result,[]) 

class TestCheckerForCardInCarreAndAnnouncement(unittest.TestCase):

    def test_when_a_card_is_in_a_carre_and_tierce(self):
        announced=Announcements([Card(seven,diamonds),Card(eight,diamonds),Card(nine,diamonds),Card(queen,diamonds),Card(nine,spades),Card(nine,hearts),Card(nine,clubs),Card(ace,diamonds)])
        
        announced.find_carres()
        announced.find_consecutive_cards()
        announced.check_card_in_carre_and_announcement()

        result_announced_announcements = announced.getAnnouncedannouncements()
        result_repr_of_announcements = announced.getRepresentationOfannouncements()

        expected_announcements = [carre]
        expected_representation = [[Card(nine,clubs),Card(nine,diamonds),Card(nine,hearts),Card(nine,spades)]]

        self.assertEqual(result_announced_announcements,expected_announcements)
        self.assertEqual(result_repr_of_announcements,expected_representation)

    def test_when_a_card_is_in_a_carre_and_belote(self):
        announced=Announcements([Card(seven,diamonds),Card(eight,diamonds),Card(ten,diamonds),Card(queen,diamonds),Card(queen,spades),Card(queen,hearts),Card(queen,clubs),Card(king,clubs)])
        
        announced.find_carres()
        announced.find_consecutive_cards()
        announced.find_belotes(all_trumps)
        announced.check_card_in_carre_and_announcement()

        result_announced_announcements = announced.getAnnouncedannouncements()
        result_repr_of_announcements = announced.getRepresentationOfannouncements()

        expected_announcements = [carre,belote]
        expected_representation = [[Card(queen,clubs),Card(queen,diamonds),Card(queen,hearts),Card(queen,spades)],[Card(queen,clubs),Card(king,clubs)]]

        self.assertEqual(result_announced_announcements,expected_announcements)
        self.assertEqual(result_repr_of_announcements,expected_representation)



class ТestgetAnnouncedAnnouncements(unittest.TestCase):
    
    def test_get_Announced_one_belote_find(self):
        announced=Announcements([Card(queen,diamonds),Card(king,hearts),Card(king,diamonds),Card(queen,clubs),Card(eight,clubs),Card(eight,hearts),Card(eight,spades),Card(eight,diamonds)])

        announced.find_belotes(all_trumps)
        result=announced.getAnnouncedannouncements()

        self.assertEqual(result,[belote])

    def test_get_Announced_two_belote_find(self):

        announced=Announcements([Card(queen,diamonds),Card(king,clubs),Card(king,diamonds),Card(queen,clubs),Card(eight,clubs),Card(eight,hearts),Card(eight,spades),Card(eight,diamonds)])

        announced.find_belotes(all_trumps)
        result=announced.getAnnouncedannouncements()

        self.assertEqual(result,[belote,belote])

    def test_get_Announced_no_belote_find(self):
        announced=Announcements([Card(queen,diamonds),Card(king,clubs),Card(king,diamonds),Card(queen,clubs),Card(eight,clubs),Card(eight,hearts),Card(eight,spades),Card(eight,diamonds)])

        announced.find_belotes(no_trumps)
        result=announced.getAnnouncedannouncements()

        self.assertEqual(result,[])

    def test_get_Announced_two_belotes_and_carre(self):
        announced=Announcements([Card(queen,diamonds),Card(king,clubs),Card(king,diamonds),Card(queen,clubs),Card(ten,clubs),Card(ten,hearts),Card(ten,spades),Card(ten,diamonds)])

        announced.find_belotes(all_trumps)
        announced.find_carres()
        result=announced.getAnnouncedannouncements()

        self.assertEqual(result,[belote,belote,carre])

    def test_get_Announced_tierce_belotes_and_carre(self):
        announced=Announcements([Card(queen,diamonds),Card(king,clubs),Card(king,diamonds),Card(queen,clubs),Card(seven,clubs),Card(eight,clubs),Card(nine,clubs),Card(ten,diamonds)])

        announced.find_belotes(all_trumps)
        announced.find_carres()
        announced.find_consecutive_cards()
        result=announced.getAnnouncedannouncements()

        self.assertEqual(result,[belote,belote,tierce])

    def test_get_Announced_carre(self):
        announced=Announcements([Card(eight,diamonds),Card(jack,diamonds),Card(ace,diamonds),Card(queen,clubs),Card(ten,clubs),Card(ten,hearts),Card(ten,diamonds),Card(ten,spades)])

        announced.find_belotes(all_trumps)
        announced.find_carres()
        announced.find_consecutive_cards()
        result=announced.getAnnouncedannouncements()

        self.assertEqual(result,[carre])

class ТestGetRepresentationOfAnnouncements(unittest.TestCase):
    
    def test_get_Representation_tierce_and_two_belotes(self):
        announced=Announcements([Card(queen,diamonds),Card(king,clubs),Card(king,diamonds),Card(queen,clubs),Card(seven,clubs),Card(eight,clubs),Card(nine,clubs),Card(ten,diamonds)])

        announced.find_belotes(all_trumps)
        announced.find_carres()
        announced.find_consecutive_cards()
        result=announced.getRepresentationOfannouncements()

        self.assertEqual(result,[[Card(queen,clubs),Card(king,clubs)],[Card(queen,diamonds),Card(king,diamonds)],[Card(seven,clubs),Card(eight,clubs),Card(nine,clubs)]])

    def test_get_Representation_tierce_and_quinte(self):
        announced=Announcements([Card(seven,diamonds),Card(eight,diamonds),Card(nine,diamonds),Card(queen,diamonds),Card(ten,diamonds),Card(jack,diamonds),Card(king,diamonds),Card(ace,diamonds)])

        announced.find_consecutive_cards()
        result=announced.getRepresentationOfannouncements()

        self.assertEqual(result,[[Card(ten,diamonds),Card(jack,diamonds),Card(queen,diamonds),Card(king,diamonds),Card(ace,diamonds)],[Card(seven,diamonds),Card(eight,diamonds),Card(nine,diamonds)]])

    def test_get_Representation_belote_representation(self):
        announced=Announcements([Card(seven,clubs),Card(eight,clubs),Card(nine,diamonds),Card(queen,diamonds),Card(ten,hearts),Card(jack,hearts),Card(king,diamonds),Card(ace,diamonds)])

        announced.find_belotes(all_trumps)
        result=announced.getRepresentationOfannouncements()
        
        self.assertEqual(result,[[Card(queen,diamonds),Card(king,diamonds)]])


if __name__=='__main__':
    unittest.main()