from Problem54.Card import Card


class Hand:
	def __init__(self, card1: Card, card2: Card, card3: Card, card4: Card, card5: Card):
		self.ranks = ['High Card', 'One Pair', 'Two Pairs', 'Three of a Kind', 'Straight', 'Flush', 'Full House',
		              'Four of a Kind', 'Straight Flush', 'Royal Flush']
		self.card1 = card1
		self.card2 = card2
		self.card3 = card3
		self.card4 = card4
		self.card5 = card5
		self.cards = [self.card1, self.card2, self.card3, self.card4, self.card5]
		self.rank = self.ranks.index(self.__evaluaterank())

	def __lt__(self, other):
		if isinstance(other, self.__class__):
			if self.get_rank_index() == other.get_rank_index():
				if self.rank_high_card() == other.rank_high_card():
					return self.high_card() < other.high_card()
				else:
					return self.rank_high_card() < other.rank_high_card()
			else:
				return self.get_rank_index() < other.get_rank_index()

	def __gt__(self, other):
		if isinstance(other, self.__class__):
			if self.get_rank_index() == other.get_rank_index():
				if self.rank_high_card() == other.rank_high_card():
					return self.high_card() > other.high_card()
				else:
					return self.rank_high_card() > other.rank_high_card()
			else:
				return self.get_rank_index() > other.get_rank_index()

	def __getvals(self):
		vals = []
		for card in self.cards:
			vals.append(card.getvalue())
		return vals

	def __get_valset(self):
		return set(self.__getvals())

	def __getvalindices(self):
		valindices = []
		for card in self.cards:
			valindices.append(card.getvalueindex())
		return valindices

	def __getsuits(self):
		suits = set()
		for card in self.cards:
			suits.add(card.getsuit())
		return suits

	def __evaluaterank(self):
		if self.royal_flush():
			return 'Royal Flush'
		elif self.straight_flush():
			return 'Straight Flush'
		elif self.four_of_a_kind():
			return 'Four of a Kind'
		elif self.full_house():
			return 'Full House'
		elif self.flush():
			return 'Flush'
		elif self.straight():
			return 'Straight'
		elif self.three_of_a_kind():
			return 'Three of a Kind'
		elif self.two_pair():
			return 'Two Pairs'
		elif self.one_pair():
			return 'One Pair'
		else:
			return 'High Card'

	def get_rank(self):
		return self.ranks[self.rank]

	def get_rank_index(self):
		return self.rank

	def royal_flush(self):
		vals = self.__getvals()
		return self.all_same_suit() and 'T' in vals and 'J' in vals and 'Q' in vals and 'K' in vals and 'A' in vals

	def straight_flush(self):
		valindices = self.__getvalindices()
		valindices.sort()
		for i in range(0, len(valindices) - 1):
			if valindices[i] != valindices[i + 1] - 1:
				return False
		return self.all_same_suit()

	def four_of_a_kind(self):
		valset = self.__get_valset()
		return len(valset) == 2

	def full_house(self):
		if self.three_of_a_kind():
			valset = self.__get_valset()
			return len(valset) == 2
		return False

	def flush(self):
		return self.all_same_suit()

	def straight(self):
		valindices = self.__getvalindices()
		valindices.sort()
		for i in range(0, len(valindices) - 1):
			if valindices[i] != valindices[i + 1] - 1:
				return False
		return True

	def three_of_a_kind(self):
		valset = self.__get_valset()
		for val in valset:
			count = 0
			for card in self.cards:
				if card.getvalue() == val:
					count += 1
			if count == 3:
				return True
		return False

	def two_pair(self):
		valset = self.__get_valset()
		return len(valset) == 3

	def one_pair(self):
		valset = self.__get_valset()
		return len(valset) == 4

	def high_card(self):
		maxcard = self.card1
		for card in self.cards:
			if card.getvalueindex() > maxcard.getvalueindex():
				maxcard = card
		return maxcard

	def rank_high_card(self):
		if self.get_rank() == 'High Card' or self.get_rank() == 'Straight Flush' or self.get_rank() == 'Flush':
			return self.high_card()

		if self.get_rank() == 'Four of a Kind':
			valset = self.__get_valset()
			fourval = ''
			count = 0
			for val in valset:
				for card in self.cards:
					if card.getvalue() == val:
						count += 1
				if count == 4:
					fourval = val
			for card in self.cards:
				if card.getvalue() == fourval:
					return card

		if self.get_rank() == 'Full House' or self.get_rank() == 'Three of a Kind':
			valset = self.__get_valset()
			threeval = ''
			count = 0
			for val in valset:
				for card in self.cards:
					if card.getvalue() == val:
						count += 1
				if count == 3:
					threeval = val
			for card in self.cards:
				if card.getvalue() == threeval:
					return card

		if self.get_rank() == 'Two Pairs':
			valset = self.__get_valset()
			maxvalindex = 0
			for val in valset:
				valcount = 0
				for card in self.cards:
					if card.getvalue() == val:
						valcount += 1
				if valcount == 2:
					if maxvalindex < Card.getvalueindex(val):
						maxvalindex = Card.getvalueindex(val)
			for card in self.cards:
				if card.getvalueindex() == maxvalindex:
					return card

		if self.get_rank() == 'One Pair':
			valset = self.__get_valset()
			for val in valset:
				valcount = 0
				for card in self.cards:
					if card.getvalue() == val:
						valcount += 1
				if valcount == 2:
					for card in self.cards:
						if card.getvalue() == val:
							return card

	def all_same_suit(self):
		suits = []
		for card in self.cards:
			suits.append(card.getsuit())
		return len(set(suits)) == 1
