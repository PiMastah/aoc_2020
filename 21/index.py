my_file = open("input.txt", "r")
content_list = my_file.read()
lines = content_list.split('\n')

items = []

for l in lines:
	ingrs, allergs = l.split('(')

	ingrs = ingrs[:-1].split(' ')
	allergs = list(map(lambda x: x.strip(','), allergs[:-1].split(' ')[1:]))

	items.append((ingrs, allergs))

possible_pairings = set()

all_ingredients = {}

for ingrs, allergs in items:
	for i in ingrs:
		if i not in all_ingredients:
			all_ingredients[i] = 0
		all_ingredients[i] += 1	
		for a in allergs:
			foundItem = True
			for otherItem in items:
				if a in otherItem[1] and i not in otherItem[0]:
					foundItem = False
					break
			if foundItem:
				possible_pairings.add((i, a))

c = 0

to_remove = set()

for i in all_ingredients:
	found = False
	for ing, allerg in possible_pairings:
		if ing == i:
			found = True
			break
	if not found:
		c += all_ingredients[i]
		to_remove.add(i)

print("PART 1: {}".format(c))

allerg_list = {}

for i, a in possible_pairings:
	if i not in allerg_list:
		allerg_list[i] = []
	allerg_list[i].append(a)

code_map = {}

to_map = [i for i in all_ingredients if i not in to_remove]

while len(to_map) > 0:
	for x, i in enumerate(to_map):
		if len(allerg_list[i]) == 1:
			code_map[i] = allerg_list[i][0]
			to_map.remove(i)
			for j in allerg_list:
				if code_map[i] in allerg_list[j]:
					allerg_list[j].remove(code_map[i])

l = []

for a in code_map:
	l.append((a, code_map[a]))

l.sort(key=lambda x: x[1])

print("PART 2: {}".format(','.join([x[0] for x in l])))
