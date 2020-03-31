from announcements import Announcements
from card import Card
import unittest
class TestGroupingOfCards(unittest.TestCase):

	def test_when_there_are_cards_of_all_four_suits(self):

		announced=Announcements([Card('J','diamonds'),Card('7','clubs'),Card('9','diamonds'),Card('K','clubs'),Card('Q','hearts'),Card('10','hearts'),Card('10','spades'),Card('8','clubs')])
		
		result = announced.group_cards_by_suit()
		expected = {'c':[Card('7','clubs'),Card('8','clubs'),Card('K','clubs')],'d':[Card('9','diamonds'),Card('J','diamonds')],'h':[Card('10','hearts'),Card('Q','hearts')],'s':[Card('10','spades')]}
		
		self.assertEqual(result,expected,'Dicts of lists are equal')

	def test_when_there_are_cards_of_three_suits(self):

		announced=Announcements([Card('J','diamonds'),Card('7','clubs'),Card('9','diamonds'),Card('K','clubs'),Card('Q','hearts'),Card('10','hearts'),Card('10','diamonds'),Card('8','clubs')])
		
		result = announced.group_cards_by_suit()
		expected = {'c':[Card('7','clubs'),Card('8','clubs'),Card('K','clubs')],'d':[Card('9','diamonds'),Card('10','diamonds'),Card('J','diamonds')],'h':[Card('10','hearts'),Card('Q','hearts')]}
		
		self.assertEqual(result,expected,'Dicts of lists are equal')

	def test_when_there_are_cards_of_two_suits(self):

		announced=Announcements([Card('J','diamonds'),Card('7','diamonds'),Card('9','diamonds'),Card('K','diamonds'),Card('Q','hearts'),Card('10','hearts'),Card('8','hearts'),Card('A','hearts')])
		
		result = announced.group_cards_by_suit()
		expected = {'d':[Card('7','diamonds'),Card('9','diamonds'),Card('J','diamonds'),Card('K','diamonds')],'h':[Card('8','hearts'),Card('10','hearts'),Card('Q','hearts'),Card('A','hearts')]}
		
		self.assertEqual(result,expected,'Lists of lists are equal')

	def test_when_there_are_cards_of_one_suit(self):

		announced=Announcements([Card('A','diamonds'),Card('7','diamonds'),Card('9','diamonds'),Card('K','diamonds'),Card('Q','diamonds'),Card('J','diamonds'),Card('10','diamonds'),Card('8','diamonds')])
		result = announced.group_cards_by_suit()
		expected = {'d':[Card('7','diamonds'),Card('8','diamonds'),Card('9','diamonds'),Card('10','diamonds'),Card('J','diamonds'),Card('Q','diamonds'),Card('K','diamonds'),Card('A','diamonds')]}
		
		self.assertEqual(result,expected,'Lists of lists are equal')

