my_file = open("input.txt", "r")
content_list = list(map(lambda x: int(x), my_file.read().split('\n')))

def find_pair_with_sum(sum, l):
	for i, x in enumerate(l):
		x = int(x)
		for j, y in enumerate(l[i+1:]):
			y = int(y)
			if x + y == sum:
				return x, y
	return None, None



for i in range(25, len(content_list)):
	x = content_list[i]
	a,b = find_pair_with_sum(x, content_list[i-25:i])
	if a is None:
		print("PART 1: {}".format(x))
		break


for j in range(0, i):
	for k in range(j+1, i):
		ended = sum(content_list[j:k]) == x
		if ended:
			print("PART 2: {}".format(max(content_list[j:k]) + min(content_list[j:k])))
			break
	if ended:
		break