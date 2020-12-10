my_file = open("input.txt", "r")
content_list = list(map(lambda x: int(x), my_file.read().split('\n')))

content_list.sort()

l = [x - content_list[i-1] for i, x in enumerate(content_list) if i > 0]

diffs_1 = sum([1 for x in l if x == 1])

diffs_3 = 1 + sum([1 for x in l if x == 3])

if content_list[0] == 1:
	diffs_1 += 1
if content_list[0] == 3: 
	diffs_3 += 1

print("PART 1: {}".format(diffs_1 * diffs_3))

content_list.reverse()

content_list = [content_list[0] + 3] + content_list + [0]

available_hops = [len([1 for y in content_list if y > x and y <= x +3 ]) for x in content_list]

available_hops[0] = 1

steps = [1]

for x in available_hops:
	steps.append(sum(steps[-x:]))

print("PART 2: {}".format(steps[-1]))