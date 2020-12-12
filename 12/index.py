my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

facing = 'E'

dirs = {
	'N': (0,-1),
	'E': (1,0),
	'S': (0,1),
	'W': (-1,0),
}

x = 0
y = 0

for e in content_list:
	command = e[0]
	i = int(e[1:])
	if command == 'F':
		command = facing
	if command in dirs:
		x += i * dirs[command][0]
		y += i * dirs[command][1]
	elif command in ['L', 'R']:
		ds = list(dirs.keys())
		index = ds.index(facing)
		steps = int(i / 90)
		if command == 'L':
			steps = -steps
		facing = ds[(index + steps + 4) % 4]

print("PART 1: {}".format(abs(x) + abs(y)))

x = 0
y = 0

wx = 10
wy = -1

for e in content_list:
	command = e[0]
	i = int(e[1:])
	if command == 'F':
		x += i * (wx)
		y += i * (wy)
	if command in dirs:
		wx += i * dirs[command][0]
		wy += i * dirs[command][1]
	elif command in ['L', 'R']:
		if command == 'L':
			i = 360 - i
		i = (i + 360) % 360

		if i == 90:
			t = wx
			wx = -wy
			wy = t
		if i == 180:
			wx = -wx
			wy = -wy
		if i == 270:
			t = wx
			wx = wy
			wy = -t

print("PART 2: {}".format(abs(x) + abs(y)))