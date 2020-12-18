import re

my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

def calc(expression):
	parts = expression.split(' ')
	v = int(parts[0])
	for i in range(int(len(parts)/2)):
		if parts[i * 2 + 1] == '+':
			v += int(parts[i * 2+2])
		else:
			v *= int(parts[i * 2+2])
	return v

add = re.compile('[0-9]+ \+ [0-9]+')

def calc_advanced(expression):
	matches = add.findall(expression)

	while len(matches) > 0:
		for m in matches:
			p = m.split(' ')
			v = int(p[0]) + int(p[2])
			expression = expression.replace(m, str(v), 1)
		matches = add.findall(expression)

	return calc(expression)

r = re.compile('\([^(^)]*\)')

s1 = 0
s2 = 0

for expression in content_list:
	matches = r.findall(expression)
	while len(matches) > 0:
		for m in matches:
			v = calc(m[1:-1])
			expression = expression.replace(m, str(v), 1)
		matches = r.findall(expression)

	s1 += calc(expression)

for expression in content_list:
	matches = r.findall(expression)
	while len(matches) > 0:
		for m in matches:
			v = calc_advanced(m[1:-1])

			expression = expression.replace(m, str(v), 1)
		matches = r.findall(expression)

	s2 += calc_advanced(expression)

print("PART 1: {}".format(s1))
print("PART 2: {}".format(s2))
