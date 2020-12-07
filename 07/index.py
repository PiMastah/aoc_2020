my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

bags = {}

for item in content_list:
	parts = item.split(' contain ')

	bags[parts[0][:-1]] = {
		'valid_contents' : [],
		'amounts': []
	}

	for b in parts[1][:-1].split(', '):
		i = b.find(' ')
		if b[:i] != 'no':
			amount = int(b[:i])
			t = b[i+1:]
			if amount > 1:
				t = t[:-1]
			bags[parts[0][:-1]]['valid_contents'].append(t)
			bags[parts[0][:-1]]['amounts'].append(amount)

def find_outer_bags(name):
	containers = []
	for t in bags:
		if name in bags[t]['valid_contents']:
			containers.append(t)
	return containers

to_check = find_outer_bags('shiny gold bag')

found = []

while len(to_check) > 0:
	i = to_check.pop()
	if i not in found:
		found.append(i)
		to_check = to_check + find_outer_bags(i)
print("PART 1: {}".format(len(found)))

def get_inner_count(x):
	c = 0
	if len(bags[x]['valid_contents']) == 0:
		return c
	else:
		for i, b in enumerate(bags[x]['valid_contents']):
			c += bags[x]['amounts'][i] + bags[x]['amounts'][i] * get_inner_count(b)
	return c

print("PART 2: {}".format(get_inner_count('shiny gold bag')))
