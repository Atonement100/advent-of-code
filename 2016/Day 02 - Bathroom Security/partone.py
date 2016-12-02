NORTH = 0x1
EAST = 0x2
SOUTH = 0x4
WEST = 0x8
HEX_TO_ZONE = {0x0 : 5, 0x1 : 2, 0x2 : 6, 0x3 : 3, 0x4 : 8, 0x6 : 9, 0x8 : 4, 0x9 : 1, 0xC : 7}

#Location 5 is inherently 0x0
def process_instructions(instruction, start):
	currLoc = start
	for dir in instruction:
		if dir == 'U' and not (currLoc & NORTH):
			if (currLoc & SOUTH):
				currLoc &= ~SOUTH
			else:
				currLoc |= NORTH
		elif dir == 'R' and not (currLoc & EAST):
			if (currLoc & WEST):
				currLoc &= ~WEST
			else:
				currLoc |= EAST
		elif dir == 'D' and not (currLoc & SOUTH):
			if (currLoc & NORTH):
				currLoc &= ~NORTH
			else:
				currLoc |= SOUTH
		elif dir == 'L' and not (currLoc & WEST):
			if (currLoc & EAST):
				currLoc &= ~EAST
			else:
				currLoc |= WEST
	return currLoc

inFile = open('input.txt','r')
instruction_list = [inLine.rstrip('\n') for inLine in inFile]
start = 0x0
for instr in instruction_list:
	start = process_instructions(instr, start)
	print(HEX_TO_ZONE[start])
input("Press Enter to continue...")