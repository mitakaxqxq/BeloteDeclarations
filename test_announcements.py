from declarations import Announcements
import unittest


class TestBelote(unittest.TestCase):
	def test_belote_announcement_with_announce_noTrums(self):
		announcements=Announcements(['Qs','Ks'])

		result=Announcements.announce_belote(announcements,noTrums=True)
		print(result)

		self.assertEqual(result,'')

	def test_belote_announcement_with_announce_allTrums(self):
		announcements=Announcements(['Qs','Ks','7c','8h','Ad','Js','10s'])

		result=Announcements.announce_belote(announcements,allTrums=True)

		self.assertEqual(result,'belote')

	def test_belote_announcement_with_announce_allTrums_with_no_belote(self):
		announcements=Announcements(['Qs','Kh'])

		result=Announcements.announce_belote(announcements,allTrums=True)

		self.assertEqual(result,'')

	def test_belote_announcement_with_announce_clubs(self):
		announcements=Announcements(['Qc','Kc'])

		result=Announcements.announce_belote(announcements,clubs=True)

		self.assertEqual(result,'belote')

	def test_belote_announcement_with_announce_with_different_of_clubs(self):
		announcements=Announcements(['Qh','Kh'])

		result=Announcements.announce_belote(announcements,allTrums=False,clubs=True)

		self.assertEqual(result,'')

	def test_belote_announcement_with_announce_hearts(self):
		announcements=Announcements(['Qh','Kh'])

		result=Announcements.announce_belote(announcements,hearts=True)

		self.assertEqual(result,'belote')
	def test_belote_announcement_with_announce_diamonds(self):
		announcements=Announcements(['Qd','Kd'])

		result=Announcements.announce_belote(announcements,diamonds=True)

		self.assertEqual(result,'belote')
	def test_belote_announcement_with_announce_spades(self):
		announcements=Announcements(['Qs','Ks'])

		result=Announcements.announce_belote(announcements,spades=True)

		self.assertEqual(result,'belote')

class testConsecutiveCardsFindFunction(unittest.TestCase):
	def test_if_it_is_noTrums_case(self):
		announcements=Announcements(['7s','8s', '9h'])

		result=Announcements.find_consecutive_cards(announcements,noTrums=True)

		self.assertEqual(result,[],'they are')

