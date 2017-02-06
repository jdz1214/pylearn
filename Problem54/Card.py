class Card:
	def __init__(self, cardstring):
		value = cardstring[0]
		suit = cardstring[1]
		self.values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
		self.suits = ['H', 'D', 'S', 'C']
		if str(value).upper() in self.values:
			self.value = str(value).upper()
		if suit.upper() in self.suits:
			self.suit = suit.upper()

	def __eq__(self, other):
		"""Override the default Equals behavior. Disregards suits."""
		if isinstance(other, self.__class__):
			return self.getvalueindex() == other.getvalueindex()
		return False

	def __ne__(self, other):
		"""Define a non-equality test"""
		return not self.__eq__(other)

	def __gt__(self, other):
		"""Overrides default greater-than comparator"""
		if isinstance(other, self.__class__):
			return self.getvalueindex() > other.getvalueindex()

	def __lt__(self, other):
		"""Overrides default less-than comparator"""
		if isinstance(other, self.__class__):
			return self.getvalueindex() < other.getvalueindex()

	def getvalue(self):
		return self.value

	def getvalueindex(self):
		return self.values.index(self.value)

	def getsuit(self):
		return self.suit

	def getvalueslist(self):
		return self.values

	def getsuitslist(self):
		return self.suits
