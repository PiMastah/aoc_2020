my_file = open("input.txt", "r")
content_list = my_file.read().split(',')

LIMIT = 30 * 1000 * 1000
LIMIT_part1 = 2020

sequence = []
turn = 0

last_indices = {}

for x in content_list:
	sequence.append(int(x))
	last_indices[int(x)] = (0, turn)
	turn += 1

while turn < LIMIT:
	last_num = sequence[turn-1]
	i = last_indices[last_num][1] if last_num in last_indices else 0
	j = last_indices[last_num][0] if last_num in last_indices else 0
	if i == 0 or (j == 0 and i == turn -1 and last_num != 0):
		number = 0
	else:
		last_index = turn - i + j
		number = turn - last_index

	if number in last_indices:
		last_indices[number] = (last_indices[number][1], turn)
	else:
		last_indices[number] = (0, turn)
	sequence.append(number)

	turn += 1

	if turn == LIMIT_part1:
		print("PART 1: {}".format(number))

print("PART 2: {}".format(sequence[-1]))
