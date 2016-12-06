inFile = open('input.txt','r')
instruction_list = [inLine.rstrip('\n') for inLine in inFile]

length = 8

matrix = [[0 for x in range(26)] for y in range(length)]

for instr in instruction_list:
	for c in range(length):
		matrix[c][ord(instr[c]) - ord('a')] += 1
		
out = []
for y in range(length):
	maxIndex = 0
	max = float('inf')
	for x in range(26):
		if matrix[y][x] < max:
			max = matrix[y][x]
			maxIndex = x
	out.append(chr(maxIndex + ord('a')))
print(''.join(out))
	
input("Press Enter to continue...")