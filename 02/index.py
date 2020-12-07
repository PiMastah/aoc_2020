import sys

my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

def is_valid_1(s, l, low, high):
	c = sum([1 for x in s if x == l])
	return low <= c and c <= high

def is_valid_2(s, l, low, high):
	return (s[low-1] == l) != (s[high-1] == l)

def validate(s, mode=1):
	val, st = s.split(': ')
	lims, letter = val.split(' ')
	low, high = lims.split('-')

	low = int(low)
	high = int(high)

	fn = is_valid_1 if mode == 1 else is_valid_2

	return fn(st, letter, low, high)

print("PART 1: {}".format(sum([1 for x in content_list if validate(x)])))
print("PART 2: {}".format(sum([1 for x in content_list if validate(x, 2)])))
