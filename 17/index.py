my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

grid = {}

coords = [(x, y, 0) for y, l in enumerate(content_list) for x, c in enumerate(l) if c == '#']

for t in coords:
	grid[t] = 1

def enumerate_neighbors(t):
	x, y, z = t
	return [(x-1+i, y-1+j, z-1+k) for i in range(3) for j in range(3) for k in range(3)]

def enumerate_neighbors2(t):
	x, y, z, q = t
	return [(x-1+i, y-1+j, z-1+k, q-1+l) for i in range(3) for j in range(3) for k in range(3) for l in range(3)]

def step(grid, part2 = False):
	new_grid = {}

	fn = enumerate_neighbors2 if part2 else enumerate_neighbors

	q = []
	checked = {}

	for t in grid:
		q += fn(t)

	for t in q:
		if not t in checked:
			checked[t] = 1
			l = len([1 for n in fn(t) if n in grid]) - (1 if t in grid else 0)
			if (t in grid and l == 2) or l == 3:
				new_grid[t] = 1

	return new_grid

steps = 6

for _ in range(steps):
	grid = step(grid)

print("PART 1: {}".format(len(grid)))

grid = {}

coords = [(x, y, 0, 0) for y, l in enumerate(content_list) for x, c in enumerate(l) if c == '#']

for t in coords:
	grid[t] = 1

steps = 6

for _ in range(steps):
	grid = step(grid, True)

print("PART 2: {}".format(len(grid)))
