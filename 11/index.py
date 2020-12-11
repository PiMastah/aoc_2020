import itertools

my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

grid = [[i for i in x] for x in content_list]

max_y = len(grid)
max_x = len(grid[0])

offsets = list(itertools.product(range(-1, 2), range(-1, 2)))
offsets = offsets[:4] + offsets[5:]

def get_directional_neighbors(x, y, grid):
	coords = []
	for dx, dy in offsets:
		cx = x + dx
		cy = y + dy
		while cx >= 0 and cx < max_x and cy >= 0 and cy < max_y and grid[cy][cx] == '.':
			cx += dx
			cy += dy
		if cx >= 0 and cx < max_x and cy >= 0 and cy < max_y:
			coords.append((cx, cy))
	return coords

def step(grid, advanced=False):
	new_grid = []
	changes = 0
	for y, l in enumerate(grid):
		new_line = []
		new_grid.append(new_line)
		for x, c in enumerate(l):
			old_char = c
			new_char = c
			if old_char != '.':
				if advanced:
					neighbors = get_directional_neighbors(x, y, grid)
				else:
					neighbors = itertools.product(range(max(0, x-1), min(max_x, x+2)), range(max(0, y-1), min(max_y, y+2)))
				full_neighbors = len([1 for n in list(neighbors) if (n[0] != x or n[1] != y) and grid[n[1]][n[0]] == '#'])
				if old_char == 'L' and full_neighbors == 0:
					new_char = '#'
					changes += 1
				elif old_char == '#' and (not advanced and full_neighbors >= 4 or advanced and full_neighbors >= 5):
					new_char = 'L'
					changes += 1
			new_line.append(new_char)
	return new_grid, changes

changed = 1

while (changed > 0):
	grid, changed = step(grid)

print("PART 1: {}".format(len([1 for y in grid for x in y if x == '#'])))


grid = [[i for i in x] for x in content_list]
changed = 1

while (changed > 0):
	grid, changed = step(grid, True)

print("PART 2: {}".format(len([1 for y in grid for x in y if x == '#'])))