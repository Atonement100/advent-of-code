DIRS = {"NORTH" : 0x01, "EAST" : 0x02, "SOUTH" : 0x04, "WEST" : 0x08, "FAR" : 0x10}
HEX_TO_ZONE = {0x00 : '7', 0x01 : '3', 0x02 : '8', 0x03 : '4', 0x04 : 'B', 0x06 : 'C', 0x08 : '6', 0x09 : '2', 0x0C : 'A', 0x11 : '1', 0x14 : 'D', 0x12 : '9', 0x18 : '5'}
ZONE_TO_HEX = dict((val, key) for key, val in HEX_TO_ZONE.items())

def get_relative_location(zone_hex):
	dx, dy = 0, 0
	if zone_hex & DIRS["NORTH"]:
		dy += 1
	elif zone_hex & DIRS["SOUTH"]:
		dy -= 1
		
	if zone_hex & DIRS["EAST"]:
		dx += 1
	elif zone_hex & DIRS["WEST"]:
		dx -= 1
	
	if zone_hex & DIRS["FAR"]:
		dy *= 2
		dx *= 2
	return dx, dy

def get_zone_from_location(dx, dy):
	hex = 0
	if dx > 0:
		hex |= DIRS["EAST"]
	elif dx < 0:
		hex |= DIRS["WEST"]
	if dy > 0:
		hex |= DIRS["NORTH"]
	elif dy < 0:
		hex |= DIRS["SOUTH"]
	if (abs(dx) == 2 or abs(dy) == 2):
		hex |= DIRS["FAR"]
	return HEX_TO_ZONE[hex]
	
def process_instructions(instruction, dx, dy):
		
	for dir in instruction:
		if dir == 'U':
			if dy == 1 and dx == 0:
				dy += 1;
			elif dy == 0 and abs(dx) != 2:
				dy += 1;
			elif dy < 0:
				dy += 1;
		elif dir == 'R':
			if dx == 1 and dy == 0:
				dx += 1;
			elif dx == 0 and abs(dy) != 2:
				dx += 1;
			elif dx < 0:
				dx += 1;
		elif dir == 'D':
			if dy == -1 and dx == 0:
				dy -= 1;
			elif dy == 0 and abs(dx) != 2:
				dy -= 1;
			elif dy > 0:
				dy -= 1;
		elif dir == 'L':
			if dx == -1 and dy == 0:
				dx -= 1;
			elif dx == 0 and abs(dy) != 2:
				dx -= 1;
			elif dx > 0:
				dx -= 1;
	return (dx, dy)
	
inFile = open('input.txt','r')
instruction_list = [inLine.rstrip('\n') for inLine in inFile]
dx, dy = -2, 0
for instr in instruction_list:
	dx, dy = process_instructions(instr, dx, dy)
	print(get_zone_from_location(dx, dy))
input("Press Enter to continue...")