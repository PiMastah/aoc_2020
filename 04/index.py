import sys
import re

my_file = open("input.txt", "r")
content_list = my_file.read().split('\n\n')
content_list = [re.split('\n| ', x) for x in content_list]

hcl = re.compile('#[0-9a-f]{6}')
pid = re.compile('[0-9]{9}')

def val_height(x):
	if 'in' in x:
		v = int(x.split('in')[0])
		if 59 <= v and v <= 76:
			return True
	if 'cm' in x:
		v = int(x.split('cm')[0])
		if 150 <= v and v <= 193:
			return True
	return False

validation = {
	'byr': lambda x: int(x) >= 1920 and int(x) <= 2002,
	'iyr': lambda x: int(x) >= 2010 and int(x) <= 2020,
	'eyr': lambda x: int(x) >= 2020 and int(x) <= 2030,
	'hcl': lambda x: not not hcl.match(x),
	'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
	'pid': lambda x: len(x) == 9 and not not pid.match(x),
	'hgt': lambda x: val_height(x),
}

find = lambda fun, lst: next((x for x in lst if fun(x)), None)

c_valid_simple = sum([1 for item in content_list if all([find(lambda x: x.startswith(prop), item) for prop in validation.keys()])])
c_valid_strict = sum([1 for item in content_list if all([find(lambda x: x.startswith(prop) and validation[prop](x[len(prop)+1:]), item) for prop in validation.keys()])])

print("PART 1: {}".format(c_valid_simple))
print("PART 2: {}".format(c_valid_strict))