import sys
import re

my_file = open("input.txt", "r")
content_list = my_file.read().split('\n\n')
content_list = [re.split('\n| ', x) for x in content_list]

total_part1 = 0
total_part2 = 0
for l in content_list:
	length = len(l)
	counts = {}
	for s in l:
		for c in s:
			if not c in counts:
				counts[c] = 0
			counts[c] += 1
	total_part1 += len(counts.keys())
	total_part2 += sum([1 for x in counts.keys() if counts[x] == length])

print("PART 1: {}".format(total_part1))
print("PART 2: {}".format(total_part2))