class TestConsecutiveCards(unittest.TestCase):

	def test_for_sort_by_ranks(self):

		announcements=Announcements(['7s','8s', '9h'])

		result=Announcements.sort_cards_by_ranks(announcements)

		self.assertEqual(result,['9h','8s','7s'])

	def test_for_sort_by_ranks_with_two_values(self):
		announcements=Announcements(['7s','8s'])

		result=Announcements.sort_cards_by_ranks(announcements)

		self.assertEqual(result,['7s','8s'])

	def test_sort_by_rank_eight_with_diffent_value(self):
		announcements=Announcements(['8s','9s','10s','Qh','Kh','Qs','Ks'])

		result=Announcements.sort_cards_by_ranks(announcements)

		self.assertEqual(result,['Qh','Kh','10s','8s','9s','Qs','Ks'])


	def test_sort_by_value_two_with_same_value(self):
		announcements=Announcements(['7s','7s'])

		result=Announcements.sort_cards_by_value(announcements)

		self.assertEqual(result,['7s','7s'])

	def test_sort_by_value_two_with_diffent_value(self):
		announcements=Announcements(['7s','8s'])

		result=Announcements.sort_cards_by_value(announcements)

		self.assertEqual(result,['7s','8s'])


	def test_sort_by_value_two_with_diffent_value(self):
		announcements=Announcements(['7s','8h'])

		result=Announcements.sort_cards_by_value(announcements)

		self.assertEqual(result,['7s','8h'])


	def test_sort_by_value_eight_with_diffent_value(self):
		announcements=Announcements(['8s','9s','10s','Qh','Kh','Qs','Ks'])

		result=Announcements.sort_cards_by_value(announcements)

		self.assertEqual(result,['8s','9s','10s','Qh','Qs','Kh','Ks'])

	def test_sort_cards_by_ranks_and_values_function(self):
		announcements=Announcements(['8s','9s','10s','Qh','Kh','Qs','Ks'])

		result=Announcements.sort_cards_by_rank_and_value(announcements)

		self.assertEqual(result,['Qh','Kh','8s','9s','10s','Qs','Ks'])

	def test_if_there_is_one_triece(self):
		announcements=Announcements(['7d','8d','9d','10h','Jc','7s','8h','9s'])

		result=Announcements.find_consecutive_cards(announcements)
		
		self.assertEqual(result,[['7d','8d','9d']])

	def test_if_there_is_one_quarte(self):
		announcements=Announcements(['7d','8d','9d','10d','Jc','7s','8h','9s'])

		result=Announcements.find_consecutive_cards(announcements)
		
		self.assertEqual(result,[['7d','8d','9d','10d']])

	def test_if_there_is_one_quinte(self):
		announcements=Announcements(['7d','8d','9d','10d','Jd','7s','8h','9s'])

		result=Announcements.find_consecutive_cards(announcements)
		
		self.assertEqual(result,[['7d','8d','9d','10d','Jd']])

	def test_if_there_is_one_quinte_and_tierce(self):
		announcements=Announcements(['7d','8d','9d','10d','Jd','7s','8s','9s'])

		result=Announcements.find_consecutive_cards(announcements)
		
		self.assertEqual(result,[['7d','8d','9d','10d','Jd'],['7s','8s','9s']])

	def test_if_there_is_two_tiercies(self):
		announcements=Announcements(['7d','8d','9d','10h','Jh','7s','8s','9s'])

		result=Announcements.find_consecutive_cards(announcements)
		
		self.assertEqual(result,[['7d','8d','9d'],['7s','8s','9s']])

	def test_if_there_is_quarte_and_tierce(self):
		announcements=Announcements(['7d','8d','9d','10d','Jh','7s','8s','9s'])

		result=Announcements.find_consecutive_cards(announcements)
		
		self.assertEqual(result,[['7d','8d','9d','10d'],['7s','8s','9s']])

	def test_if_there_is_quarte_and_tierce(self):
		announcements=Announcements(['8s','9s','10s','Qh','Kh','Qs','Ks'])

		result=Announcements.find_consecutive_cards(announcements)
		
		self.assertEqual(result,[['8s','9s','10s']])


	def test_if_there_is_no_consecutive_cards(self):
		announcements=Announcements(['7d','8c','9c','10d','Jh','7s','8h','9s'])

		result=Announcements.find_consecutive_cards(announcements)
		
		self.assertEqual(result,[])



class testCarreFinder(unittest.TestCase):

	def test_if_it_find_one_count_of_carre_in_front_of_cards(self):
		announcements=Announcements(['Js','Jd','Jh','Qs','Jc','Qc','Kh','Ad'])

		result=Announcements.carre_find_function(announcements)
		
		self.assertEqual(result,[['Js','Jd','Jh','Jc']])	

	def test_if_it_find_two_of_count_of_carre(self):
		announcements=Announcements(['Js','Jd','Jh','Qs','Jc','Qc','Qh','Qd'])

		result=Announcements.carre_find_function(announcements)
		
		self.assertEqual(result,[['Js','Jd','Jh','Jc'],['Qs','Qc','Qh','Qd']])	

	def test_if_there_is_no_carre(self):
		announcements=Announcements(['8s','7d','10h','10s','9c','Ac','Ah','Kd'])

		result=Announcements.carre_find_function(announcements)
		
		self.assertEqual(result,[])	

	def test_if_it_find_carre_in_the_middle_of_cards(self):
		announcements=Announcements(['Js','Jd','Jh','10s','Jc','7c','Ah','Kd'])

		result=Announcements.carre_find_function(announcements)
		
		self.assertEqual(result,[['Jh','Js','Jc','Jd']])	






if __name__=='__main__':
	unittest.main()