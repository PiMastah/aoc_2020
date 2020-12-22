my_file = open("input.txt", "r")
content_list = my_file.read()
player1_string, player2_string = content_list.split('\n\n')

def play_round(deck1, deck2):
	card1 = deck1.pop(0)
	card2 = deck2.pop(0)

	if card1 > card2:
		deck1.append(card1)
		deck1.append(card2)
	else:
		deck2.append(card2)
		deck2.append(card1)

	return deck1, deck2

def play_game(deck1, deck2):
	while len(deck1) > 0 and len(deck2) > 0:
		deck1, deck2 = play_round(deck1, deck2)

	winner_cards = deck1

	if len(deck1) == 0:
		winner_cards = deck2

	return winner_cards

def build_state(deck1, deck2):
	set1 = '-'.join(['{}-{}'.format(i, c) for i, c in enumerate(deck1)])
	set2 = '-'.join(['{}-{}'.format(i, c) for i, c in enumerate(deck2)])

	return (set1, set2)

def play_game_r(deck1, deck2):
	seen_sets = set()

	player_1_win = True

	while len(deck1) > 0 and len(deck2) > 0:
		state = build_state(deck1, deck2)

		if state in seen_sets:
			return deck1, player_1_win
		else:
			seen_sets.add(state)
		deck1, deck2 = play_round_r(deck1, deck2)

	winner_cards = deck1

	if len(deck1) == 0:
		player_1_win = False
		winner_cards = deck2

	return winner_cards, player_1_win

def play_round_r(deck1, deck2):
	card1 = deck1.pop(0)
	card2 = deck2.pop(0)

	if len(deck1) >= card1 and len(deck2) >= card2:
		_, player_1_win = play_game_r(deck1[:card1], deck2[:card2])

		if player_1_win:
			deck1.append(card1)
			deck1.append(card2)
		else:
			deck2.append(card2)
			deck2.append(card1)
	elif card1 > card2:
		deck1.append(card1)
		deck1.append(card2)
	else:
		deck2.append(card2)
		deck2.append(card1)

	return deck1, deck2

player1_cards = list(map(lambda x: int(x), player1_string.split('\n')[1:]))
player2_cards = list(map(lambda x: int(x), player2_string.split('\n')[1:]))

winner_cards = play_game(player1_cards, player2_cards)

p = 0

for i, c in enumerate(winner_cards):
	p += winner_cards[-i-1] * (i+1)

print("PART 1: {}".format(p))

player1_cards = list(map(lambda x: int(x), player1_string.split('\n')[1:]))
player2_cards = list(map(lambda x: int(x), player2_string.split('\n')[1:]))

winner_cards, _ = play_game_r(player1_cards, player2_cards)

p = 0

for i, c in enumerate(winner_cards):
	p += winner_cards[-i-1] * (i+1)

print("PART 2: {}".format(p))
