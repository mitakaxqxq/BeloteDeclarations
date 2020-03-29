from announcements import Announcements
from card import Card
import unittest


class TestRemovingThreeConsecutiveCards(unittest.TestCase):

	def test_when_there_is_tierce_and_no_cards_before_the_tierce_and_some_cards_after_it(self):

		announced=Announcements([Card('J','diamonds'),Card('7','spades'),Card('9','diamonds'),Card('K','diamonds'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('10','clubs')])
		grouped = announced.group_cards()[1]
		self.assertEqual(announced.remove_three_consecutive(grouped),[Card('K','diamonds')])
		
	def test_when_there_is_tierce_and_some_cards_before_the_tierce_and_after_it(self):

		announced=Announcements([Card('J','diamonds'),Card('7','diamonds'),Card('9','diamonds'),Card('K','diamonds'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('10','clubs')])
		grouped = announced.group_cards()[1]
		self.assertEqual(announced.remove_three_consecutive(grouped),[Card('7','diamonds'),Card('K','diamonds')])
		
	def test_when_there_is_tierce_and_some_cards_before_the_tierce_and_no_cards_after_it(self):

		announced=Announcements([Card('J','diamonds'),Card('7','diamonds'),Card('9','diamonds'),Card('K','spades'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('10','clubs')])
		grouped = announced.group_cards()[1]
		self.assertEqual(announced.remove_three_consecutive(grouped),[Card('7','diamonds')])

	def test_when_there_is_tierce_and_no_cards_before_and_after_it(self):

		announced=Announcements([Card('J','diamonds'),Card('7','spades'),Card('9','diamonds'),Card('K','spades'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('10','clubs')])
		grouped = announced.group_cards()[1]
		self.assertEqual(announced.remove_three_consecutive(grouped),[])
		
class TestRemovingFourConsecutiveCards(unittest.TestCase):
		
	def test_when_there_is_quarte_and_some_cards_before_the_quarte_and_after_it(self):

		announced=Announcements([Card('Q','diamonds'),Card('7','diamonds'),Card('9','diamonds'),Card('K','diamonds'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('8','diamonds')])
		grouped = announced.group_cards()[0]
		self.assertEqual(announced.remove_four_consecutive(grouped),[Card('Q','diamonds'),Card('K','diamonds')])
		
	def test_when_there_is_quarte_and_some_cards_before_the_quarte_and_no_cards_after_it(self):

		announced=Announcements([Card('Q','diamonds'),Card('7','diamonds'),Card('9','diamonds'),Card('K','spades'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('8','diamonds')])
		grouped = announced.group_cards()[0]
		self.assertEqual(announced.remove_four_consecutive(grouped),[Card('Q','diamonds')])

	def test_when_there_is_quarte_and_no_cards_before_the_quarte_and_some_after_it(self):

		announced=Announcements([Card('Q','spades'),Card('7','diamonds'),Card('9','diamonds'),Card('K','diamonds'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('8','diamonds')])
		grouped = announced.group_cards()[0]
		self.assertEqual(announced.remove_four_consecutive(grouped),[Card('K','diamonds')])
	
		
	def test_when_there_is_quarte_and_no_cards_before_the_quarte_and_after_it(self):

		announced=Announcements([Card('J','diamonds'),Card('7','spades'),Card('9','diamonds'),Card('Q','diamonds'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('10','clubs')])
		grouped = announced.group_cards()[1]
		self.assertEqual(announced.remove_four_consecutive(grouped),[])

class TestRemovingFiveConsecutiveCards(unittest.TestCase):
		
	def test_when_there_is_quinte_and_some_cards_after_it(self):

		announced=Announcements([Card('J','diamonds'),Card('7','diamonds'),Card('9','diamonds'),Card('K','diamonds'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('8','diamonds')])
		grouped = announced.group_cards()[0]
		self.assertEqual(announced.remove_five_consecutive(grouped),[Card('K','diamonds')])
		
	def test_when_there_is_quinte_and_some_cards_before_it(self):

		announced=Announcements([Card('J','diamonds'),Card('Q','diamonds'),Card('9','diamonds'),Card('K','diamonds'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('7','diamonds')])
		grouped = announced.group_cards()[0]
		self.assertEqual(announced.remove_five_consecutive(grouped),[Card('7','diamonds')])

	def test_when_there_is_quinte_and_no_cards_before_and_after_it(self):
		
		announced=Announcements([Card('J','diamonds'),Card('Q','diamonds'),Card('9','diamonds'),Card('K','diamonds'),Card('10','diamonds'),Card('10','hearts'),Card('10','spades'),Card('7','spades')])
		grouped = announced.group_cards()[0]
		self.assertEqual(announced.remove_five_consecutive(grouped),[])

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



class testCarreFinder(unittest.TestCase):

	def test_if_it_find_one_count_of_carre_in_front_of_cards(self):
		announced=Announcements([Card('J','clubs'),Card('J','hearts'),Card('J','diamonds'),Card('J','spades'),Card('Q','hearts'),Card('K','diamonds'),Card('10','spades'),Card('A','spades')])

		result=announced.carre_find_function()

		self.assertEqual(result,[[Card('J','hearts'),Card('J','diamonds'),Card('J','spades'),Card('J','clubs')]])



	def test_if_it_find_two_of_count_of_carre(self):
		announced=Announcements([Card('J','clubs'),Card('J','hearts'),Card('J','diamonds'),Card('J','spades'),Card('Q','hearts'),Card('Q','diamonds'),Card('Q','clubs'),Card('Q','spades')])
		result=announced.carre_find_function()
		self.assertEqual(result,[[Card('J','clubs'),Card('J','hearts'),Card('J','diamonds'),Card('J','spades')],[Card('Q','hearts'),Card('Q','diamonds'),Card('Q','clubs'),Card('Q','spades')]])
	


	def test_if_there_is_no_carre(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('10','clubs'),Card('8','hearts'),Card('7','spades'),Card('J','diamonds')])

		result=announced.carre_find_function()
		
		self.assertEqual(result,[])	

	def test_if_it_find_carre_of_8(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('8','clubs'),Card('8','hearts'),Card('8','spades'),Card('8','diamonds')])

		result=announced.carre_find_function()
		
		self.assertEqual(result,[])	

class testgetAnnouncedAnnouncements(unittest.TestCase):
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
		announced.carre_find_function()
		result=announced.getAnnouncedannouncements()

		self.assertEqual(result,['belote','belote','carre'])

	def test_get_Announced_tierce_belotes_and_carre(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('7','clubs'),Card('8','clubs'),Card('9','clubs'),Card('10','diamonds')])

		announced.announce_belote('all trumps')
		announced.carre_find_function()
		announced.find_consecutive_cards()
		result=announced.getAnnouncedannouncements()

		self.assertEqual(result,['belote','belote','tierce'])

	def test_get_Announced_carre(self):
		announced=Announcements([Card('8','diamonds'),Card('J','diamonds'),Card('A','diamonds'),Card('Q','clubs'),Card('10','clubs'),Card('10','hearts'),Card('10','diamonds'),Card('10','spades')])

		announced.announce_belote('all trumps')
		announced.carre_find_function()
		announced.find_consecutive_cards()
		result=announced.getAnnouncedannouncements()

		self.assertEqual(result,['carre'])



class testGetRepresentationOfAnnouncements(unittest.TestCase):
	def test_get_Representation_tierce_and_two_belotes(self):
		announced=Announcements([Card('Q','diamonds'),Card('K','clubs'),Card('K','diamonds'),Card('Q','clubs'),Card('7','clubs'),Card('8','clubs'),Card('9','clubs'),Card('10','diamonds')])

		announced.announce_belote('all trumps')
		announced.carre_find_function()
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