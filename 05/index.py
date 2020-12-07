import sys

my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

seat_ids = [int(str(s).replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for s in content_list]

f = max(seat_ids)

print("PART 1: {}".format(f))
seat_ids.sort()
l = len(seat_ids)
for i, x in enumerate(seat_ids):
	if (i > 0 and seat_ids[i-1] != x-1):
		print("PART 2: {}".format(x-1))
		break