from deck import Deck
from card import Card

class Announcements:

	def __init__(self,Cards):
		self.Cards=Cards
		self.announced_declarations=[]
		self.repr_of_declarations=[]

	def __str__(self):
		return f'{self.announced}'

	def __eq__(self,other):
		return self.Cards==other.Cards

	def __len__(self):
		return len(self.Cards)

	def __getitem__(self, index):
		return self.Cards[index]

	def getAnnouncedDeclarations(self):
		return self.announced_declarations

	def getRepresentationOfDeclarations(self):
		return self.repr_of_declarations

	def find_belote_cards(self):
		list_of_belotes_in_desk=[]
		list_of_found_cuples=[]
		for card in self.Cards:
			value=card[0]
			suit=card[1]
			if value=='Q':
				other_half='K'+suit
				if other_half in self.Cards:
					list_of_found_cuples.append(card)
					list_of_found_cuples.append(other_half)
					list_of_belotes_in_desk.append(list_of_found_cuples)
		return list_of_belotes_in_desk



	def announce_belote(self,allTrums=False,noTrums=False,clubs=False,hearts=False,diamonds=False,spades=False):
		lists=Announcements.find_belote_cards(self)
		string=''
		if noTrums:
			return ''
		elif allTrums:
			len_of_list=len(lists)
			i=0
			while i<len_of_list:
				string='belote'
				self.announced_declarations.append(string)
				self.repr_of_declarations.append(lists[i])
				i=i+1
		elif clubs:
			belote=['Qc','Kc']
			if belote in lists:
				string='belote'
				self.announced_declarations.append(string)
				self.repr_of_declarations.append(belote)
		elif hearts:
			belote=['Qh','Kh']
			if belote in lists:
				string='belote'
				self.announced_declarations.append(string)
				self.repr_of_declarations.append(belote)
		elif diamonds:
			belote=['Qd','Kd']
			if belote in lists:
				string='belote'
				self.announced_declarations.append(string)
				self.repr_of_declarations.append(belote)
		elif spades:
			belote=['Qs','Ks']
			if belote in lists:
				string='belote'
				self.announced_declarations.append(string)
				self.repr_of_declarations.append(belote)
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
		new_list=self.Cards
		for i in range(0,len(new_list)-1):
			for j in range(i,len(new_list)):
				card1=new_list[i]
				card2=new_list[j]
				if len(card1)==2:
					suit_f=card1[1]
				if len(card1)==3:
					suit_f=card1[2]
				if len(card2)==2:
					suit_s=card2[1]
				if len(card2)==3:
					suit_s=card2[2]
				if helping_dictionary.get(suit_f)>helping_dictionary.get(suit_s):
					temp=new_list[i]
					new_list[i]=new_list[j]
					new_list[j]=temp
		return new_list

	def sort_cards_by_value(self):
		new_list=self.Cards
		for i in range(0,len(new_list)-1):
			for j in range(i,len(new_list)):
				card1=new_list[i]
				card2=new_list[j]
				if len(card1)==2:
					new_card1=Card(card1[0],Announcements.change_rank(card1[1]))
					suit_f=card1[1]
				if len(card1)==3:
					new_card1=Card(card1[0]+card1[1],Announcements.change_rank(card1[2]))
					suit_f=card1[2]
				if len(card2)==2:
					new_card2=Card(card2[0],Announcements.change_rank(card2[1]))
					suit_s=card2[1]
				if len(card2)==3:
					new_card2=Card(card2[0]+card2[1],Announcements.change_rank(card2[2]))
					suit_s=card2[2]
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
				if len(card1)==2:
					new_card1=Card(card1[0],Announcements.change_rank(card1[1]))
					suit_f=card1[1]
				if len(card1)==3:
					new_card1=Card(card1[0]+card1[1],Announcements.change_rank(card1[2]))
					suit_f=card1[2]
				if len(card2)==2:
					new_card2=Card(card2[0],Announcements.change_rank(card2[1]))
					suit_s=card2[1]
				if len(card2)==3:
					new_card2=Card(card2[0]+card2[1],Announcements.change_rank(card2[2]))
					suit_s=card2[2]
				if new_card2<new_card1 and suit_s==suit_f:
					temp=sorted_list[i]
					sorted_list[i]=sorted_list[j]
					sorted_list[j]=temp
		return sorted_list


	def find_consecutive_cards(self,allTrums=False,noTrums=False,clubs=False,hearts=False,diamonds=False,spades=False ):
		helping_dictionary = {'7': 7, '8': 8,'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
		count_of_tierce=0
		new_list=[]
		current_list=[]
		sorted_list=Announcements.sort_cards_by_rank_and_value(self)
		i=0
		while i<len(sorted_list)-1:
			card1=sorted_list[i]
			card2=sorted_list[i+1]
			if len(card1)==2:
				value1=card1[0]
				suit_f=card1[1]
			if len(card1)==3:
				value1=card1[0]+card1[1]
				suit_f=card1[2]
			if len(card2)==2:
				value2=card2[0]
				suit_s=card2[1]
			if len(card2)==3:
				value2=card2[0]+card2[1]
				suit_s=card2[2]
			if  suit_f==suit_s:
				if helping_dictionary.get(value1)+1==helping_dictionary.get(value2):
					current_list.append(card1)
				else:
					current_list.append(card1)
					if len(current_list)>2:
						new_list.append(current_list)
						self.repr_of_declarations.append(current_list)
						if len(current_list)==3:
							self.announced_declarations.append('tierce')
						if len(current_list)==4:
							self.announced_declarations.append('quarte')
						if len(current_list)==5:
							self.announced_declarations.append('quinte')
					current_list=[]
			else:
				current_list.append(card1)
				if len(current_list)>2:
					new_list.append(current_list)
					self.repr_of_declarations.append(current_list)
					if len(current_list)==3:
						self.announced_declarations.append('tierce')
					if len(current_list)==4:
						self.announced_declarations.append('quarte')
					if len(current_list)==5:
						self.announced_declarations.append('quinte')
				current_list=[]
			i=i+1
		current_list.append(card2)
		if len(current_list)>2:
			new_list.append(current_list)
			self.repr_of_declarations.append(current_list)
			if len(current_list)==3:
				self.announced_declarations.append('tierce')
			if len(current_list)==4:
				self.announced_declarations.append('quarte')
			if len(current_list)==5:
				self.announced_declarations.append('quinte')
		return new_list


	def carre_find_function(self,allTrums=False,noTrums=False,clubs=False,hearts=False,diamonds=False,spades=False ):
		list_find_carre_cards=[]
		new_list=[]
		count_of_carre=0
		sorted_array_by_rank=Announcements.sort_cards_by_value(self)
		if noTrums:
			return list_find_carre_cards
		i=0
		while i<len(sorted_array_by_rank)-3:
			card1=self[i]
			card2=self[i+1]
			card3=self[i+2]
			card4=self[i+3]
			if len(card1)==2:
				value1=card1[0]
			if len(card1)==3:
				value1=card1[0]+card1[1]
			if len(card2)==2:
				value2=card2[0]
			if len(card2)==3:
				value2=card2[0]+card2[1]
			if len(card3)==2:
				value3=card3[0]
			if len(card3)==3:
				value3=card3[0]+card3[1]
			if len(card4)==2:
				value4=card4[0]
			if len(card4)==3:
				value4=card4[0]+card4[1]
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
						self.announced_declarations.append('carre')
						self.repr_of_declarations.append(list_find_carre_cards)
						count_of_carre=0
						list_find_carre_cards=[]
			i=i+1
		if count_of_carre==1:
			new_list.append(list_find_carre_cards)
			self.announced_declarations.append('carre')
			self.repr_of_declarations.append(list_find_carre_cards)
		return new_list


def main():
	announced=Announcements(['7d','8d','9d','10d','Jd','Qd','8s','9s'])
	Announcements.find_consecutive_cards(announced)
	Announcements.announce_belote(announced)
	print(Announcements.getAnnouncedDeclarations(announced))
	print(Announcements.getRepresentationOfDeclarations(announced))

if __name__=='__main__':
	main()