class TestBelote(unittest.TestCase):
	def test_belote_announcement_with_announce_noTrums(self):
		announced=Announcements([Card('J','diamonds'),Card('Q','diamonds'),Card('9','diamonds'),Card('K','diamonds'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('7','spades')])
		result=announced.announce_belote('no trums')

		self.assertEqual(result,'')


	def test_belote_announcement_with_announce_allTrums(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('10','clubs'),Card('10','hearts'),Card('10','spades'),Card('10','diamonds')])

		result=announced.announce_belote('all trumps')

		self.assertEqual(result,'belote')

	def test_belote_announcement_with_announce_allTrums_with_no_belote(self):
		announced=Announcements([Card('Q','clubs'),Card('K','spades'),Card('K','diamonds'),Card('Q','hearts'),Card('10','clubs'),Card('10','hearts'),Card('10','spades'),Card('10','diamonds')])

		result=announced.announce_belote('all trumps')

		self.assertEqual(result,'')

	def test_belote_announcement_with_announce_clubs(self):
		announced=Announcements([Card('Q','clubs'),Card('K','clubs'),Card('K','diamonds'),Card('Q','hearts'),Card('10','clubs'),Card('10','hearts'),Card('10','spades'),Card('10','diamonds')])

		result=announced.announce_belote('clubs')

		self.assertEqual(result,'belote')

	def test_belote_announcement_with_announce_with_different_of_clubs(self):
		announced=Announcements([Card('Q','clubs'),Card('K','hearts'),Card('K','diamonds'),Card('Q','hearts'),Card('10','clubs'),Card('10','hearts'),Card('10','spades'),Card('10','diamonds')])

		result=announced.announce_belote('clubs')


		self.assertEqual(result,'')

	def test_belote_announcement_with_announce_hearts(self):
		announced=Announcements([Card('Q','clubs'),Card('K','hearts'),Card('K','diamonds'),Card('Q','hearts'),Card('10','clubs'),Card('10','hearts'),Card('10','spades'),Card('10','diamonds')])

		result=announced.announce_belote('hearts')


		self.assertEqual(result,'belote')
	def test_belote_announcement_with_announce_diamonds(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','hearts'),Card('K','diamonds'),Card('Q','hearts'),Card('10','clubs'),Card('10','hearts'),Card('10','spades'),Card('10','diamonds')])

		result=announced.announce_belote('diamonds')

		self.assertEqual(result,'belote')
	def test_belote_announcement_with_announce_spades(self):
		announced=Announcements([Card('Q','spades'),Card('K','spades'),Card('K','diamonds'),Card('Q','hearts'),Card('10','clubs'),Card('10','hearts'),Card('10','spades'),Card('10','diamonds')])

		result=announced.announce_belote('spades')


		self.assertEqual(result,'belote')

'''
class TestSortCards(unittest.TestCase):

	def test_for_sort_by_ranks(self):

		announced=Announcements([Card('7','clubs'),Card('8','clubs'),Card('9','clubs')])

		result=announced.sort_cards_by_ranks()

		self.assertEqual(result,[Card('7','clubs'),Card('8','clubs'),Card('9','clubs')])

	def test_for_sort_by_ranks_with_two_values(self):
		announced=Announcements([Card('7','clubs'),Card('8','clubs')])

		result=announced.sort_cards_by_ranks()

		self.assertEqual(result,[Card('7','clubs'),Card('8','clubs')])

	def test_sort_by_rank_eight_with_diffent_value(self):
		announced=Announcements([Card('7','clubs'),Card('8','clubs'),Card('9','hearts'),Card('8','diamonds'),Card('Q','hearts'),Card('K','diamonds'),Card('10','spades'),Card('A','spades')])

		result=announced.sort_cards_by_ranks()

		self.assertEqual(result,[Card('7','clubs'),Card('8','clubs'),Card('8','diamonds'),Card('K','diamonds'),Card('Q','hearts'),Card('9','hearts'),Card('10','spades'),Card('A','spades')])


	def test_sort_by_value_eight_with_diffent_value(self):
		announced=Announcements([Card('7','clubs'),Card('8','clubs'),Card('9','hearts'),Card('8','diamonds'),Card('Q','hearts'),Card('K','diamonds'),Card('10','spades'),Card('A','spades')])

		result=announced.sort_cards_by_value()

		self.assertEqual(result,[Card('7','clubs'),Card('8','clubs'),Card('8','diamonds'),Card('9','hearts'),Card('10','spades'),Card('Q','hearts'),Card('K','diamonds'),Card('A','spades')])


	def test_sort_cards_by_ranks_and_values_function(self):
		announced=Announcements([Card('7','clubs'),Card('8','clubs'),Card('9','hearts'),Card('8','diamonds'),Card('Q','hearts'),Card('K','diamonds'),Card('10','spades'),Card('A','spades')])

		result=announced.sort_cards_by_rank_and_value()

		self.assertEqual(result,[Card('7','clubs'),Card('8','clubs'),Card('8','diamonds'),Card('K','diamonds'),Card('9','hearts'),Card('Q','hearts'),Card('10','spades'),Card('A','spades')])

'''

class ТestCarreFinder(unittest.TestCase):

	def test_if_it_find_one_count_of_carre_in_front_of_cards(self):
		announced=Announcements([Card('J','clubs'),Card('J','hearts'),Card('J','diamonds'),Card('J','spades'),Card('Q','hearts'),Card('K','diamonds'),Card('10','spades'),Card('A','spades')])

		result=announced.find_carres()

		self.assertEqual(result,[[Card('J','clubs'),Card('J','diamonds'),Card('J','hearts'),Card('J','spades')]])



	def test_if_it_find_two_of_count_of_carre(self):
		announced=Announcements([Card('J','clubs'),Card('J','hearts'),Card('J','diamonds'),Card('J','spades'),Card('Q','hearts'),Card('Q','diamonds'),Card('Q','clubs'),Card('Q','spades')])
		result=announced.find_carres()
		self.assertEqual(result,[[Card('J','clubs'),Card('J','diamonds'),Card('J','hearts'),Card('J','spades')],[Card('Q','clubs'),Card('Q','diamonds'),Card('Q','hearts'),Card('Q','spades')]])
	


	def test_if_there_is_no_carre(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('10','clubs'),Card('8','hearts'),Card('7','spades'),Card('J','diamonds')])

		result=announced.find_carres()
		
		self.assertEqual(result,[])	

	def test_if_it_find_carre_of_8(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('8','clubs'),Card('8','hearts'),Card('8','spades'),Card('8','diamonds')])

		result=announced.find_carres()
		
		self.assertEqual(result,[])	


