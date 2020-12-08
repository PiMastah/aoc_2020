my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

def run(instructions):
	i = 0
	a = 0
	visited = {}
	looped = False
	l = len(instructions)

	while not looped and i < l:
		if i in visited:
			looped = True
			break
		visited[i] = 1
		line = instructions[i]
		instruction, val = line.split(' ')

		if instruction == 'acc':
			a += int(val)
			i += 1
		elif instruction == 'jmp':
			i += int(val)
		elif instruction == 'nop':
			i += 1

	return a, looped

print("PART 1: {}".format(run(content_list)[0]))

def change_instruction_and_build_list(change_index):
	instruction, val = content_list[change_index].split(' ')
	new_instruction_type = 'jmp' if instruction == 'nop' else 'nop'
	l = content_list[:]
	l[i] = new_instruction_type + ' ' + val
	return l

for i, l in enumerate(content_list):
	instruction, val = l.split(' ')
	if instruction in ['jmp', 'nop']:
		instructions = change_instruction_and_build_list(i)
		a, looped = run(instructions)
		if not looped:
			print("PART 2: {}".format(a))
			break
