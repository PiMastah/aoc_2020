my_file = open("input.txt", "r")
pub1, pub2 = my_file.read().split('\n')

pub1 = int(pub1)
pub2 = int(pub2)

def transform(loop_size, subject_number):
	s = 1
	for _ in range(loop_size):
		s = (s * subject_number) % 20201227
	return s

def get_loop_sizes(v1, v2, subject_number):
	l = 0
	s = 1
	found1 = False
	found2 = False

	l1 = 0
	l2 = 0

	while not (found1 and found2):
		s = (s * subject_number) % 20201227
		l += 1
		if s == v1:
			l1 = l
			found1 = True
		if s == v2:
			l2 = l
			found2 = True

	return l1, l2

l1, l2 = get_loop_sizes(pub1, pub2, 7)

print("PART 1: {}".format(transform(l1, pub2)))