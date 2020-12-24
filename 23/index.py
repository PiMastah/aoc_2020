my_file = open("input.txt", "r")
content_list = my_file.read()

right_nodes = {}

l = list(content_list)
k = len(l)

for i, v in enumerate(l):
	right_nodes[v] = l[(i+1) % k]

moves = 100

active_node = content_list[0]

for _ in range(moves):
	first_mover = right_nodes[active_node]
	last_mover = right_nodes[right_nodes[first_mover]]
	first_non_mover = right_nodes[last_mover]
	target = str(int(active_node) - 1)
	if target == '0':
		target = str(len(content_list))
	while target == first_mover or target == right_nodes[first_mover] or target == last_mover:
		target = str(int(target) - 1)
		if target == '0':
			target = str(len(content_list))

	after_target = right_nodes[target]

	right_nodes[active_node] = first_non_mover
	right_nodes[target] = first_mover
	right_nodes[last_mover] = after_target

	active_node = right_nodes[active_node]

a = right_nodes['1']

s = ''

while a != '1':
	s += a
	a = right_nodes[a]

print("PART 1: {}".format(s))

right_nodes = {}

l = list(content_list)
k = len(l)

for i, v in enumerate(l):
	right_nodes[int(v)] = int(l[(i+1) % k])

right_nodes[int(content_list[-1])] = len(right_nodes) + 1

for i in range(len(right_nodes) + 1, 1000001):
	right_nodes[i] = i+1

right_nodes[1000000] = int(content_list[0])

moves = 10000000

active_node = int(content_list[0])

for i in range(moves):
	first_mover = right_nodes[active_node]
	last_mover = right_nodes[right_nodes[first_mover]]
	first_non_mover = right_nodes[last_mover]
	target = active_node - 1
	if target == 0:
		target = 1000000
	while target == first_mover or target == right_nodes[first_mover] or target == last_mover:
		target = target - 1
		if target == 0:
			target = 1000000

	after_target = right_nodes[target]

	right_nodes[active_node] = first_non_mover
	right_nodes[target] = first_mover
	right_nodes[last_mover] = after_target

	active_node = right_nodes[active_node]

a = right_nodes[1]

print("PART 2: {}".format(a * right_nodes[a]))