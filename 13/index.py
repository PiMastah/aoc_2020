my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

ts = int(content_list[0])

bus_times = content_list[1].split(',')

arrival_offsets = [(int(x), int(x) - ts % int(x)) for x in bus_times if x != 'x']

bus_with_shortest_wait = min(arrival_offsets, key=lambda x: x[1])

print("PART 1: {}".format(bus_with_shortest_wait[0] * bus_with_shortest_wait[1]))

modulo_classes = [(int(x),int(i)) for i,x in enumerate(bus_times) if x != 'x']

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = egcd(b % a, a)
		return (gcd, y - (b//a) * x, x)


def calc_common(modulo_class1, modulo_class2):
	n1, a1 = modulo_class1
	n2, a2 = modulo_class2

	_, m1, m2 = egcd(n1, n2)

	x = a1*m2*n2 + a2*m1*n1

	return n1*n2, x % (n1*n2)

x = modulo_classes[0]
for i in range(1, len(modulo_classes)):
	x = calc_common(x, modulo_classes[i])

print("PART 2: {}".format(x[0] % x[1]))
