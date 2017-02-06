from Problem54.Card import Card
from Problem54.Hand import Hand


def main():
	load()


def load():
	with open("p054_poker.txt", 'r') as f:
		lines = f.readlines()
	execute(lines)


def execute(lines):
	p1wins = 0
	p2wins = 0

	for line in lines:
		line = line.strip()
		cardstrings = line.strip().split(' ')
		cards = []

		for cs in cardstrings:
			# print(cs)
			cards.append(Card(cs))
		if len(cards) != 10:
			print("Problem found. length was ", len(cards))
		elif len(cards) == 10:
			p1 = Hand(cards[0], cards[1], cards[2], cards[3], cards[4])
			p2 = Hand(cards[5], cards[6], cards[7], cards[8], cards[9])

			if p1.get_rank() == 'Flush':
				print(line, '   p1 rank: ', p1.get_rank(), ' p2 rank: ', p2.get_rank(),
				            ' p1 indices: ', p1.high_card().getvalueindex(), ' p2 indices: ', p2.high_card().getvalueindex(), ' p1wins: ', (p1 > p2))

			if p1 > p2:
				p1wins += 1
			elif p2 > p1:
				p2wins += 1
			else:
				print(line, 'p1 rank: ', p1.get_rank(), ' p2 rank: ', p2.get_rank(),
				            ' p1 rank index: ', p1.get_rank_index(), ' p2 rank index: ', p2.get_rank_index(), ' p1wins: ', (p1 > p2), ' p2wins: ', ())
	print('Player 1 wins ', p1wins)
	print('Player 2 wins ', p2wins)


main()
