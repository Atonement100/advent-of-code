def process_row_triangle(tri):
	nums = [int(n) for n in tri.split()]
	nums.sort()
	if (nums[0] + nums[1] <= nums[2]):
		return 0;
	return 1;

def process_column_triangle(a, b, c):
	numsa = [int(n) for n in a.split()]
	numsb = [int(n) for n in b.split()]
	numsc = [int(n) for n in c.split()]

	total_good = 0
	for k in range(0,3):
		total_good += process_row_triangle(str(numsa[k]) + " " + str(numsb[k]) + " " + str(numsc[k]))	
	return total_good;
	
inFile = open('input.txt','r')
instruction_list = [inLine.rstrip('\n') for inLine in inFile]
num_possible = 0
num_possible_col = 0
for instr in instruction_list:
	num_possible += process_row_triangle(instr)
for a,b,c in zip(*[iter(instruction_list)]*3):
	num_possible_col += process_column_triangle(a,b,c)

print("Solution to part one: " + str(num_possible))
print("Solution to part two: " + str(num_possible_col))
input("Press Enter to continue...")