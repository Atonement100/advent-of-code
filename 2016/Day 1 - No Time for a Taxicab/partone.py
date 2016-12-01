def direction_split(str):
	direction = str.rstrip('0123456789')
	distance = str[len(direction):]
	return direction, distance

def process_directions(dir_tuples):
	direction = 0
	towards_east = 0
	towards_north = 0
	for dir in dir_tuples:
		if dir[0] == 'R':
			direction = (direction + 1) % 4
		else:
			direction = (direction - 1) % 4
		if direction == 0:
			towards_north += int(dir[1])
		elif direction == 1:
			towards_east += int(dir[1])
		elif direction == 2:
			towards_north -= int(dir[1])
		else:
			towards_east -= int(dir[1])
	return towards_north, towards_east


inFile = open('input.txt','r')
dir_list = inFile.read().split(", ")
dir_tuples = [direction_split(str) for str in dir_list]
(north, east) = process_directions(dir_tuples)
print(north + east)
input("Press Enter to continue...")