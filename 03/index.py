import sys

my_file = open("input.txt", "r")
content_list = my_file.read().split('\n')

grid = [[i for i in x] for x in content_list]

l = len(grid)
w = len(grid[0])

def is_tree(x, y):
	return grid[y][x] == '#'

def check_slope(x_off, y_off):

	my_y = 0
	my_x = 0
	c_trees = 0

	while my_y < l:
		if is_tree(my_x, my_y):
			c_trees += 1
		my_x = (my_x + x_off) % w
		my_y += y_off

	return c_trees

x0 = check_slope(1, 1)
x1 = check_slope(3, 1)
x2 = check_slope(5, 1)
x3 = check_slope(7, 1)
x4 = check_slope(1, 2)

print("PART 1: {}".format(x1))


print("PART 2: {}".format(x0*x1*x2*x3*x4))