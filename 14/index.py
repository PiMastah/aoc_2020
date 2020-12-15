my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

mem = {}
mask = ''

for x in content_list:
	target, val = x.split(' = ')
	if target == 'mask':
		mask = val
	else:
		bit_str = '{:036b}'.format(int(val))
		intval = int(''.join([x if x != 'X' else bit_str[i] for i, x in enumerate(mask)]), 2)
		mem[target[4:-1]] = intval

print("PART 1: {}".format(sum([mem[x] for x in mem])))

def write(address, value, mem):
	if 'X' in address:
		i = address.index('X')
		zero_mask = address[:i] + '0' + address[i+1:]
		one_mask = address[:i] + '1' + address[i+1:]
		write(zero_mask, value, mem)
		write(one_mask, value, mem)
	else:
		mem[address] = value

mem = {}
mask = ''

for x in content_list:
	target, val = x.split(' = ')
	if target == 'mask':
		mask = val
	else:
		bit_str_a = '{:036b}'.format(int(target[4:-1]))
		intval = int(val)
		a_masked = ''.join([x if x != '0' else bit_str_a[i] for i, x in enumerate(mask)])

		write(a_masked, intval, mem)

print("PART 2: {}".format(sum([mem[x] for x in mem])))