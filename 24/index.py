my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

def tokenize(s):
	l = list(s)
	tokens = []

	while len(l) > 0:
		c = l.pop(0)
		if c not in ['e', 'w']:
			c += l.pop(0)
		tokens.append(c)

	return tokens

def s_to_x_y(s):
	x = 0
	y = 0

	tokens = tokenize(s)

	for t in tokens:
		if t == 'e':
			x += 1
		if t == 'se':
			y += 1
		if t == 'sw':
			x -= 1
			y += 1
		if t == 'w':
			x -= 1
		if t == 'nw':
			y -= 1
		if t == 'ne':
			x += 1
			y -= 1

	return x, y

grid = {}

for l in content_list:
	x, y  = s_to_x_y(l)
	if (x, y) not in grid:
		grid[(x, y)] = 0
	grid[(x, y)] += 1

s = 0
dels = []

for c in grid:
	if grid[c] % 2 == 1:
		s += 1
	else:
		dels.append(c)

for c in dels:
	del grid[c]

print("PART 1: {}".format(s))

offsets = [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]

def neighbors(x, y):
	return [(x + o[0], y + o[1]) for o in offsets]

def flip(grid):
	new_grid = {}
	to_explore = [c for c in grid]
	explored = set()
	while len(to_explore) > 0:
		x, y = to_explore.pop(0)
		col = 'black' if (x, y) in grid else 'white'
		n = neighbors(x,y)
		c = 0
		for nb in n:
			if nb not in explored and nb not in to_explore and col == 'black':
				to_explore.append(nb)
			if nb in grid:
				c += 1

		if col == 'white' and c == 2 or col == 'black' and 0 < c and c <= 2:
			new_grid[(x, y)] = 1

		explored.add((x, y))

	return new_grid

for _ in range(100):
	grid = flip(grid)

print("PART 2: {}".format(len(grid)))