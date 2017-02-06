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
		return [card.getvalue() for card in self.cards]

	def __get_valset(self):
		return set(self.__getvals())

	def __getvalindices(self):
		return [card.getvalueindex() for card in self.cards]

	def __getsuits(self):
		return {card.getsuit() for card in self.cards}

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
		return self.all_same_suit() and all(val in self.__getvals() for val in ['T', 'J', 'Q', 'K', 'A'])

	def straight_flush(self):
		return self.all_same_suit() and self.straight()

	def four_of_a_kind(self):
		return len(self.__get_valset()) == 2

	def full_house(self):
		return self.three_of_a_kind() and len(self.__get_valset()) == 2

	def flush(self):
		return self.all_same_suit()

	def straight(self):
		valindices = sorted(self.__getvalindices())
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
		return len(self.__get_valset()) == 3

	def one_pair(self):
		return len(self.__get_valset()) == 4

	def high_card(self):
		return max(self.cards, key=lambda c: c.getvalueindex())

	def rank_high_card(self):
		valset = self.__get_valset()
		if self.get_rank() in ['High Card', 'Straight Flush', 'Flush']:
			return self.high_card()

		elif self.get_rank() == 'Four of a Kind':
			fourval = ''
			count = 0
			for val in valset:
				for card in self.cards:
					if card.getvalue() == val:
						count += 1
				if count == 4:
					fourval = val
			return (card for card in self.cards if card.getvalue() == fourval)

		elif self.get_rank() in ['Full House', 'Three of a Kind']:
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

		elif self.get_rank() == 'Two Pairs':
			maxvalindex = 0
			for val in valset:
				if len([card.getvalue() for card in self.cards if card.getvalue() == val]) == 2:
					if maxvalindex < Card.getvalueindex(val):
						maxvalindex = Card.getvalueindex(val)
			return (card for card in self.cards if card.getvalueindex() == maxvalindex)

		elif self.get_rank() == 'One Pair':
			for val in valset:
				if len([card.getvalue() for card in self.cards if card.getvalue() == val]) == 2:
					for card in self.cards:
						if card.getvalue() == val:
							return card

	def all_same_suit(self):
		return len(set(card.getsuit() for card in self.cards)) == 1
