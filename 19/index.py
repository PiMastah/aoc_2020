import re, sys, itertools

my_file = open("input.txt", "r")
content_list = my_file.read()
rule_strings, messages = content_list.split('\n\n')

messages = messages.split('\n')

rules = {}

for r in rule_strings.split('\n'):
	id, s = r.split(': ')
	rules[id] = s

max_l = max([len(m) for m in messages])

def expand(s):
	if s in ['"a"', '"b"']:
		return set((s[1:-1]))

	if s in rules:
		if s not in rules[s].split(' '):
			return expand(rules[s])
		else:
			if s == '8':
				return set(('k'))
			else:
				return set(('l'))
			return new_set 

	if '|' in s:
		i = s.index('|')
		left = expand(s[:i - 1])
		right = expand(s[i + 2:])

		return left.union(right)

	if ' ' in s:
		parts = [expand(i) for i in s.split(' ')]

		products = list(map(lambda x: ''.join(x), itertools.product(*parts)))

		return {x for x in products if len(x) <= max_l}


words = expand('0')

valid = 0

for m in messages:
	if m in words:
		valid += 1

print("PART 1: {}".format(valid))

expr31 = expand('31')
expr42 = expand('42')

valid = 0

k = len(next(iter(expr31)))

for m in messages:
	ended1 = False
	ended2 = False

	count1 = 0
	count2 = 0

	for i in range(int(len(m)/k)):
		next_part = m[i*k:i*k+k]
		if not ended1 and next_part not in expr42:
			ended1 = True
		elif not ended1:
			count1 += 1
		if ended1 and next_part not in expr31:
			ended2 = True
			break
		elif ended1:
			count2 += 1

	if ended1 and not ended2 and count1 > count2:
		print(count1, count2)
		valid += 1

print("PART 2: {}".format(valid))
