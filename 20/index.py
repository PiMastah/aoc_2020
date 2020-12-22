import math

my_file = open("input.txt", "r")
content_list = my_file.read()
tile_strings = content_list.split('\n\n')

tiles = {}

rot_r_map = {
	"N": "E",
	"E": "S",
	"S": "W",
	"W": "N"
}

ind_dir_map = {
	0: "W",
	1: "W",
	2: "E",
	3: "E",		
	4: "N",
	5: "N",
	6: "S",
	7: "S"	
}

def rotate_tile_right(lines):
	tile_length = len(lines)
	return [''.join([lines[tile_length-1-x][y] for x, c in enumerate(line)]) for y, line in enumerate(lines)]

def rotate_connections_right(connections):
	return [(rot_r_map[c[0]], c[1]) for c in connections]

def rotate(tile, connections, target_orientations):
	connection_directions = list(map(lambda x: x["match_indices"], connections))
	lines = tile["lines"]

	while target_orientations[0] not in connection_directions:
		connection_directions = rotate_connections_right(connection_directions)
		lines = rotate_tile_right(lines)

	if target_orientations[1][1] is None:
		if connection_directions[0][0] == target_orientations[1][0] or connection_directions[1][0] == target_orientations[1][0] or len(connection_directions) > 2 and connection_directions[2][0] == target_orientations[1][0]:
			if target_orientations[1][0] in ['W', 'E']:
				lines = [line[::-1] for line in lines]
				for i, c in enumerate(connection_directions):
					if c[0] in ['W', 'E']:
						connection_directions[i] = ('E' if c[0] == 'W' else 'W', c[1])
			else:
				lines = lines[::-1]
				for i, c in enumerate(connection_directions):
					if c[0] in ['N', 'S']:
						connection_directions[i] = ('N' if c[0] == 'S' else 'S', c[1])
	else:
		if connection_directions[1] not in target_orientations:
			if target_orientations[1][0] in ['W', 'E']:
				lines = [line[::-1] for line in lines]
				for i, c in enumerate(connection_directions):
					if c[0] in ['W', 'E']:
						connection_directions[i] = ('E' if c[0] == 'W' else 'W', c[1])
			else:
				lines = lines[::-1]
				for i, c in enumerate(connection_directions):
					if c[0] in ['N', 'S']:
						connection_directions[i] = ('N' if c[0] == 'S' else 'S', c[1])

	for dir, id in target_orientations:
		if dir == 'W' and id is not None:
			needs_swap = True
			for e in tiles[id]["edges"]:
				if e == ''.join([line[0] for line in lines]):
					needs_swap = False
					break
			if needs_swap:
				lines = [line[::-1] for line in lines]
				for i, c in enumerate(connection_directions):
					if c[0] in ['W', 'E']:
						connection_directions[i] = ('E' if c[0] == 'W' else 'W', c[1])

	return (lines, connection_directions)

for t in tile_strings:
	lines = t.split('\n')
	id = lines[0][5:-1]
	lines = lines[1:]

	t = lines[0]
	t_r = t[::-1]
	b = lines[-1]
	b_r = b[::-1]

	f = ''.join([l[0] for l in lines])
	f_r = f[::-1]
	l = ''.join([l[-1] for l in lines])
	l_r = l[::-1]


	tiles[id] = {
		"lines": lines,
		"edges": [f, f_r, l, l_r, t, t_r, b, b_r]
	}

adjacents = {}

for candidate_id in tiles:
	adjacents[candidate_id] = []
	for other_tile in tiles:
		if candidate_id != other_tile:
			for i, e in enumerate(tiles[candidate_id]['edges']):
				if e in tiles[other_tile]['edges']:
					adjacents[candidate_id].append({
						"other_tile": other_tile,
						"matching_edge": e,
						"match_indices": (ind_dir_map[i], other_tile)
					})
					break

v = 1
corners = []

for i in adjacents:
	if len(adjacents[i]) == 2:
		v *= int(i)
		corners.append(i)

print("PART 1: {}".format(v))

piece_ids = []

output = []

puzzle_len = int(math.sqrt(len(adjacents)))

tile_len = len(tiles[corners[0]]["lines"])

for i in range(puzzle_len):
	row = []
	for _ in range(tile_len - 2):
		output.append('')
	piece_ids.append(row)
	for j in range(puzzle_len):
		if i == 0 and j == 0:
			current_id = corners[0]
			current = adjacents[current_id]
			lines, orientations = rotate(tiles[current_id], current, [('E', current[0]["other_tile"]), ('S', current[1]["other_tile"])])
		elif i == 0 and j > 0:
			x = list(filter(lambda x: x[0][0] == 'E', orientations))
			current_id = x[0][1]
			current = adjacents[current_id]
			lines, orientations = rotate(tiles[current_id], current, [('W', piece_ids[i][j-1]), ('N', None)])
		elif i > 0 and j > 0:
			x = list(filter(lambda x: x[0][0] == 'E', orientations))
			current_id = x[0][1]
			current = adjacents[current_id]
			lines, orientations = rotate(tiles[current_id], current, [('N', piece_ids[i-1][j]), ('W', piece_ids[i][j-1])])
		elif i > 0 and j == 0:
			above_id = piece_ids[i-1][0]
			above_neighbors = list(map(lambda x: x["other_tile"], adjacents[above_id]))

			if len(above_neighbors) == 3:
				above_neighbors.remove(piece_ids[i-2][0])
			above_neighbors.remove(piece_ids[i-1][1])

			current_id = above_neighbors[0]
			current = adjacents[current_id]
			lines, orientations = rotate(tiles[current_id], current, [('N', piece_ids[i-1][0]), ('W', None)])

		row.append(current_id)

		for k, l in enumerate(lines[1:-1]):
			output[k + i * (tile_len-2)] += lines[k+1][1:-1]

sea_monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

offsets = set()

max_x = 19
max_y = 2

for y, i in enumerate(sea_monster.split('\n')):
	for x, c in enumerate(i):
		if c == '#':
			offsets.add((x, y))

monster_coords = set()

# would need to check all combinations of rotate_tile_right and flipped rotate_tile_right for output, this code works for my input but is not generic!

for y, i in enumerate(output):
	for x, c in enumerate(i):
		if x < len(i) - max_x and y < len(output) - max_y:
			match = True
			for ox, oy in offsets:
				if output[y + oy][x + ox] != '#':
					match = False
					break
			if match:
				print("MATCH", x, y)
				for ox, oy in offsets:
					monster_coords.add((x + ox, y + oy))

print("PART 2: {}".format(len([1 for y, l in enumerate(output) for x, c in enumerate(l) if c == '#' and (x, y) not in monster_coords])))
