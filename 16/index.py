import math

my_file = open("input.txt", "r")
content_list = my_file.read()

definition_strings, my_ticket_string, all_ticket_strings = content_list.split('\n\n')

definitions = {}

for s in definition_strings.split('\n'):
	n, v = s.split(': ')
	v = [(int(m1), int(m2)) for m1, m2 in [s.split('-') for s in v.split(' or ')]]
	definitions[n] = v

all_tickets = [list(map(lambda x: int(x), s.split(','))) for s in all_ticket_strings.split('\n')[1:]]

def is_valid_value(x):
	for d in definitions:
		for m1, m2 in definitions[d]:
			if x >= m1 and x <= m2:
				return True
	return False

def is_valid_value_for_def(x, valid_ranges):
	for m1, m2 in valid_ranges:
		if x >= m1 and x <= m2:
			return True
	return False

print("PART 1: {}".format(sum([x for t in all_tickets for x in t if not is_valid_value(x)])))

valid_tickets = [t for t in all_tickets if all([is_valid_value(v) for v in t])]

attrs = len(valid_tickets[0])

candidate_indices = {}

for d in definitions:
	valid_ranges = definitions[d]

	candidate_indices[d] = [] 

	for i in range(attrs):
		attr_valid = True
		for t in valid_tickets:
			if not is_valid_value_for_def(t[i], valid_ranges):
				attr_valid = False
				break
		if attr_valid:
			candidate_indices[d].append(i)

attrs_to_match = list(definitions.keys())

attr_indices = {}

while len(attrs_to_match) > 0:
	definitive_attrs = [a for a in attrs_to_match if len(candidate_indices[a]) == 1]

	for a in definitive_attrs:
		i = candidate_indices[a][0]
		attr_indices[a] = i
		candidate_indices.pop(a, None)
		attrs_to_match.remove(a)
		for a in candidate_indices:
			if i in candidate_indices[a]:
				candidate_indices[a].remove(i)

my_ticket = list(map(lambda v: int(v), my_ticket_string.split('\n')[1].split(',')))

print("PART 2: {}".format(math.prod([my_ticket[attr_indices[x]] for x in attr_indices if 'departure ' in x])))