class ТestgetAnnouncedAnnouncements(unittest.TestCase):
	
	def test_get_Announced_one_belote_find(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','hearts'),Card('K','diamonds'),Card('Q','clubs'),Card('8','clubs'),Card('8','hearts'),Card('8','spades'),Card('8','diamonds')])

		announced.announce_belote('all trumps')
		result=announced.getAnnouncedannouncements()

		self.assertEqual(result,['belote'])

	def test_get_Announced_two_belote_find(self):

		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('8','clubs'),Card('8','hearts'),Card('8','spades'),Card('8','diamonds')])

		announced.announce_belote('all trumps')
		result=announced.getAnnouncedannouncements()

		self.assertEqual(result,['belote','belote'])

	def test_get_Announced_no_belote_find(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('8','clubs'),Card('8','hearts'),Card('8','spades'),Card('8','diamonds')])

		announced.announce_belote('no trumps')
		result=announced.getAnnouncedannouncements()

		self.assertEqual(result,[])

	def test_get_Announced_two_belotes_and_carre(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('10','clubs'),Card('10','hearts'),Card('10','spades'),Card('10','diamonds')])

		announced.announce_belote('all trumps')
		announced.find_carres()
		result=announced.getAnnouncedannouncements()

		self.assertEqual(result,['belote','belote','carre'])

	def test_get_Announced_tierce_belotes_and_carre(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('7','clubs'),Card('8','clubs'),Card('9','clubs'),Card('10','diamonds')])

		announced.announce_belote('all trumps')
		announced.find_carres()
		announced.find_consecutive_cards()
		result=announced.getAnnouncedannouncements()

		self.assertEqual(result,['belote','belote','tierce'])

	def test_get_Announced_carre(self):
		announced=Announcements([Card('8','diamonds'),Card('J','diamonds'),Card('A','diamonds'),Card('Q','clubs'),Card('10','clubs'),Card('10','hearts'),Card('10','diamonds'),Card('10','spades')])

		announced.announce_belote('all trumps')
		announced.find_carres()
		announced.find_consecutive_cards()
		result=announced.getAnnouncedannouncements()

		self.assertEqual(result,['carre'])

class ТestGetRepresentationOfAnnouncements(unittest.TestCase):
	
	def test_get_Representation_tierce_and_two_belotes(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('7','clubs'),Card('8','clubs'),Card('9','clubs'),Card('10','diamonds')])

		announced.announce_belote('all trumps')
		announced.find_carres()
		announced.find_consecutive_cards()
		result=announced.getRepresentationOfannouncements()

		self.assertEqual(result,[[Card('Q','diamonds'),Card('K','diamonds')],[Card('Q','clubs'),Card('K','clubs')],[Card('7','clubs'),Card('8','clubs'),Card('9','clubs')]])

	def test_get_Representation_tierce_and_quinte(self):
		announced=Announcements([Card('7','diamonds'),Card('8','diamonds'),Card('9','diamonds'),Card('Q','diamonds'),Card('10','diamonds'),Card('J','diamonds'),Card('K','diamonds'),Card('A','diamonds')])

		announced.find_consecutive_cards()
		result=announced.getRepresentationOfannouncements()

		self.assertEqual(result,[[Card('10','diamonds'),Card('J','diamonds'),Card('Q','diamonds'),Card('K','diamonds'),Card('A','diamonds')],[Card('7','diamonds'),Card('8','diamonds'),Card('9','diamonds')]])

	def test_get_Representation_belote_representation(self):
		announced=Announcements([Card('7','clubs'),Card('8','clubs'),Card('9','diamonds'),Card('Q','diamonds'),Card('10','hearts'),Card('J','hearts'),Card('K','diamonds'),Card('A','diamonds')])

		announced.announce_belote("all trumps")
		result=announced.getRepresentationOfannouncements()
		
		self.assertEqual(result,[[Card('Q','diamonds'),Card('K','diamonds')]])


if __name__=='__main__':
	unittest.main()