my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

def find_pair_with_sum(sum, l):
	for i, x in enumerate(l):
		x = int(x)
		for j, y in enumerate(l[i+1:]):
			y = int(y)
			if x + y == sum:
				return x, y
	return None, None

x, y = find_pair_with_sum(2020, content_list)

print("PART 1: {}".format(x*y))

for i, x in enumerate(content_list):
	x = int(x)
	y, z = find_pair_with_sum(2020 - x, content_list[i+1:])
	if y is not None:
		print("PART 2: {}".format(x*y*z))
		break
